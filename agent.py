import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)

class PrintJob:
    """Represents a print job"""
    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
        self.timestamp = datetime.now()
        self.status = 'pending'
        
def process_print_job(message_text, sender_id):
    """
    Process incoming WhatsApp message and queue print job
    Args:
        message_text: Text from WhatsApp message
        sender_id: User ID from WhatsApp
    Returns:
        Response message to send back to user
    """
    
    try:
        logger.info(f'Processing print job from {sender_id}: {message_text}')
        
        # Parse message
        if not message_text or len(message_text.strip()) == 0:
            return 'Please send a message with content to print.'
            
        # Create print job
        print_job = PrintJob(message_text, sender_id)
        logger.info(f'Created print job: {print_job.__dict__}')
        
        # Handle different print commands
        if message_text.lower().startswith('/print'):
            # Extract content after /print command
            content = message_text[6:].strip()
            if not content:
                return 'Usage: /print <your content here>'
            print_job.content = content
            
        elif message_text.lower().startswith('/status'):
            return f'Print job status: {print_job.status}'
            
        elif message_text.lower().startswith('/help'):
            return '''Available commands:
/print <content> - Print the content
/status - Check print status
/help - Show this help message'''
        
        # Queue the print job (simulated)
        logger.info(f'Queuing print job: {print_job.content}')
        print_job.status = 'queued'
        
        # For now, just acknowledge
        return f'✓ Print job received. Content: "{print_job.content[:50]}..." queued for printing.'
        
    except Exception as e:
        logger.error(f'Error processing print job: {e}')
        return f'Error processing request: {str(e)}'

def validate_message(message):
    """Validate incoming message format"""
    if not isinstance(message, str):
        return False
    if len(message) == 0:
        return False
    return True

def format_response(status, content):
    """Format response message"""
    return f'[{status}] {content}'
