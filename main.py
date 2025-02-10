import discord
import sys
from dotenv import load_dotenv
import os
from message_scraper import CustomClient
from post_on_x import initialize_x_client

def main():
    # Load environment variables
    load_dotenv()

    # Initialize X
    x_client = initialize_x_client()
    if not x_client:
        print("Failed to initialize X client")
        sys.exit(1)

    # Initialize Discord
    discord_token = os.getenv('DISCORD_TOKEN')
    channel_id = int(os.getenv('CHANNEL_ID'))
    print(channel_id)
    if not discord_token:
        print("Discord token not found in environment variables")
        sys.exit(1)
    
    # Start Discord client
    discord_client = CustomClient(channel_id, x_client)
    try:
        print("Starting Discord monitor...")
        discord_client.run(discord_token)
    except Exception as e:
        print(f"Failed to start Discord client: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()