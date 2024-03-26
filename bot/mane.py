import os

import telebot
from telebot import types
import sqlite3

from bot.data import create_table, insert_data, data
from bot.order_db import create_orders_table, insert_order

bot = telebot.TeleBot('ВАШ КЛЮЧ СЮДА')


def update_database():
    create_table()
    insert_data(data)


if __name__ == "__main__":
    update_database()

# ---------------------------
user_params = {}


# Обработчик команды /order для начала процесса оформления заказа
@bot.message_handler(commands=['order'])
def start_order(message):
    user_params[message.chat.id] = {'order_started': True}  # Устанавливаем флаг начала заказа
    # Разделение строки на две части
    message_part1 = 'Для оформления заказа введите имя'
    bot.send_message(message.chat.id, message_part1)


# Обработчик обычных сообщений для получения данных пользователя
@bot.message_handler(
    func=lambda message: message.chat.id in user_params and user_params[message.chat.id].get('order_started'))
def get_order_data(message):
    chat_id = message.chat.id
    if 'ФИО' not in user_params[chat_id]:
        user_params[chat_id]['ФИО'] = message.text
        bot.send_message(chat_id, 'Укажите адрес доставки')
    elif 'Адрес' not in user_params[chat_id]:
        user_params[chat_id]['Адрес'] = message.text
        bot.send_message(chat_id, 'Оставьте номер телефона')
    elif 'Номер телефона' not in user_params[chat_id]:
        user_params[chat_id]['Номер телефона'] = message.text
        bot.send_message(chat_id, 'Введите артикул товара')
    elif 'Артикул товара' not in user_params[chat_id]:
        user_params[chat_id]['Артикул товара'] = message.text
        confirm_order(chat_id)


# Функция подтверждения заказа с кнопками "Да", "Нет", "Отмена"
def confirm_order(chat_id):
    order_data = user_params[chat_id]  # Получаем данные о заказе из user_params
    order_message = f"Подтвердите заказ:\n\n" \
                    f"Имя получателя: {order_data['ФИО']}\n" \
                    f"Адрес доставки: {order_data['Адрес']}\n" \
                    f"Номер телефона: {order_data['Номер телефона']}\n" \
                    f"Артикул товара: {order_data['Артикул товара']}"

    markup = types.InlineKeyboardMarkup()
    confirm_button = types.InlineKeyboardButton('Да', callback_data='confirm')
    cancel_button = types.InlineKeyboardButton('Нет', callback_data='cancel')
    abort_button = types.InlineKeyboardButton('Отмена', callback_data='abort')
    markup.row(confirm_button, cancel_button, abort_button)

    bot.send_message(chat_id, order_message, reply_markup=markup)


# Обработчик нажатия кнопки подтверждения заказа
@bot.callback_query_handler(
    func=lambda call: call.message.chat.id in user_params and user_params[call.message.chat.id].get('order_started'))
def handle_confirmation(call):
    chat_id = call.message.chat.id
    if call.data == 'confirm':
        save_order(chat_id)
        bot.send_message(chat_id,
                         'Ваш заказ успешно оформлен! В ближайшее время с Вами свяжется оператор для конечного '
                         'подтверждения заказа и уточнения деталей.')
        if chat_id in user_params:  # Проверяем наличие данных о заказе в словаре
            del user_params[chat_id]  # Удаляем данные о заказе после подтверждения
    elif call.data == 'cancel':
        bot.send_message(chat_id,
                         'Для оформления нового заказа воспользуйтесь командой /order')
        if chat_id in user_params:  # Проверяем наличие данных о заказе в словаре
            del user_params[chat_id]  # Удаляем данные о заказе после отмены
    elif call.data == 'abort':
        bot.send_message(chat_id, 'Оформление заказа отменено.')
        if chat_id in user_params:  # Проверяем наличие данных о заказе в словаре
            del user_params[chat_id]  # Удаляем данные о заказе после отмены


