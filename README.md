# IKEA Stock Checker

This Python script checks the stock availability of a specified IKEA product on the IKEA Hong Kong website using web scraping techniques with Selenium.

## Features

- Checks stock availability of a specified IKEA product
- Uses headless Chrome browser for efficient checking
- Configurable through environment variables
- Suitable for periodic automated checks (e.g., with GitHub Actions)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- pip (Python package installer)
- Chrome browser installed on your system

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/harrychanhoyin95/ikea-stock-checker.git
   cd ikea-stock-checker
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Install ChromeDriver:
   - Download the appropriate version of ChromeDriver for your system from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Ensure the ChromeDriver executable is in your system's PATH.

## Configuration

1. Create a `.env` file in the project root directory with the following content:
   ```
   IKEA_PRODUCT_URL=https://www.ikea.com.hk/zh/products/your-product-url-here
   ```
   Replace `your-product-url-here` with the URL of the IKEA product you want to check.

## Usage

Run the script with the following command:

```
python ikea_stock_checker.py
```

The script will output whether the specified product is in stock or not.

## Running Periodically with GitHub Actions

To run this script periodically using GitHub Actions:

1. Push your code to a GitHub repository.
2. Create a `.github/workflows/stock_check.yml` file in your repository with the content provided in the "GitHub Actions Workflow" section of this README.
3. Set up the `IKEA_PRODUCT_URL` secret in your GitHub repository settings.

## Contributing

Contributions to this project are welcome. Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is for educational purposes only. Please respect IKEA's terms of service and do not perform checks too frequently.
