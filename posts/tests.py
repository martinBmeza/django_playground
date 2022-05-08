from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Con esto creo unos datos para hacerle pruebas
        #uso el modelo que defini, que es el que quiero testear
        cls.post = Post.objects.create(text="This is a test")
        
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test")
    
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/home2/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home2"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home2.html")
        self.assertContains(response, "This is a test")