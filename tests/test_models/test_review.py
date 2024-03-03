#!/usr/bin/python3

"""Unittest for Review"""

from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    review = None

    def setUp(self) -> None:
        self.review = Review()

    def tearDown(self) -> None:
        del self.review

    def test_create_review(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
        del review

    def test_place_id(self):
        self.assertEqual(self.review.place_id, "")
        self.review.place_id = "123"
        self.assertEqual(self.review.place_id, "123")

    def test_user_id(self):
        self.assertEqual(self.review.user_id, "")
        self.review.user_id = "123"
        self.assertEqual(self.review.user_id, "123")

    def test_text(self):
        self.assertEqual(self.review.text, "")
        self.review.text = "Great place"
        self.assertEqual(self.review.text, "Great place")


if __name__ == "__main__":
    unittest.main()
