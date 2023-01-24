from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Магазин')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductListViewTestCase(TestCase):
    fixtures = ['category.json', 'products.json']

    def setUp(self):
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._common_tests(response)

        self.assertEqual(list(response.context_data['object_list']),
                         list(self.products[:3]))

    def text_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'categody_id': category.id})
        response = self.client.get(path)

        self._common_tests(response)

        self.assertEqual(list(response.context_data['object_list']),
                         list(self.products.filter(category_id=category.id)))

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Магазин -  Каталог')
        self.assertTemplateUsed(response, 'products/products.html')
