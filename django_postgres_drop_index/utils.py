from django.db import connection

from .classes import Index


def get_indexes():
    sql = """
SELECT n.nspname AS schemaname,t.relname AS tablename,c.relname AS indexname
from pg_catalog.pg_class c
JOIN pg_catalog.pg_namespace n on n.oid = c.relnamespace
JOIN pg_catalog.pg_index i on i.indexrelid = c.oid
JOIN pg_catalog.pg_class t on i.indrelid   = t.oid
WHERE
    c.relkind = 'i' AND NOT i.indisprimary AND NOT i.indisunique
    AND n.nspname not in ('pg_catalog', 'pg_toast')
    AND pg_catalog.pg_table_is_visible(c.oid)
ORDER BY n.nspname,t.relname,c.relname;
    """
    cursor = connection.cursor()
    cursor.execute(sql.strip())
    indexes = []
    for r in cursor.fetchall():
        schemaname, tablename, indexname = r
        index = Index(schemaname, tablename, indexname)
        indexes.append(index)
    return indexes


def drop_index(indexname, schemaname=None):
    if not schemaname:
        schemaname = 'public'
    sql = """DROP INDEX IF EXISTS "%s"."%s" CASCADE;""" % (
        schemaname, indexname)
    cursor = connection.cursor()
    print(sql.strip())
    cursor.execute(sql.strip())


def drop_table_indexes(tablename, schemaname=None):
    if not schemaname:
        schemaname = 'public'
    for index in get_indexes():
        if index.schemaname == schemaname and index.tablename == tablename:
            drop_index(indexname=index.indexname, schemaname=index.schemaname)


def drop_schema_indexes(schemaname):
    for index in get_indexes():
        if index.schemaname == schemaname:
            drop_index(indexname=index.indexname, schemaname=index.schemaname)


def drop_all_indexes():
    for index in get_indexes():
        drop_index(indexname=index.indexname, schemaname=index.schemaname)
