from django.core.management.base import BaseCommand
from django_postgres_drop_index.utils import drop_all_indexes


class Command(BaseCommand):

    def handle(self, *args, **options):
        drop_all_indexes()
