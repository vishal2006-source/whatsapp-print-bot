# WhatsApp Print Bot 🤖📱

Automatically send print jobs via WhatsApp messages. Receive messages on WhatsApp and trigger printing on your local printer or remote system.

## Features ✨

- 📨 **Receive WhatsApp Messages** - Get print requests via WhatsApp
- 🖨️ **Automatic Printing** - Process print jobs automatically
- 💬 **Command Support** - Use `/print`, `/status`, `/help` commands
- ⚡ **Real-time Processing** - Instant message acknowledgment
- 🔐 **Secure** - API key verification with webhooks
- 🚀 **Cloud Ready** - Deploy on Railway, Heroku, or any server
- 🐍 **Python Flask** - Lightweight and extensible

## Quick Setup 🚀

### 1. Clone Repository
```bash
git clone https://github.com/vishal2006-source/whatsapp-print-bot
cd whatsapp-print-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your Meta API credentials
```

### 4. Run Locally
```bash
python app.py
```

## Environment Variables 🔑

```env
PHONE_ID=YOUR_PHONE_ID_HERE
ACCESS_TOKEN=YOUR_ACCESS_TOKEN_HERE
VERIFY_TOKEN=YOUR_VERIFY_TOKEN_HERE
PORT=5000
FLASK_ENV=production
```

## Getting Meta Credentials 📝

1. Go to https://developers.facebook.com/apps/902649778829508
2. Navigate to WhatsApp → Getting Started
3. Create/Add WhatsApp Business Account
4. Get PHONE_ID from account settings
5. Generate ACCESS_TOKEN from App Settings → System Users
6. Create your own VERIFY_TOKEN (any random string)

## Deploy on Railway 🚀

### Step 1: Connect GitHub Repository
1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Choose this repository

### Step 2: Set Environment Variables
1. In Railway Dashboard → Variables
2. Add all environment variables from .env
3. Save and deploy

### Step 3: Get Webhook URL
1. Copy your Railway URL: `https://your-app.railway.app`
2. Webhook URL: `https://your-app.railway.app/webhook`

### Step 4: Configure Meta Webhook
1. Go to Meta Developers console
2. Settings → WhatsApp → Webhook
3. Set Callback URL: `https://your-app.railway.app/webhook`
4. Set Verify Token: (use VERIFY_TOKEN from .env)
5. Subscribe to: messages

## API Endpoints 📡

### GET /webhook
Verifies webhook with Meta servers.

**Parameters:**
- `hub.verify_token` - Must match VERIFY_TOKEN
- `hub.challenge` - Challenge token from Meta

**Response:** Challenge token if verified

### POST /webhook
Receives messages from WhatsApp.

**Body:**
```json
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "changes": [
        {
          "value": {
            "messages": [
              {
                "from": "919663116469",
                "text": {
                  "body": "Print my document"
                }
              }
            ]
          }
        }
      ]
    }
  ]
}
```

### GET /health
Health check endpoint.

**Response:**
```json
{"status": "healthy"}
```

## Usage Examples 💻

### Send a Message to WhatsApp Bot

**Command:** `/print Hello World`
**Response:** `✓ Print job received. Content: "Hello World" queued for printing.`

**Command:** `/status`
**Response:** `Print job status: pending`

**Command:** `/help`
**Response:**
```
Available commands:
/print <content> - Print the content
/status - Check print status
/help - Show this help message
```

## Project Structure 📁

```
whatsapp-print-bot/
├── app.py              # Flask application & webhooks
├── agent.py            # Print job processing logic
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # This file
```

## Developer Info 👤

**Bot Owner Phone:** +919663116469
**GitHub:** https://github.com/vishal2006-source
**Location:** Mandya, Karnataka, India

## License 📄

MIT License - feel free to use and modify!

## Support & Issues 🆘

For issues or feature requests, create an issue on GitHub.

## Future Enhancements 🔮

- [ ] Local printer integration (CUPS/Windows Print)
- [ ] Document upload via WhatsApp
- [ ] Print queue management
- [ ] User authentication
- [ ] Multi-language support
- [ ] Database for print history
- [ ] Mobile app integration

---

**Built with ❤️ using Flask + Meta WhatsApp API**
