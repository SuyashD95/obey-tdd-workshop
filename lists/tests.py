from django.test import TestCase


# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/index.html", "Response doesn't return homepage template.")

    def test_handles_post_requests(self):
        response = self.client.post("/", {"item_text": "a list item"})
        self.assertIn("a list item", response.content.decode(), "Homepage cannot handle POST requests")
