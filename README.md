# RobinHoodAPI Trading Bot

A simple stock trading bot using Robinhood's API. Get stock quotes, buy and sell stocks through a command-line interface.

## Features

- User authentication with Robinhood (including MFA support)
- Get real-time stock quotes
- Place market buy orders
- Place market sell orders

## Prerequisites

- Python 3.7+
- Robinhood account

## Installation

1. Clone the repository:
git clone https://github.com/neilpatelll/RobinHoodAPI.git

cd RobinHoodAPI

3. Install required packages:
pip install robin_stocks pyotp

4. Create `config.py` in the project root:
```python
USERNAME = "your_robinhood_username"
PASSWORD = "your_robinhood_password"
MFA_CODE = "your_mfa_code"  # Leave as empty string if not using MFA
```

# Usage
Run the bot:
python trading_bot.py
Follow the prompts to get stock quotes, buy stocks, or sell stocks. Enter 'exit' to quit.

# Security
Never share your config.py file or commit it to version control.
Add config.py to your .gitignore file.
