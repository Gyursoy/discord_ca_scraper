import tweepy
import os
from dotenv import load_dotenv
import re

load_dotenv()

# X API credentials
api_key = os.getenv('X_API_KEY')
api_secret = os.getenv('X_API_KEY_SECRET')
access_token = os.getenv('X_ACCESS_TOKEN')
access_token_secret = os.getenv('X_ACCESS_TOKEN_SECRET')

# Initialize X client
def initialize_x_client():
    """Initialize and return X client"""
    try:
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        return client
    except Exception as e:
        print(f"Failed to initialize X client: {e}")
        return None

def format_pumpfun_message(content):
    """Format a PumpFun message for X posting"""
    # Extract contract address
    # ca_match = re.search(r'0x[a-fA-F0-9]{40}', content)
    # if not ca_match:
    #     return None
    
    # ca = ca_match.group(0)
    ca = content
    
    # Create formatted message
    message = f"""
        CA: {ca}
"""
    
    return message

def post_pumpfun_ca(content, x_client):
    """Process and post a PumpFun contract address"""
    formatted_message = format_pumpfun_message(content)
    if formatted_message:
        return post_to_x(x_client, formatted_message)
    return False

def post_to_x(client, message):
    try:
        # Post the tweet
        response = client.create_tweet(text=message)
        print(f"Posted to X successfully: {message}")
        return True
    
    except Exception as e:
        print(f"Failed to post to X: {e}")
        return False
