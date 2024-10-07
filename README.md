# IKEA Stock Checker

IKEA Stock Checker is a Python-based tool that automatically checks the availability of IKEA products on the IKEA Hong Kong website. When a product becomes available, it sends a notification via Telegram.

## Features

- Automated stock checking for IKEA Hong Kong products
- Telegram notifications when products are in stock
- Configurable product list
- GitHub Actions integration for scheduled checks

## Requirements

- Python 3.12+
- Chrome browser
- ChromeDriver

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ikea-stock-checker.git
   cd ikea-stock-checker
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables by creating a `.env` file in the project root:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

## Usage

### Local Execution

To run the stock checker locally:

```
python telegram_bot.py
```

### GitHub Actions

The project includes a GitHub Actions workflow (`ikea-stock-checker.yml`) that runs the stock checker every 10 minutes. To use this:

1. Fork this repository
2. Go to your fork's Settings > Secrets and add the following repository secrets:
   - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
   - `TELEGRAM_CHAT_ID`: Your Telegram chat ID
3. Enable GitHub Actions for your fork

## Customization

To check different IKEA products, edit the `urls` list in the `main()` function of `telegram_bot.py`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for personal use only. Please be respectful of IKEA's website and terms of service.
