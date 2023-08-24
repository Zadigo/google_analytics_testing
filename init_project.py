import asyncio
import dataclasses
import os
import random
from collections import OrderedDict
from pathlib import Path
from django.utils.log import configure_logging
import django
from django.db.models import Model
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent

os.environ.setdefault('DJANGO_ALLOW_ASYNC_UNSAFE', 'True')

settings.configure(
    BASE_DIR=BASE_DIR,
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_analytics'
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

)

django.setup()


class DataModel:
    @property
    def fields(self):
        return dataclasses.fields(self)

    def as_dict(self):
        result = OrderedDict()
        for field in self.fields:
            result[field] = getattr(self, field)

        self.fields['name'] = None
        return result


@dataclasses.dataclass
class Product(DataModel):
    model: str
    pk: int
    name: str
    fields: str = dataclasses.field(default_factory=dict)


@dataclasses.dataclass
class Article(DataModel):
    pk: int
    title: str


async def create(model, params):
    if not isinstance(model, Model):
        raise ValueError('Is not a model')
    return model.objects.save(**params)


async def create_products(k=100):
    queue = asyncio.Queue()
    for i in range(k):
        await queue.put(Product(i + 1, 'Some name'))
    while not queue.empty():
        product = await queue.get()
        create(None, product.as_dict())
        print('Creating product', product)
        await asyncio.sleep(random.randrange(0, 5))


async def create_articles(k=10):
    queue = asyncio.Queue()
    for i in range(k):
        await queue.put(Article(i + 1, 'Some name'))
    while not queue.empty():
        article = await queue.get()
        create(None, article.as_dict())
        print('Creating article', article)
        await asyncio.sleep(random.randrange(0, 5))


async def main():
    await asyncio.gather(create_products(), create_articles())

if __name__ == '__main__':
    asyncio.run(main())
