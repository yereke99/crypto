from pybit import usdt_perpetual

class Request:
    def __init__(self):
        self.session_unauth = usdt_perpetual.HTTP(endpoint="https://api-testnet.bybit.com").public_trading_records(symbol="BTCUSDT", limit=10)

    def public_trading(self):
        return  self.session_unauth.public_trading_records(
        symbol="BTCUSDT",
        limit=10
    )




if __name__ == "__name__":
    r = Request().session_unauth
    print(r.session_unauth())
    print(r.public_trading())

