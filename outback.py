from http import client
import itertools
import discord
import distutils

import asyncio
import random

client = discord.Client()

async def send_message(client, channel, message):
    await client.send_message(channel, message)

async def send_file(client, channel, file):
    await client.send_file(channel, file)

async def send_file_bytes(client, channel, file_bytes):
    await client.send_file(channel, file_bytes)

async def send_file_bytes_async(client, channel, file_bytes):
    await client.send_file(channel, file_bytes)

def get_file_bytes(file):
    with open(file, "rb") as f:
        return f.read()

def get_file_bytes_async(file):
    with open(file, "rb") as f:
        return f.read()
    
async def send_message_async(client, channel, message):
    await client.send_message(channel, message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    await client.change_presence(game=discord.Game(name='with your feelings'))
    
    def read_channel_messages(channel):
        return channel.history(limit=None)
    
    if client.is_logged_in:
        print("Logged in")

    msg_history = read_channel_messages(client.get_channel("CHANNEL_ID"))
    for msg in msg_history:
        if msg == "join":
            await send_message(client, client.get_channel("CHANNEL_ID"), "Hello there!")
            break