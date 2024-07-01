import robin_stocks.robinhood as rh
import pyotp
from config import USERNAME, PASSWORD, MFA_CODE


def login():
    if MFA_CODE:
        totp = pyotp.TOTP(MFA_CODE).now()
        login = rh.login(USERNAME, PASSWORD, mfa_code=totp)
    else:
        login = rh.login(USERNAME, PASSWORD)
    return login


def get_stock_info(symbol):
    return rh.stocks.get_stock_quote_by_symbol(symbol)


def buy_stock(symbol, quantity):
    return rh.orders.order_buy_market(symbol, quantity)


def sell_stock(symbol, quantity):
    return rh.orders.order_sell_market(symbol, quantity)


def main():
    login()

    while True:
        action = input("Enter action (buy/sell/quote/exit): ").lower()

        if action == 'exit':
            break

        symbol = input("Enter stock symbol: ").upper()

        if action == 'buy':
            quantity = int(input("Enter quantity to buy: "))
            result = buy_stock(symbol, quantity)
            print(f"Buy order result: {result}")
        elif action == 'sell':
            quantity = int(input("Enter quantity to sell: "))
            result = sell_stock(symbol, quantity)
            print(f"Sell order result: {result}")
        elif action == 'quote':
            info = get_stock_info(symbol)
            print(f"Current price of {symbol}: ${info['last_trade_price']}")
        else:
            print("Invalid action. Please try again.")

    rh.logout()


if __name__ == "__main__":
    main()