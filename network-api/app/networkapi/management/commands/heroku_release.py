from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.contrib.sites.models import Site
from mezzanine.conf import settings

class Command(BaseCommand):
    help = 'migrate the database if needed, and optionally seed the database using app/networkapi/fixtures/test_data.json'

    def handle(self, *args, **options):

        call_command('migrate')

        if settings.LOAD_FIXTURE:
            call_command('loaddata', 'app/networkapi/fixtures/test_data.json')
            site = Site.objects.get(id=1)
            site.domain = 'localhost:8000'
            site.save()