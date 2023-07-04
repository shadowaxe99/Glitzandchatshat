-- Inserting sample data into the User table
INSERT INTO UserSchema (user_data) VALUES 
('{"username": "user1", "preferences": {"voice_meme": true, "anonymous_messaging": true}}'),
('{"username": "user2", "preferences": {"voice_meme": false, "anonymous_messaging": true}}');

-- Inserting sample data into the Creator table
INSERT INTO CreatorSchema (creator_data) VALUES 
('{"creator_name": "creator1", "content": {"videos": ["video1", "video2"], "voice_memes": ["meme1", "meme2"]}}'),
('{"creator_name": "creator2", "content": {"videos": ["video3", "video4"], "voice_memes": ["meme3", "meme4"]}}');

-- Inserting sample data into the AI Companion table
INSERT INTO AICompanionSchema (ai_companion_data) VALUES 
('{"companion_name": "companion1", "interactions": {"user1": "interaction1", "user2": "interaction2"}}'),
('{"companion_name": "companion2", "interactions": {"user1": "interaction3", "user2": "interaction4"}}');

-- Inserting sample data into the Chatbot table
INSERT INTO ChatbotSchema (chatbot_data) VALUES 
('{"chatbot_name": "chatbot1", "interactions": {"user1": "interaction1", "user2": "interaction2"}}'),
('{"chatbot_name": "chatbot2", "interactions": {"user1": "interaction3", "user2": "interaction4"}}');

-- Inserting sample data into the Community table
INSERT INTO CommunitySchema (community_data) VALUES 
('{"community_name": "community1", "user_generated_content": ["content1", "content2"] }'),
('{"community_name": "community2", "user_generated_content": ["content3", "content4"] }');

-- Inserting sample data into the Analytics table
INSERT INTO AnalyticsSchema (analytics_data) VALUES 
('{"user_engagement": {"user1": "engagement1", "user2": "engagement2"}, "app_usage": {"user1": "usage1", "user2": "usage2"}, "audience_behavior": {"user1": "behavior1", "user2": "behavior2"}}');

-- Inserting sample data into the Monetization table
INSERT INTO MonetizationSchema (monetization_data) VALUES 
('{"subscription_plans": {"user1": "plan1", "user2": "plan2"}, "in_app_purchases": {"user1": "purchase1", "user2": "purchase2"}, "revenue": {"user1": "revenue1", "user2": "revenue2"}}');