# Функция сохранения заказа в базу данных
def save_order(chat_id):
    order_data = user_params[chat_id]  # Получаем данные о заказе из user_params
    full_name = order_data['ФИО']
    address = order_data['Адрес']
    phone_number = order_data['Номер телефона']
    article = order_data['Артикул товара']

    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO orders (chat_id, full_name, address, phone_number, article) 
                      VALUES (?, ?, ?, ?, ?)''', (chat_id, full_name, address, phone_number, article))
    conn.commit()
    conn.close()

    del user_params[chat_id]  # Удаляем данные о заказе после сохранения


# Обработчик нажатия кнопки "Нет"
@bot.callback_query_handler(func=lambda call: call.data == 'cancel')
def handle_cancel(call):
    chat_id = call.message.chat.id
    user_params[chat_id] = {}  # Сбрасываем данные о текущем заказе
    start_order(call.message)  # Начинаем новый заказ


# Обработчик нажатия кнопки "Отмена"
@bot.callback_query_handler(func=lambda call: call.data == 'abort')
def handle_abort(call):
    chat_id = call.message.chat.id
    bot.send_message(chat_id, 'Оформление заказа отменено.')
    del user_params[chat_id]  # Удаляем данные о заказе после отмены


# Функция сохранения заказа в базу данных
def save_order(chat_id):
    order_data = user_params[chat_id]  # Получаем данные о заказе из user_params
    full_name = order_data['ФИО']
    address = order_data['Адрес']
    phone_number = order_data['Номер телефона']
    article = order_data['Артикул товара']

    create_orders_table()  # Создаем таблицу, если ее нет

    insert_order(chat_id, full_name, address, phone_number, article)

    del user_params[chat_id]  # Удаляем данные о заказе после сохранения


# order close------

def get_products_from_db(square, house_type, price_category):
    conn = sqlite3.connect('links.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM links WHERE square = ? AND house_type = ? AND price_category = ? ORDER BY ROWID''',
                   (square, house_type, price_category))
    rows = cursor.fetchall()
    conn.close()
    return rows


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'👋 Здравствуйте, {message.from_user.first_name}. Для начала работы '
                                      f'воспользуйтесь меню.')


@bot.message_handler(commands=['site'])
def site(message):
    bot.send_message(message.chat.id, 'Веб сайт: https://домашний-климат.рф/')


@bot.message_handler(commands=['vkgroup'])
def vkgroup(message):
    bot.send_message(message.chat.id, 'Группа ВК: https://vk.com/domashniy_klimat_simferopol')


@bot.message_handler(commands=['help'])
def sup(message):
    multiline_message = 'Команды бота:\n' \
                        '\n' \
                        '/site - Ссылка на веб сайт\n' \
                        '/help - Помощь\n' \
                        '/work - Подбор\n' \
                        '\n' \
                        '⬇️ Все команды бота находятся в меню (возле поля ввода) 🤖\n'
    bot.send_message(message.chat.id, multiline_message, parse_mode='HTML')


user_params = {}


@bot.message_handler(commands=['selection'])
def work(message):
    user_params[message.chat.id] = {}
    ask_next_param(message.chat.id)


def ask_next_param(chat_id):
    if 'площадь' not in user_params[chat_id]:
        param_name = 'площадь'
    elif 'тип компрессора' not in user_params[chat_id]:
        param_name = 'тип компрессора'
    elif 'ценовой диапозон' not in user_params[chat_id]:
        param_name = 'ценовой диапозон'
    else:
        send_products(chat_id)
        return

    user_params[chat_id]['current_param'] = param_name

    markup = types.InlineKeyboardMarkup()

    if param_name == "площадь":
        values = ["До 18 кв.м.", "До 28 кв.м.", "До 38 кв.м."]
    elif param_name == "тип компрессора":
        values = ["On/Off", "Инвертор"]
    elif param_name == "ценовой диапозон":
        values = ["Бюджет", "Стандарт", "Премиум"]
    else:
        values = []

    buttons = [types.InlineKeyboardButton(text=value, callback_data=f"{param_name}_{value}") for value in values]
    markup.add(*buttons)
    bot.send_message(chat_id, f"Выберите {param_name.lower()}", reply_markup=markup)

    user_params[chat_id]['current_param'] = param_name


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    param_name, param_value = call.data.split("_")
    user_params[chat_id][param_name] = param_value
    ask_next_param(chat_id)


