from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase


class TestContactForm(TestCase):

    def setUp(self):
        self.url = reverse('contact_form')
        self.data = {
            'name': 'Lincoln Clay',
            'email': 'lincoln.clay@cia.gov',
            'message': "Family isn't who you're born with, it's who you die "
            "for.",
        }.copy()

    def test_good(self):
        response = self.client.post(self.url, self.data)
        self.assertRedirects(
            response, '/thank-you/', fetch_redirect_response=False)
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertIn(self.data['name'], message.body)
        self.assertIn(self.data['email'], message.body)
        self.assertIn(self.data['message'], message.body)

    def test_missing_data(self):
        del self.data['message']
        response = self.client.post(self.url, self.data, HTTP_REFERER='/origin/')
        self.assertRedirects(
            response, '/origin/', fetch_redirect_response=False)

    def test_missing_data_no_referer(self):
        del self.data['message']
        response = self.client.post(self.url, self.data)
        self.assertRedirects(
            response, '/', fetch_redirect_response=False)

    def test_missing_data_ajax(self):
        del self.data['message']
        response = self.client.post(
            self.url, self.data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.content, b'{"message": ["This field is required."]}')
