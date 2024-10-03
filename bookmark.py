import os

import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="bookmark", description="Create a bookmark request")
async def bookmark(interaction: discord.Interaction):
    # send an ephemeral message to the user
    await interaction.response.send_message("We have received your bookmark request!", ephemeral=True)

    # log the request in the "All Requests" channel
    all_requests_channel = client.get_channel(os.environ['ALL_REQUESTS_CHANNEL_ID'])
    if all_requests_channel:
        await all_requests_channel.send(f"Bookmark request from {interaction.user.mention} in {interaction.channel.mention}")
    else:
        print("Error: 'All Requests' channel not found")

@client.event
async def on_ready():
    await tree.sync()
    print(f"We have logged in as {client.user}")


client.run(os.environ['BOT_TOKEN'])
