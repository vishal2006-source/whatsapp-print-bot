from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv
import logging

load_dotenv()

app = Flask(__name__)

# Configuration
PHONE_ID = os.getenv('PHONE_ID')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN', 'mysecret')
MESSAGES_API_URL = f'https://graph.instagram.com/v18.0/{PHONE_ID}/messages'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/webhook', methods=['GET'])
def webhook_verify():
    """Webhook verification endpoint"""
    verify_token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    if verify_token == VERIFY_TOKEN:
        logger.info('Webhook verified')
        return challenge
    return 'Unauthorized', 403

@app.route('/webhook', methods=['POST'])
def webhook_receive():
    """Webhook to receive messages from WhatsApp"""
    data = request.get_json()
    logger.info(f'Received webhook: {data}')
    
    try:
        if data['object'] == 'whatsapp_business_account':
            changes = data['entry'][0]['changes'][0]
            
            if 'messages' in changes['value']:
                message = changes['value']['messages'][0]
                sender_id = message['from']
                message_text = message.get('text', {}).get('body', '')
                
                logger.info(f'Message from {sender_id}: {message_text}')
                
                # Import agent here to handle the message
                from agent import process_print_job
                response = process_print_job(message_text, sender_id)
                
                # Send acknowledgment
                send_message(sender_id, response)
                
        return jsonify({'status': 'ok'}), 200
    except Exception as e:
        logger.error(f'Error processing webhook: {e}')
        return jsonify({'error': str(e)}), 400

def send_message(recipient_id, text):
    """Send message via WhatsApp API"""
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'to': recipient_id,
        'type': 'text',
        'text': {'preview_url': False, 'body': text}
    }
    
    try:
        response = requests.post(MESSAGES_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        logger.info(f'Message sent to {recipient_id}')
    except requests.exceptions.RequestException as e:
        logger.error(f'Failed to send message: {e}')

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)
