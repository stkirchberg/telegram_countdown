import logging
import asyncio
from telegram import Bot
from telegram.error import TelegramError
from datetime import datetime

TOKEN = "123456789:AAAbbbCCCdddEEEfffGGG"
CHANNEL_ID = "@testchannel123"
TARGET_DATE = datetime(2025, 6, 14, 18, 0, 0)

bot = Bot(token=TOKEN)

logging.basicConfig(level=logging.INFO)

def format_countdown(time_diff):
    days = time_diff.days
    seconds = time_diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{days} Days, {hours:02d} Hours, {minutes:02d} Minutes"

async def main():
    try:
        now = datetime.now()
        diff = TARGET_DATE - now
        if diff.total_seconds() <= 0:
            await bot.send_message(CHANNEL_ID, "The event is currently taking place or has taken place!")
            return
        
        msg = await bot.send_message(CHANNEL_ID, f"Time to the event:\n{format_countdown(diff)}")
        message_id = msg.message_id

        while True:
            await asyncio.sleep(60)

            now = datetime.now()
            diff = TARGET_DATE - now

            if diff.total_seconds() <= 0:
                await bot.edit_message_text(chat_id=CHANNEL_ID, message_id=message_id,
                                            text="It's now!")
                break
            
            countdown_text = f"Time to the event:\n{format_countdown(diff)}"
            try:
                await bot.edit_message_text(chat_id=CHANNEL_ID, message_id=message_id, text=countdown_text)
            except TelegramError as e:
                logging.error(f"Error updating message: {e}")

    except Exception as e:
        logging.error(f"Error in bot: {e}")

if __name__ == "__main__":
    asyncio.run(main())

