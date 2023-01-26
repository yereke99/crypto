class Coin():
    def __init__(self) -> None:
        self.list_of_coins = ["SWEATEUSDT", "GMTUSDT", "BITUSDT", "ETHUSDT", "ATOMUSDT", "APTUSDT"]

    def get_coin(self):
        return self.list_of_coins

if __name__ == "__main__":
    coin = Coin()
    coin.get_coin() 

