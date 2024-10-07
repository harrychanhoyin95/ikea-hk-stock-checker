import asyncio
import os
from dotenv import load_dotenv
from telegram import Bot

from ikea_stock_checker import check_stock

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def send_telegram_message(message: str):
    """
    Send a message to a specified Telegram chat.

    Args:
        message (str): The message to be sent.

    Returns:
        None
    """
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

async def check_and_notify(url: str):
    """
    Check stock for a given IKEA product URL and send a notification if in stock.

    Args:
        url (str): The IKEA product URL to check.

    Returns:
        None
    """
    try:
        has_stock = check_stock(url)
        if has_stock:
            await send_telegram_message(f"🔥🔥🔥 Good news! The product is in stock: {url} 🔥🔥🔥")
            print(f"Product in stock: {url}")
        else:
            print(f"Product out of stock: {url}")
    except Exception as e:
        print(f"Error checking stock for {url}: {str(e)}")
        await send_telegram_message(
            f"An error occurred while checking the stock for {url}. Please check the logs.")

async def main() -> None:
    """Start the bot."""
    # List of IKEA product URLs to check
    urls = [
        "https://www.ikea.com.hk/zh/products/luminaires/table-lamps/nodmast-art-70575914",
    ]

    for url in urls:
        await check_and_notify(url)

if __name__ == "__main__":
    asyncio.run(main())
