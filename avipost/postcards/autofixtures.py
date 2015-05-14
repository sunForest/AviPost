from .models import Postcard
from autofixture import generators, register, AutoFixture


class PostcardAutoFixture(AutoFixture):

    default_cover_sizes = (
        (800, 600),
        (600, 800),
        (1200, 600),
        (600, 1200),
        (1000, 1000),
    )

    field_values = {
        'cover': generators.ImageGenerator(sizes=default_cover_sizes),
    }

register(Postcard, PostcardAutoFixture)