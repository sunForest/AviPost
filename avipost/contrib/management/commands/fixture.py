import importlib

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create Fixture'

    def add_arguments(self, parser):
        parser.add_argument('creator', nargs='?', default=None)
        parser.add_argument('--par', nargs='?', default='')

    def handle(self, *args, **options):
        if options['creator']:
            # generate fixtures
            self._handle_create(options['creator'], options['par'])
        else:
            # do other work
            pass

    def _parse_args(self, args):
        if args == '':
            return [], {}
        tokens = args.split(',')
        pos_args = list(t for t in tokens if '=' not in t)
        kw_args = dict(t.split('=') for t in tokens if '=' in t)
        return pos_args, kw_args

    def _handle_create(self, creator, args):
        args, kw = self._parse_args(args)
        mod = importlib.import_module('..' + creator, __name__)
        mod.create(*args, **kw)
