import telebot
from telebot import TeleBot, types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = '6202417152:AAGOP0-Czt7huFKujx082YNOqu7NzMTFflU'
bot = telebot.TeleBot(token)

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


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        if call.data == 'student':
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
            btn1 = types.InlineKeyboardButton("elearning.bseu.by", callback_data="ans_1")
            btn2 = types.InlineKeyboardButton("i.bseu.by", callback_data="ans_2")
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(chat_id=call.message.chat.id, text=f"Какой адрес прописан? в адресной строке?", reply_markup=markup)





bot.polling(none_stop=True, interval=0)