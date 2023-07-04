# TalkFamous API Reference

## User Profile API

### GET /user/{userId}

Fetches the user profile data.

**Parameters**

- `userId` (required): The ID of the user.

**Response**

Returns a `UserSchema` object.

---

### POST /user

Updates the user profile data.

**Parameters**

- `user_data` (required): The updated user data.

**Response**

Returns a `userUpdate` message.

---

## Creator Profile API

### GET /creator/{creatorId}

Fetches the creator profile data.

**Parameters**

- `creatorId` (required): The ID of the creator.

**Response**

Returns a `CreatorSchema` object.

---

### POST /creator

Updates the creator profile data.

**Parameters**

- `creator_data` (required): The updated creator data.

**Response**

Returns a `creatorUpdate` message.

---

## AI Companion API

### GET /ai-companion/{companionId}

Fetches the AI companion data.

**Parameters**

- `companionId` (required): The ID of the AI companion.

**Response**

Returns an `AICompanionSchema` object.

---

### POST /ai-companion

Updates the AI companion data.

**Parameters**

- `ai_companion_data` (required): The updated AI companion data.

**Response**

Returns an `aiCompanionUpdate` message.

---

## Chatbot API

### GET /chatbot/{chatbotId}

Fetches the chatbot data.

**Parameters**

- `chatbotId` (required): The ID of the chatbot.

**Response**

Returns a `ChatbotSchema` object.

---

### POST /chatbot

Updates the chatbot data.

**Parameters**

- `chatbot_data` (required): The updated chatbot data.

**Response**

Returns a `chatbotUpdate` message.

---

## Community API

### GET /community/{communityId}

Fetches the community data.

**Parameters**

- `communityId` (required): The ID of the community.

**Response**

Returns a `CommunitySchema` object.

---

### POST /community

Updates the community data.

**Parameters**

- `community_data` (required): The updated community data.

**Response**

Returns a `communityUpdate` message.

---

## Analytics API

### GET /analytics/{analyticsId}

Fetches the analytics data.

**Parameters**

- `analyticsId` (required): The ID of the analytics.

**Response**

Returns an `AnalyticsSchema` object.

---

### POST /analytics

Updates the analytics data.

**Parameters**

- `analytics_data` (required): The updated analytics data.

**Response**

Returns an `analyticsUpdate` message.

---

## Monetization API

### GET /monetization/{monetizationId}

Fetches the monetization data.

**Parameters**

- `monetizationId` (required): The ID of the monetization.

**Response**

Returns a `MonetizationSchema` object.

---

### POST /monetization

Updates the monetization data.

**Parameters**

- `monetization_data` (required): The updated monetization data.

**Response**

Returns a `monetizationUpdate` message.