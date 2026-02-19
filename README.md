## Discord Message-to-Webhook Forwarder

A lightweight Discord bot that adds a **Context Menu** (Apps menu) to messages, allowing you to forward message content and metadata to any external HTTP Webhook with a single click.

---

### 🚀 Features

* **Context Menu Integration:** Right-click any message -> Apps -> *Send to Webhook*.
* **Rich Metadata:** Forwards message content, author details (ID, Avatar), channel info (ID, Name, Type), and Guild ID.
* **Action Tracking:** Includes information about which user triggered the action.
* **Docker Ready:** Easily deployable via Docker and Docker Compose.
* **CI/CD Support:** GitHub Actions workflow included for automatic builds to GHCR.

---

### 🛠 Installation & Setup

#### 1. Discord Developer Portal

1. Create a new application at the [Discord Developer Portal](https://www.google.com/search?q=https://discord.com/developers/applications).
2. Navigate to **Bot** and enable the **Message Content Intent**.
3. Reset/Copy your **Bot Token**.
4. Invite the bot using the URL Generator with `application.commands` scope.

#### 2. Environment Variables

The bot requires two environment variables:

* `DISCORD_TOKEN`: Your Discord bot token.
* `WEBHOOK_URL`: The destination URL where the JSON payload will be sent.

#### 3. Deployment with Docker

Use the provided `docker-compose.yml`:

```yaml
services:
  discord-webhook-bot:
    image: ghcr.io/btwonion/DiscordWebhookSender:latest
    environment:
      - DISCORD_TOKEN=your_token_here
      - WEBHOOK_URL=https://your-api-endpoint.com/webhook
    restart: unless-stopped

```

Run the bot:

```bash
docker-compose up -d

```

---

### 📦 Payload Structure

When triggered, the bot sends a `POST` request with the following JSON body:

```json
{
  "content": "Message text here",
  "author": {
    "name": "Username",
    "id": "123456789",
    "avatar": "https://cdn.discordapp.com/..."
  },
  "channel": {
    "name": "general",
    "id": "987654321",
    "type": "text"
  },
  "guild": {
    "id": "1122334455"
  },
  "message_id": "5544332211",
  "timestamp": "2024-01-01T12:00:00Z",
  "triggered_by": {
    "name": "AdminUser",
    "id": 123456789
  }
}

```

---

### 🛠 Development

To run locally without Docker:

1. `pip install discord.py aiohttp`
2. Set your environment variables.
3. `python main.py`

Would you like me to add a **troubleshooting** section to the README for common Docker or Discord permission issues?