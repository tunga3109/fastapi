from capitalcom.client_demo import *
from config import login, password, API_KEY
import json


cl = Client(
    login,
    password,
    API_KEY
)

status = cl.historical_prices(
    'BTCUSD'
)

prices = json.loads(status)

a = ''