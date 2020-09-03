from django.test import TestCase


class MainPageViewTest(TestCase):
    def test_get_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
