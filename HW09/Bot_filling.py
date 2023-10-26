import telebot
from adjutant_code import bot_token
import requests
# from bs4 import BeautifulSoup as bs
import fun as f

bot = telebot.TeleBot(bot_token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Здравствуйте, чем вам может помочь ваш личный адъютант?")
    elif message.text == "Как дела?":
        bot.send_message(message.from_user.id, "Потихоньку вывозим, но кукуха уже не справляется... А у вас?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id,
                         "/help - описание доступных команд\n/weather - погода.\n"
                         "Как дела? - моральная поддержка\n")
    elif message.text == "/weather":
        bot.send_message(message.from_user.id, "Укажите город\n(Тула, Москва, Рыбинск, Саранск)\n")
    elif message.text == "Тула" or message.text == "Москва" or message.text == "Рыбинск" or message.text == "Саранск":
        city_name = message.text
        api_key = '3c5e466be166547ac88a15cc126e5235'
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=ru')
        weather_temp = round(float(response.json()['main']['temp']))
        weather_temp_feels = round(float(response.json()['main']['feels_like']))
        degree = ['градус', 'градуса', 'градусов']
        bot.send_message(message.from_user.id,
                         f"В городе {city_name} {weather_temp} {f.declension(abs(weather_temp), degree)}.\n"
                         f"Ощущается как {weather_temp_feels} {f.declension(abs(weather_temp_feels), degree)}.\n")
        bot.send_message(message.from_user.id, "Чем ещё я могу вам помочь?(/help)")
    # elif message.text == "/weatherMoscow":
    #     url = 'https://pogoda.mail.ru/prognoz/moskva/'
    #     response = requests.get(url).text
    #     soup = bs(response, 'html.parser')
    #     temperature = soup.find('div', class_="information__content__temperature").text
    #     fill_temperature = soup.find('div', class_="information__content__additional__item").find('span').text
    #     precipitation = soup.find('div',
    #                               class_="information__content__additional information__content__additional_first")
    #                               .find('div', class_='information__content__additional__item').text
    #     temperature = temperature.replace('\n', '')
    #     temperature = temperature.replace('\t', '')
    #     fill_temperature = fill_temperature.replace('\n', '')
    #     fill_temperature = fill_temperature.replace('\t', '')
    #     precipitation = precipitation.replace('\n', '')
    #     precipitation = precipitation.replace('\t', '')
    #     bot.send_message(message.from_user.id, f'Погода: {temperature}, {fill_temperature}, {precipitation}')
    #     bot.send_message(message.from_user.id, "Чем ещё я могу вам помочь?(/help)")
    else:
        bot.send_message(message.from_user.id, "Чем я могу вам помочь?(/help)")


# @bot.message_handler(commands=['button'])
# def button_message(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton("Кнопка")


# markup.add(item1)

bot.polling(none_stop=True, interval=0)
