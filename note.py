from capitalcom.client_demo import Client 
from config import login, password, API_KEY


cl = Client(
    login,
    password,
    API_KEY
)

status = cl.historical_prices(
    'BTCUSD'
)

print(status)

a = ''