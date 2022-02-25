from unicodedata import category
from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='Adventure', slug='Adventure')

    def test_category_model_entry(self):
        """
        Test category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        """
        Test category model default name
        """
        data = self.data1
        self.assertTrue(str(data), 'Adventure')

class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='Adventure', slug='Adventure')
        User.objects.create(username='Admin')
        self.data1 = Product.objects.create(
            category_id=1,
            title='One Piece',
            created_by_id=1,
            slug='one-pice',
            price='10.0',
            image='one-piece'
        )
    
    def test_product_model_entry(self):
        """
        Test product model data insertion/types/fields attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertTrue(str(data), 'One Piece')