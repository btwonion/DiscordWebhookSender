import discord
from discord import app_commands
import aiohttp
import os

BOT_TOKEN = os.getenv('DISCORD_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

class WebhookForwarderBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = WebhookForwarderBot()

@client.tree.context_menu(name='Send to Webhook')
async def send_to_webhook(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.defer(ephemeral=True)

    raw_type = interaction.channel.type
    channel_type = raw_type.name if hasattr(raw_type, 'name') else str(raw_type)

    payload = {
        "content": message.content,
        "author": {
            "name": message.author.display_name,
            "id": str(message.author.id),
            "avatar": str(message.author.display_avatar.url)
        },
        "channel": {
            "name": message.channel.name if hasattr(message.channel, 'name') else "DM",
            "id": str(message.channel.id),
            "type": channel_type
        },
        "guild": {
            "id": str(interaction.guild_id) if interaction.guild_id else "DM"
        },
        "message_id": str(message.id),
        "timestamp": message.created_at.isoformat(),
        "triggered_by": {
            "name": interaction.user.display_name,
            "id": interaction.user.id
        }
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(WEBHOOK_URL, json=payload) as response:
                if response.status in [200, 201]:
                    await interaction.followup.send("🚀 Sent to Webhook successfully!", ephemeral=True)
                else:
                    await interaction.followup.send(f"⚠️ Webhook returned error: {response.status}", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"❌ Connection failed: {e}", ephemeral=True)

if __name__ == "__main__":
    client.run(BOT_TOKEN)