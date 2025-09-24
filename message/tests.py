from django.test import SimpleTestCase
from django.urls import reverse

class MessagePageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/message/")  # توجه به /message/
        self.assertEqual(response.status_code, 200)  # بررسی وضعیت کد پاسخ
 
    def test_url_available_by_name(self):
        response = self.client.get(reverse('message'))  # استفاده از reverse برای پیدا کردن URL از نام
        self.assertEqual(response.status_code, 200)  # بررسی وضعیت کد پاسخ

    def test_template_name(self):
        response = self.client.get(reverse('message'))  # استفاده از reverse برای پیدا کردن URL از نام
        self.assertTemplateUsed(response, 'home.html')  # بررسی اینکه آیا قالب home.html استفاده شده است

    def test_template_content(self):
        response = self.client.get (reverse('message'))
        self.assertContains(response, '<h1> This is your message</h1>')