def send_products(chat_id):
    square = user_params[chat_id].get('площадь', '')
    house_type = user_params[chat_id].get('тип компрессора', '')
    price_category = user_params[chat_id].get('ценовой диапозон', '')

    products = get_products_from_db(square, house_type, price_category)[:3]

    for product in products:
        product_card = f"Название: {product[1]}\n\n" \
                       f"Площадь: {product[2]}\n" \
                       f"Тип компрессора: {product[3]}\n" \
                       f"Цена: {product[5]} руб.\n\n" \
                       f"Артикул: {product[6]}"  # Добавлено отображение артикула товара

        markup = types.InlineKeyboardMarkup()
        site_button = types.InlineKeyboardButton("Сайт", url=product[7])
        markup.row(site_button)

        with open(product[0], 'rb') as photo_file:
            bot.send_photo(chat_id, photo=photo_file, caption=product_card, reply_markup=markup)

    # Добавление сообщения после вывода карточек товаров
    bot.send_message(chat_id,
                     "Если вы нашли подходящий товар, то воспользуйтесь командой /order для оформления заказа.")


@bot.message_handler(commands=['sale'])
def send_sale_messages(message):
    sale_messages = [
        {
            'text': 'В нашем магазине регулярно проходят акции! Успейте приобрести кондиционер по выгодной цене!'
        },
        {
            'photo': 'images/sale1.jpg',
            'text': '''Название: Haier HSU-07HTT03/R2
            
Площадь: до 18 кв.м.
Тип компрессора: on/off
Старая цена: 24 700 руб.
Новая цена: 21 500 руб.

Артикул: 1932''',
            'url_button': 'Ссылка',
            'url': 'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=932'
        },
        {
            'photo': 'images/sale2.jpg',
            'text': '''Название: Haier AS12TT4HRA/1U12TL4FRA
            
Площадь: до 38 кв.м.
Тип компрессора: инвертор
Старая цена: 51 000 руб.
Новая цена: 47 100 руб.

Артикул: 1937''',
            'url_button': 'Ссылка',
            'url': 'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=937'
        },
        {
            'photo': 'images/sale3.jpg',
            'text': '''Название: Haier Lightera on/off 24
            
Площадь: до 70 кв.м.
Тип компрессора: on/off
Старая цена: 79 000 руб.
Новая цена: 76 100 руб.

Артикул: 1100''',
            'url_button': 'Ссылка',
            'url': 'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=100'
        },
        {
            'text': 'Если вы нашли подходящий товар, то воспользуйтесь командой /order для оформления заказа.'
        }
    ]

    for idx, sale_message in enumerate(sale_messages, start=1):
        photo_path = sale_message.get('photo')
        text = sale_message.get('text', '')
        url_button = sale_message.get('url_button')
        url = sale_message.get('url')

        message_text = f"{text}"

        markup = types.InlineKeyboardMarkup()
        if url_button and url:
            url_button = types.InlineKeyboardButton(url_button, url=url)
            markup.add(url_button)

        if photo_path and os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo_file:
                bot.send_photo(message.chat.id, photo=photo_file, caption=message_text, reply_markup=markup)
        else:
            bot.send_message(message.chat.id, message_text, reply_markup=markup)


