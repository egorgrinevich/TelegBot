import telebot
from telebot import TeleBot, types
import csv
from datetime import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = '6202417152:AAGOP0-Czt7huFKujx082YNOqu7NzMTFflU'
bot = telebot.TeleBot(token)
flag: bool = False
@bot.message_handler(commands=['start'])
def start(message):
    #bot.reply_to(message, message.from_user.first_name)
    first_name = message.from_user.first_name
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton("Преподаватель", callback_data="teacher")
    but2 = types.InlineKeyboardButton("Студент", callback_data="student")
    markup.add(but1, but2)
    bot.send_message(message.chat.id, text=f"👋 Здравствуйте,  {first_name} !\nВы подписались на бота БГЭУ!\n"
                                           f"Этот бот предназначен для того, чтобы помочь Вам разобраться с Вашими вопросами!\n"
                                           f"Пожалуйста, укажите свой статус:", reply_markup=markup)
problem: str = ""
status: str = ""

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        if call.data == 'student':
            global problem
            global status
            status = "student"
            #bot.send_message(chat_id=call.message.chat.id, text=f"Опишите, пожалуйста, проблему:", reply_markup=markup)
            markup = types.InlineKeyboardMarkup() #создание новых кнопок
            btn1 = types.InlineKeyboardButton("Не получается войти в систему (неверный логин или пароль)", callback_data="ans_1")
            btn2 = types.InlineKeyboardButton("Я не знаю свои логин и пароль", callback_data="ans_2")
            btn3 = types.InlineKeyboardButton("Я восстановился (перевелся из другого университета)", callback_data="ans_3")
            btn4 = types.InlineKeyboardButton("Я не вижу нужного  электронногогого курса, где бы я выполнял задания и участвовал в видеоконференциях", callback_data="ans_4")
            btn5 = types.InlineKeyboardButton("Я забыл пароль", callback_data="ans_5")
            btn6 = types.InlineKeyboardButton("Моей проблемы нет в списке", callback_data="ans_6")
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn4)
            markup.add(btn5)
            markup.add(btn6)
            bot.send_message(chat_id=call.message.chat.id, text=f"Опишите, пожалуйста, проблему:", reply_markup=markup)
        elif call.data == 'ans_1':
            markup = types.InlineKeyboardMarkup() #resize_keyboard=True)  # создание новых кнопок
            btn1 = types.InlineKeyboardButton("elearning.bseu.by", callback_data="ans_7")
            btn2 = types.InlineKeyboardButton("i.bseu.by", callback_data="ans_8")
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(chat_id=call.message.chat.id, text=f"Какой адрес прописан? в адресной строке?", reply_markup=markup)
        elif call.data == 'ans_7':
            markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
            btn1 = types.InlineKeyboardButton("Да, всё верно", callback_data="ans_9")
            btn2 = types.InlineKeyboardButton("Нет, у меня ошибка...", callback_data="ans_9")
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(chat_id=call.message.chat.id, text=f"Логин и пароль написаны строчными (маленькими) латинскими символами?",
                             reply_markup=markup)
        elif call.data == 'ans_9':
            markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
            btn1 = types.InlineKeyboardButton("Да, спасибо", callback_data="ans_10")
            btn2 = types.InlineKeyboardButton("Нет, я хочу написать администратору", callback_data="ans_11")
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(chat_id=call.message.chat.id, text=f"Вы решили свою проблему?",
                             reply_markup=markup)
        elif call.data == 'ans_10':
            markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
            btn1 = types.InlineKeyboardButton("Начать заново", callback_data="student")
            markup.add(btn1)
            bot.send_message(chat_id=call.message.chat.id, text=f"Всего доброго!",
                             reply_markup=markup)
        elif call.data == 'ans_11':
            markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
            btn1 = types.InlineKeyboardButton("Нет, я еще подумаю", callback_data="student")
            global flag
            flag = True
            markup.add(btn1)
            bot.send_message(chat_id=call.message.chat.id, text=f"Пожалуйста, сообщите Ваши фамилию, имя отчество, а так же шифр группы и введите свой вопрос.",
                             reply_markup=markup)
        elif call.data == 'ans_12':
            data_csv = [status, str(datetime.now()), problem]
            with open('admin_message.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(data_csv)
            markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
            btn1 = types.InlineKeyboardButton("В начало", callback_data="student")
            markup.add(btn1)
            bot.send_message(chat_id=call.message.chat.id,
                             text=f"Всего доброго!\nАдминистратор в ближайшее время свяжется с Вами!!!",
                             reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global flag
    global problem
    if message.text != '' and flag == True:
        problem = message.text
        markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
        btn1 = types.InlineKeyboardButton("Да, всё верно", callback_data="ans_12")
        btn2 = types.InlineKeyboardButton("Нет, хочу исправить", callback_data="ans_11")
        markup.add(btn1, btn2)
        flag = False
        bot.send_message(chat_id=message.chat.id,
                         text=f"Все ли верно введено?\n{problem}", reply_markup=markup)
    else:
        bot.send_message(chat_id=message.chat.id,
                         text=f"Выберите один из предложенных вариантов", reply_markup=markup)


bot.polling(none_stop=True, interval=0)