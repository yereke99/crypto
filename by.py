from pybit import usdt_perpetual


session_unauth = usdt_perpetual.HTTP(
    endpoint="https://api-testnet.bybit.com"
)


print(session_unauth.query_kline(
    symbol="BTCUSDT",
    interval=1,
    limit=5,
    from_time=1581231260
))

print("\n\n\n\n")

print(type(session_unauth.public_trading_records(
    symbol="BTCUSDT",
    limit=10
)))

print(session_unauth.public_trading_records(
        symbol="BTCUSDT",
        limit=10
))