<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-postgres-drop-index.svg?maxAge=3600)](https://pypi.org/project/django-postgres-drop-index/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-postgres-drop-index.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-postgres-drop-index.py/actions)

### Installation
```bash
$ [sudo] pip install django-postgres-drop-index
```

#### Features
+   ignores primary and unique indexes

##### `settings.py`
```python
INSTALLED_APPS+=['django_postgres_drop_index']
```

#### Examples
```bash
$ python manage.py drop_index "indexname1" "indexname2"
```

```bash
$ python manage.py drop_table_indexes "tablename1" "tablename2"
```

```bash
$ python manage.py drop_schema_indexes "public"
```

```bash
$ python manage.py drop_all_indexes
```

```python
from django_postgres_drop_index import drop_index

drop_index(indexname="indexname",schemaname='schemaname')
```

```python
from django_postgres_drop_index import drop_table_indexes

drop_table_indexes(tablename="tablename",schemaname='schemaname')
```

```python
from django_postgres_drop_index import drop_schema_indexes

drop_schema_indexes(schemaname='schemaname')
```

```python
from django_postgres_drop_index import drop_all_indexes

drop_all_indexes()
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
