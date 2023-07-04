```python
import unittest
from TalkFamous.src.monetization import Monetization

class TestMonetization(unittest.TestCase):

    def setUp(self):
        self.monetization = Monetization()
        self.user_data = {
            "id": 1,
            "name": "Test User",
            "subscription": "premium",
            "in_app_purchases": ["voice_meme", "exclusive_content"],
            "revenue": 100.00
        }
        self.creator_data = {
            "id": 1,
            "name": "Test Creator",
            "content": ["video1", "video2"],
            "exclusive_memberships": ["gold", "silver"],
            "revenue": 1000.00
        }

    def test_update_user_subscription(self):
        self.monetization.update_user_subscription(self.user_data["id"], "standard")
        self.assertEqual(self.user_data["subscription"], "standard")

    def test_update_creator_revenue(self):
        self.monetization.update_creator_revenue(self.creator_data["id"], 2000.00)
        self.assertEqual(self.creator_data["revenue"], 2000.00)

    def test_add_in_app_purchase(self):
        self.monetization.add_in_app_purchase(self.user_data["id"], "extra_storage")
        self.assertIn("extra_storage", self.user_data["in_app_purchases"])

    def test_add_exclusive_membership(self):
        self.monetization.add_exclusive_membership(self.creator_data["id"], "platinum")
        self.assertIn("platinum", self.creator_data["exclusive_memberships"])

if __name__ == '__main__':
    unittest.main()
```