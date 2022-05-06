import requests
import json
import const
import time
from pprint import pprint


def answer_user_bot(data):
    data = {
        'chat_id': const.MY_ID,
        'text': data
    }
    url = const.URL.format(
        token=const.TOKEN,
        method=const.SEND_METHOD
    )
    response = requests.post(url, data=data)

def parse_weather_data(data):
    for elem in data['weather']:
        weather_state = elem['main']
    temp = data['main']['temp']
    city = data['name']
    msg = f'Погодка в {city}: температура {temp}, и в небе полно {weather_state}'
    return msg

def get_weather(location):
    url = const.WEATHER_URL.format(
        city=location,
        token=const.WEATHER_TOKEN)
    response = requests.get(url)

    if response.status_code != 200:
        return 'The city is not found'
    data = json.loads(response.content)
    return parse_weather_data(data)

def get_message(data):
    return data['message']['text']

def save_update_id(update):
    with open(const.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
    const.UPDATE_ID = update['update_id']
    return True

def main():
    while True:
        url = const.URL.format(token=const.TOKEN, method=const.UPDATE_METHOD)
        content = requests.get(url).text
        data = json.loads(content)

        """two ways to get the values by the 'result' key from dict"""
        # data.get('result')
        # data['result']    # but this one is less favorable, because it is antipattern

        result = data['result'][::-1]
        needed_part = None

        for elem in result:
            if elem['message']['chat']['id'] == const.MY_ID:
                needed_part = elem
                break

        if const.UPDATE_ID != needed_part['update_id']:
            message = get_message(needed_part)
            msg = get_weather(message)
            answer_user_bot(msg)
            save_update_id(needed_part)

        # pprint(needed_part)
        # pprint(data)
        # break
        time.sleep(5)


if __name__ == '__main__':
    main()


# data = {
#     'chat_id': '22177377,',
#     'text': 'Hello from bot'
# }
#
# url = URL.format(token=TOKEN, method=SEND_METHOD)
# response = requests.post(url, data=data, files=open('a'))
# print(response)
# print(response.text)


# url = URL.format(token=TOKEN, method=UPDATE_METHOD)

# print(url)
# response = requests.get(url)
# print(response)
# # print(dir(response))
# # print(response.status_code)
# # print(response.url)
# print(response.text)
# print(type(response.text))
# # print(response.content)
# # print(response.json)
"""json has following methods: json.dump, json.dumps, json.load, json.loads.
dumps - accept dict and turn into str
loads - accept str and turn into dict
load and dump - use the file descriptor"""
# json_content = json.loads(response.text)
# print(json_content)
# print(type(json_content))
