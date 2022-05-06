TOKEN = '1368155632:AAH0SsO_0N2l46Rh9hL9PO1uC6HDEIuUkmc'

URL = 'https://api.telegram.org/bot{token}/{method}'

MY_ID = 22177377

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data

UPDATE_METHOD = 'getUpdates'
SEND_METHOD = 'sendMessage'

WEATHER_TOKEN = '3b1c012b8bb96ce447844be352b8189a'

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={token}'
# WEATHER_URL = 'https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&units=metric&exclude=minutely&appid={token}'


LAT = 37.45
LON = 126.70