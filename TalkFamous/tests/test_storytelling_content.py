```python
import unittest
from TalkFamous.src.storytelling_content import StorytellingContent

class TestStorytellingContent(unittest.TestCase):

    def setUp(self):
        self.storytelling_content = StorytellingContent()

    def test_create_documentary(self):
        creator_data = {"creator_id": "123", "creator_name": "John Doe"}
        result = self.storytelling_content.create_documentary(creator_data)
        self.assertEqual(result['status'], 'success')

    def test_storytelling_techniques(self):
        user_data = {"user_id": "456", "user_name": "Jane Doe"}
        result = self.storytelling_content.storytelling_techniques(user_data)
        self.assertEqual(result['status'], 'success')

    def test_engage_fans(self):
        user_data = {"user_id": "789", "user_name": "Bob Smith"}
        result = self.storytelling_content.engage_fans(user_data)
        self.assertEqual(result['status'], 'success')

    def test_attract_creators(self):
        creator_data = {"creator_id": "321", "creator_name": "Alice Johnson"}
        result = self.storytelling_content.attract_creators(creator_data)
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
```