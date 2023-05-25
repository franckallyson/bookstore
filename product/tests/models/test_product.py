import pytest

from product.factories import CategoryFactory, ProductFactory

@pytest.fixture
def product_created():
    return ProductFactory(price=30,
                          category=[CategoryFactory(title='random title', slug='rant', description='random description'),
                                    CategoryFactory(title='random title 2', slug='ranttwo', description='random description 2')],
                          title='Random Product Title')


@pytest.mark.django_db
def test_create_product_created(product_created):
    assert product_created.price == 30
