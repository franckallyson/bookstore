import pytest

from product.factories import CategoryFactory


@pytest.fixture
def category_created():
    return CategoryFactory(title='random title', slug='rant', description='random description')


@pytest.mark.django_db
def test_create_created_category(category_created):
    assert category_created.title == 'random title'
