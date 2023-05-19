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


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Как стать автором на Хабре?')
        btn2 = types.KeyboardButton('Правила сайта')
        btn3 = types.KeyboardButton('Советы по оформлению публикации')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Как стать автором на Хабре?':
        bot.send_message(message.from_user.id, 'Вы пишете первый пост, его проверяют модераторы, и, если всё хорошо, отправляют в основную ленту Хабра, где он набирает просмотры, комментарии и рейтинг. В дальнейшем премодерация уже не понадобится. Если с постом что-то не так, вас попросят его доработать.\n \nПолный текст можно прочитать по ' + '[ссылке](https://habr.com/ru/sandbox/start/)', parse_mode='Markdown')

    elif message.text == 'Правила сайта':
        bot.send_message(message.from_user.id, 'Прочитать правила сайта вы можете по ' + '[ссылке](https://habr.com/ru/docs/help/rules/)', parse_mode='Markdown')

    elif message.text == 'Советы по оформлению публикации':
        bot.send_message(message.from_user.id, 'Подробно про советы по оформлению публикаций прочитать по ' + '[ссылке](https://habr.com/ru/docs/companies/design/)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)