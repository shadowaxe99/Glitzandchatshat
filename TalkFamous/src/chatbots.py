```python
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import load_chatbot_data, save_chatbot_data

class Chatbot:
    def __init__(self, name):
        self.name = name
        self.chatbot_data = load_chatbot_data(name)
        self.vectorizer = TfidfVectorizer()

    def train(self, conversations):
        self.chatbot_data.extend(conversations)
        save_chatbot_data(self.name, self.chatbot_data)
        self.vectorizer.fit_transform([message for conversation in self.chatbot_data for message in conversation])

    def respond(self, message):
        responses = []
        for conversation in self.chatbot_data:
            if message in conversation:
                responses.append(conversation[(conversation.index(message) + 1) % len(conversation)])
        if responses:
            return random.choice(responses)
        else:
            return self.generate_response(message)

    def generate_response(self, message):
        tfidf = self.vectorizer.transform([message])
        max_similarity = 0
        response = None
        for conversation in self.chatbot_data:
            for i in range(len(conversation) - 1):
                similarity = cosine_similarity(tfidf, self.vectorizer.transform([conversation[i]]))
                if similarity > max_similarity:
                    max_similarity = similarity
                    response = conversation[i + 1]
        return response

def updateChatbot(name, conversations):
    chatbot = Chatbot(name)
    chatbot.train(conversations)
```
