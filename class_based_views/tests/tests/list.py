from class_based_views.tests.models import Author
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase

class ListViewTest(TestCase):
    fixtures = ['generic-views-test-data.json']
    urls = 'class_based_views.tests.urls'

    def test_list_dict(self):
        res = self.client.get('/list/dict/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object_list'], [
            {'first': 'John', 'last': 'Lennon'},
            {'last': 'Yoko',  'last': 'Ono'},
        ])
        self.assertTemplateUsed(res, 'tests/list.html')
