# Discord Bot

This repository contains a Discord bot implemented using the `discord.py` library. The bot sends a daily report to a specified channel at 8 AM every day.

## Features

- Sends a daily report to a designated Discord channel.
- Scheduled to run at 8 AM every day.

## Prerequisites

- Python 3.8 or higher
- `discord.py` library

## Setup

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```sh
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
## Step 2: Install Dependencies
Install the necessary dependencies using pip:

```sh
pip install discord.py
```

## Step 3: Configure the Bot
Replace YOUR_DISCORD_BOT_TOKEN with your actual Discord bot token in the script. Also, replace CHANNEL_ID with the ID of the channel where you want the bot to send the daily reports.

```python
DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
CHANNEL_ID = 126681076486135828  # Replace with your channel ID
```

## Step 4: Run the Bot
Run the bot using the following command:

```sh
python bot.py
```
---
# Code Overview
## Importing Libraries

```python
import discord
from discord.ext import tasks
import asyncio
from datetime import datetime
```

## Bot Configuration
Set the token and channel ID:

```python
DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
CHANNEL_ID = 126681076486135828  # Replace with your channel ID
```
## Intents
Set the bot's intents:

```python
intents = discord.Intents.default()
```

## Bot Class
Define the bot class with necessary methods:

```python
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
        report_content = "This is the daily report for " + datetime.now().strftime("%Y-%m-%d")
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
```

## Main Function
Run the bot:

```python
client = MyClient(intents=intents)

async def main():
    await client.start(DISCORD_TOKEN)

asyncio.run(main())
```

## Usage
1. Ensure the bot has the necessary permissions to send messages in the specified channel.
2. Run the script.
3. The bot will log in and start sending daily reports at 8 AM.

## Troubleshooting
1. If the bot does not start, ensure your token and channel ID are correct.
2. Make sure the bot has the required permissions to access the channel.
3. Check for any errors in the console and debug accordingly.

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
```sh
```
