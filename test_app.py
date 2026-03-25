import unittest
from app import app
class FurrEverTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
    def test_homepage(self):
        response = self.client.get("/")
        print("Homepage:", response.status_code)
        self.assertEqual(response.status_code, 200)
    def test_auth_page(self):
        response = self.client.get("/auth")
        print("Auth Page:", response.status_code)
        self.assertEqual(response.status_code, 200)
    def test_adoption_page(self):
        response = self.client.get("/adopt")
        print("Adoption Page:", response.status_code)
        self.assertIn(response.status_code, [200,302])
    def test_pawgram_page(self):
        response = self.client.get("/paw-gram")
        print("Paw-Gram Page:", response.status_code)
        self.assertIn(response.status_code, [200,302])
    def test_abuse_report(self):
        response = self.client.get("/report-abuse")
        print("Report Abuse Page:", response.status_code)
        self.assertIn(response.status_code, [200,302])
if __name__ == "__main__":
    unittest.main()