import pytest

from order.factories import OrderFactory
from product.factories import ProductFactory, CategoryFactory


@pytest.fixture
def order_created():
    return OrderFactory(product=[
                            ProductFactory(price=30,
                                category=[CategoryFactory(title='random title', slug='rant', description='random description'),
                                        CategoryFactory(title='random title 2', slug='ranttwo', description='random description 2')],
                                title='Random Product Title'),
                            ProductFactory(price=35,
                                category=[CategoryFactory(title='random title 4', slug='rantfuor', description='random description 4'),
                                        CategoryFactory(title='random title 3', slug='rantthree',description='random description 4')],
                                title='Random Product Title 2'),
                        ])


@pytest.mark.django_db
def test_create_order_created(order_created):
    product_titles = [product.title for product in order_created.product.all()]
    assert 'Random Product Title' in product_titles
    assert 'Random Product Title 2' in product_titles
