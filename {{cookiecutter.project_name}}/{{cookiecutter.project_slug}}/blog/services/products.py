from django.db.models import QuerySet
from {{cookiecutter.project_slug}}.blog.models import Product


def create_product(*, name: str) -> QuerySet[Product]:
    return Product.objects.create(name=name)
