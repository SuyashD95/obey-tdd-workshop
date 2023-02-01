from django.test import TestCase


# Create your tests here.
class HomePageTest(TestCase):

    def test_math_works(self):
        response = self.client.get("/")
        self.assertIn(
            "<title>To-Do lists</title>",
            response.content.decode(),
            "No title with 'To-Do lists' was found on homepage."
        )
        self.assertTrue(response.content.decode().strip().startswith("<html>"), "Response doesn't start with <html> tag.")
        self.assertTrue(response.content.decode().strip().endswith("</html>"), "Response doesn't end with </html> tag.")
