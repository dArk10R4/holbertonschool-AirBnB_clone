import unittest
from models.user import User

class TestUser(unittest.TestCase):
    user = None
    def setUp(self) -> None:
        self.user = User()
    
    def tearDown(self) -> None:
        del self.user

    def test_create_user(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
    def test_email(self):
        print(self.user)
        self.assertEqual(self.user.email, "")
        self.user.email = "nese@mail.com"
        self.assertEqual(self.user.email, "nese@mail.com")
if __name__ == "__main__":
    unittest.main()