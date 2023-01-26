from pybit import usdt_perpetual
from config import api_token, api_secret
from coins import Coin

coins = Coin()
class Trader():
    def __init__(self) -> None:
        self.session_unauth = usdt_perpetual.HTTP(endpoint="https://api.bybit.com")

    def get_public_trading(self, coin: str):
        return self.session_unauth.public_trading_records(symbol=coin,limit=10)

    def algo(self):
        for i in coins.get_coin():
            r = self.get_public_trading(i)
            print(r)


if __name__ == "__main__":
    trader = Trader()
    #print(trader.get_public_trading("APTUSDT")['result'][:])
    trader.algo()
