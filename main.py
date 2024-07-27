import discord
from discord.ext import tasks
import asyncio
from datetime import datetime

# توکن ربات دیسکورد
DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
CHANNEL_ID = 126681076486135828  # آی‌دی کانال مورد نظر

intents = discord.Intents.default()

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.send_daily_report_task = tasks.loop(hours=24)(self.send_daily_report)

    async def setup_hook(self):
        self.send_daily_report_task.before_loop(self.before_send_daily_report)
        self.send_daily_report_task.start()

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    def get_report_content(self):
        # تابع برای تولید محتوای گزارش
        report_content = "این گزارش روزانه برای " + datetime.now().strftime("%Y-%m-%d")
        return report_content

    async def send_daily_report(self):
        now = datetime.now()
        if now.hour == 8:
            channel = self.get_channel(CHANNEL_ID)
            if channel:
                report_content = self.get_report_content()
                await channel.send(report_content)
            else:
                print(f"Cannot find channel with ID {CHANNEL_ID}")

    async def before_send_daily_report(self):
        await self.wait_until_ready()
        print('Daily report task is starting...')

client = MyClient(intents=intents)

async def main():
    await client.start(DISCORD_TOKEN)

asyncio.run(main())
