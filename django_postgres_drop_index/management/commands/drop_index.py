from django.core.management.base import BaseCommand
from django_postgres_drop_index.utils import drop_index


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('indexname', nargs='+')

    def handle(self, *args, **options):
        for indexname in options['indexname']:
            schemaname = 'public'
            if '.' in indexname:
                schemaname, indexname in indexname.split('.')
            drop_index(indexname, schemaname=schemaname)
