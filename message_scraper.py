import discord
import sys
from dotenv import load_dotenv  # This is the correct import
import os
from datetime import datetime
from post_on_x import post_to_x, post_pumpfun_ca
import re



class CustomClient(discord.Client):

    def __init__(self, channel_id, x_client):
        super().__init__()
        self.channel_id = channel_id
        self.x_client = x_client


    async def on_ready(self):
        print(f'Logged in as {self.user}')
        print(f'Monitoring channel {self.channel_id}')


    async def on_message(self, message):
        if message.channel.id == self.channel_id:
            timestamp = message.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            log_entry = f"{timestamp} | {message.author}:{message.content}"

            # # Check if message contains a contract address and post to X
            # if re.search(r'[a-zA-Z0-9]{34,}', message.content):
            #     print("Contract address detected! Posting to X...")
            #     post_pumpfun_ca(message.content, self.x_client)
            if not message.content.startswith('$'):
                print("Message does not start with $. Posting to X...")
                post_pumpfun_ca(message.content, self.x_client)
            else:
                print("Message starts with $. Not posting to X...")

            # post_pumpfun_ca(message.content, self.x_client)

            with open('discord_messages_live.txt', 'a', encoding='utf-8') as f:
                f.write(f"{log_entry}\n")
            
            print(log_entry)
