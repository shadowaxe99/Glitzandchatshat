-- Migration script for TalkFamous database

BEGIN TRANSACTION;

-- User table
ALTER TABLE user_data
ADD COLUMN last_login TIMESTAMP;

-- Creator table
ALTER TABLE creator_data
ADD COLUMN total_followers INT,
ADD COLUMN total_likes INT;

-- AI Companion table
ALTER TABLE ai_companion_data
ADD COLUMN interaction_count INT;

-- Chatbot table
ALTER TABLE chatbot_data
ADD COLUMN response_time FLOAT;

-- Community table
ALTER TABLE community_data
ADD COLUMN total_posts INT;

-- Analytics table
ALTER TABLE analytics_data
ADD COLUMN active_users INT,
ADD COLUMN session_duration FLOAT;

-- Monetization table
ALTER TABLE monetization_data
ADD COLUMN total_revenue FLOAT;

COMMIT;