from django.core.management.base import BaseCommand
from django_postgres_drop_index.utils import drop_table_indexes


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('tablename', nargs='+')

    def handle(self, *args, **options):
        for tablename in options['tablename']:
            schemaname = 'public'
            if '.' in tablename:
                schemaname, tablename in tablename.split('.')
            drop_table_indexes(tablename, schemaname=schemaname)
