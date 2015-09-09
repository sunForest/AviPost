import os


class Env(object):
    """ Set and restore environment variables """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __enter__(self):
        self.old_value = os.environ.get(self.key, None)
        os.environ[self.key] = str(self.value)
        return self.value

    def __exit__(self, type, value, traceback):
        if self.old_value is not None:
            os.environ[self.key] = self.old_value
        else:
            os.environ.pop(self.key)


def setenv(key, value):
    return Env(key, value)
