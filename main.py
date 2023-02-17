import requests
import time
import datetime

# Задаем константы
TIMEFRAME = 60 * 60  # 60 минут
CHANGE_THRESHOLD = 0.01  # 1%
API_KEY = 'your_api_key_here'

# Функция для получения актуальной цены
def get_price():
    response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT&apiKey={API_KEY}')
    price = float(response.json()['price'])
    return price

# Функция для проверки изменения цены
def check_price():
    current_price = get_price()
    past_price = get_price()

    # Получаем время для прошлой цены
    past_time = datetime.datetime.now() - datetime.timedelta(seconds=TIMEFRAME)

    # Ждем одну секунду, чтобы получить актуальную цену
    time.sleep(1)

    # Получаем актуальную цену
    current_price = get_price()

    # Если изменение цены более чем на 1%, выводим сообщение в консоль
    price_change = abs(current_price - past_price) / past_price
    if price_change > CHANGE_THRESHOLD:
        print(f'Price has changed by {price_change:.2%} in the last {TIMEFRAME/60} minutes')

# Бесконечный цикл для проверки цены каждые 60 минут
while True:
    check_price()
