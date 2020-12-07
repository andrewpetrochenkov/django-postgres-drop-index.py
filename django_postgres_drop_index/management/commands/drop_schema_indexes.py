from django.core.management.base import BaseCommand
from django_postgres_drop_index.utils import drop_schema_indexes


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('schemaname', nargs='+')

    def handle(self, *args, **options):
        for schemaname in options['schemaname']:
            drop_schema_indexes(schemaname)
