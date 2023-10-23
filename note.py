fake_trades = [
    {"id": 1, "user_id": 1, "currency": "USD", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 2, "currency": "USD", "side": "sell", "price": 125, "amount": 2.12}
]

print(fake_trades[1:][:1])