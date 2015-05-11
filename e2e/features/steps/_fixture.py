"""
Use django and autofixture to manage test database environment
"""
import subprocess
import os

# implicit dependencies
# import django
# import autofixture


class Fixture(object):

    """ utilities to clean up database and load fixture """

    def __init__(self, manager):
        """ manager: path of manage.py """
        self.manager = manager

    def exec_manage(self, subcommand, *args):
        """ execute command using manage.py """
        cmd = (
            ['python', self.manager, subcommand] +
            ['--settings=avipost.settings.ci'] +
            list(args)
        )

        devnull = open(os.devnull, 'w')
        subprocess.call(cmd, stdout=devnull)

    def clean_db(self):
        """ clean database """
        self.exec_manage('flush', '--noinput')

    def load_data(self, model, count):
        """ load <count> models

        :model: name of model, e.g. Postcard
        :count: integer, e.g. 3

        """
        self.exec_manage(
            'loadtestdata', 'postcards.{0}:{1}'.format(model, count)
        )


# for manual test
# if __name__ == '__main__':
#     clean_db()