@bot.message_handler(commands=['new'])
def send_sale_messages(message):
    sale_messages = [
        {
            'text': 'Новая партия кондиционеров уже доступна для заказа! Порадуйте себя и своих близких комфортной '
                    'атмосферой дома в любую погоду!'
        },
        {
            'photo': 'images/new1.jpg',
            'text': '''Название: Kentatsu KSGTI35HZRN1/KSRTI35HZRN1
            
Площадь: до 35 кв.м.
Тип компрессора: инвертор
Цена: 40 700 руб.

Артикул: 1995''',
            'url_button': 'Ссылка',
            'url': 'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/index.php?route=product/product&product_id=995'
        },
        {
            'photo': 'images/new2.jpg',
            'text': '''Название: LG PC12SQ.NSJR/PC12SQ.UA3R
            
Площадь: до 38 кв.м.
Тип компрессора: инвертор
Цена: 72 000 руб.

Артикул: 1985''',
            'url_button': 'Ссылка',
            'url': 'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/index.php?route=product/product&product_id=985'
        },
        {
            'photo': 'images/new3.jpg',
            'text': '''Название: AUX ASW-H12A4/FP-R1DI
            
Площадь: до 38 кв.м.
Тип компрессора: инвертор
Цена: 34 800 руб.

Артикул: 1973''',
            'url_button': 'Ссылка',
            'url': 'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/index.php?route=product/product&product_id=973'
        },
        {
            'text': 'Если вы нашли подходящий товар, то воспользуйтесь командой /order для оформления заказа.'
        }
    ]

    for idx, sale_message in enumerate(sale_messages, start=1):
        photo_path = sale_message.get('photo')
        text = sale_message.get('text', '')
        url_button = sale_message.get('url_button')
        url = sale_message.get('url')

        message_text = f"{text}"

        markup = types.InlineKeyboardMarkup()
        if url_button and url:
            url_button = types.InlineKeyboardButton(url_button, url=url)
            markup.add(url_button)

        if photo_path and os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo_file:
                bot.send_photo(message.chat.id, photo=photo_file, caption=message_text, reply_markup=markup)
        else:
            bot.send_message(message.chat.id, message_text, reply_markup=markup)


@bot.message_handler(commands=['best'])
def send_sale_messages(message):
    sale_messages = [
        {
            'text': 'Выбор для тех, кто ценит комфорт! Ознакомьтесь с самыми популярными моделями кондиционеров, '
                    'которые уже стали любимчиками наших клиентов!'
        },
        {
            'photo': 'images/best1.jpg',
            'text': '''Название: Midea MSAG3-07N8C2-I
            
Площадь: до 18 кв.м.
Тип компрессора: инвертор
Цена: 31 500 руб.

Артикул: 1942''',
            'url_button': 'Ссылка',
            'url': 'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/index.php?route=product/product&product_id=942'
        },
        {
            'photo': 'images/best2.jpg',
            'text': '''Название: AUX ASW-H07A4/FP-R1DI
            
Площадь: до 38 кв.м.
Тип компрессора: инвертор
Цена: 29 000 руб.

Артикул: 1971''',
            'url_button': 'Ссылка',
            'url': 'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/index.php?route=product/product&product_id=971'
        },
        {
            'photo': 'images/best3.jpg',
            'text': '''Название:Daichi O2 25AVQS1R/ O2 25FVS1R
            
Площадь: до 28 кв.м.
Тип компрессора: инвертор
Цена: 33 000 руб.

Артикул: 1831''',
            'url_button': 'Ссылка',
            'url': 'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/index.php?route=product/product&product_id=831'
        },
        {
            'text': 'Если Вы нашли подходящий товар, то воспользуйтесь командой /order для оформления заказа.'
        }
    ]

    for idx, sale_message in enumerate(sale_messages, start=1):
        photo_path = sale_message.get('photo')
        text = sale_message.get('text', '')
        url_button = sale_message.get('url_button')
        url = sale_message.get('url')

        message_text = f"{text}"

        markup = types.InlineKeyboardMarkup()
        if url_button and url:
            url_button = types.InlineKeyboardButton(url_button, url=url)
            markup.add(url_button)

        if photo_path and os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo_file:
                bot.send_photo(message.chat.id, photo=photo_file, caption=message_text, reply_markup=markup)
        else:
            bot.send_message(message.chat.id, message_text, reply_markup=markup)


bot.polling(non_stop=True)
