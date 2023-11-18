import telebot
from telebot import types
# your token
token="6184086339:AAF-9545ABC7Um99YmcAUzorxIeAJ5TgyFM" 
bot=telebot.TeleBot(token)
my_chat_id='yourchatid'
corz_f = []
corz_d = []
corz_p = []
corz_b = []
corz_c = []
corz_n = []
f1 = True
f2 = True
f3 = True
f4 = True
f5 = True
f6 = True
f7 = True
f8 = True
f9 = True
f10 = True
f11 = True
f12 = True
f13 = True
f14 = True
f15 = True
pricem = ['Изначальная стоимость сайта без опций-3000']
priced = ['Цены услуг дизайна:', 'адаптивный дизайн - умножение конечной стоимости сайта на 1,6', 'Добавление страниц сайта - 3000р (на одной странице по умолчанию 9 блоков обычных и один функциональный)', 'Создание дизайна от 3000', 'Темный режим сайта - 4000р', 'Наполнение текстом и картинками - 3000р', ]
pricef = ['Цены услуг функционала:', 'Домен, хостинг - 6000 за пол года', 'Интернет магазин - от 10000', 'Блог - от 8000', 'CMS - от 8000', 'Функциональный блок - от 1000р', 'Seo - 15000', 'Форма обратной связи - 2000р', 'Настройка счетчиков аналитики - 2000р', 'Поддержка после окончания проекта - 2000р в месяц']
pl = []
po = []
def help(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button46 = types.KeyboardButton(text="о нас")
    button47 = types.KeyboardButton(text="услуги")
    button48 = types.KeyboardButton(text="сделать заказ")
    button49 = types.KeyboardButton(text="консультация")
    button55 = types.KeyboardButton(text="цены")
    keyboard.add(button46, button47, button48, button49, button55)
    bot.send_message(message.chat.id,"вы потерялись? Ничего")
    bot.send_message(message.chat.id,"Кнопка -о нас- расскажет вам о нашей компании")
    bot.send_message(message.chat.id,"Кнопка -услуги- расскажет вам о каталоге наших дополнительных услугах")
    bot.send_message(message.chat.id,"Кнопка -консультация- поможет вам с определением вашего заказа")
    bot.send_message(message.chat.id,"Кнопка -заказ- поможет вам оставить заявку")
    bot.send_message(message.chat.id,"Кнопка -цены- поможет вам узнать цены на услуги")


def order_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button5 = types.KeyboardButton(text="назад к меню")
    keyboard.add(button5)
    bot.send_message(message.chat.id,"Хотите сделать заказ?")
    bot.send_message(message.chat.id,"тогда напишите свои данные")

@bot.message_handler(commands=["start"])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="о нас")
    button2 = types.KeyboardButton(text="услуги")
    button3 = types.KeyboardButton(text="сделать заказ")
    button4 = types.KeyboardButton(text="консультация")
    button56 = types.KeyboardButton(text="цены")
    keyboard.add(button1, button2, button3, button4, button56)
    bot.send_message(message.chat.id,'Вас приветствует rgorodov.ru', reply_markup=keyboard)
    bot.send_message(message.chat.id,'как вам помочь?', reply_markup=keyboard)
    
def info_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button5 = types.KeyboardButton(text="назад к меню")
    keyboard.add(button5)
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="переходите и узнайте больше:)", url="https://rgorodov.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id,"ссылка на наш сайт", reply_markup=keyboard)

def cont(message):
     if corz_p == corz_n:
          bot.send_message(message.chat.id, "без прохождения консультации вы не можете сделать заказ")
          start2_message(message)
     else:
          bot.send_message(my_chat_id, f'новая заявка:{message.text}, корзина услуг-{corz_d}, заказ на тему:{corz_c}, {corz_b}, {corz_p}')
          bot.send_message(message.chat.id, "спасибо за заявку! оператор с вами в скорем времени свяжется!")

def start2_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="о нас")
    button2 = types.KeyboardButton(text="услуги")
    button3 = types.KeyboardButton(text="консультация")
    button4 = types.KeyboardButton(text="заказ")
    button55 = types.KeyboardButton(text="цены")
    keyboard.add(button1, button2, button3, button4, button55)
    bot.send_message(message.chat.id,'как вам помочь?', reply_markup=keyboard)

def make(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button5 = types.KeyboardButton(text="назад к меню")
    button6 = types.KeyboardButton(text="дизайн")
    button7 = types.KeyboardButton(text="функционал")
    button30 = types.KeyboardButton(text="корзина")
    keyboard.add(button6, button7, button5, button30)
    bot.send_message(message.chat.id,"выберите раздел", reply_markup=keyboard)

def dis(message):
     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
     button10 = types.KeyboardButton(text="Наполнение текстами и картинками")
     button11 = types.KeyboardButton(text="Адаптивный дизайн")
     button12 = types.KeyboardButton(text="Создание дизайна: Персонального или ультра")
     button13 = types.KeyboardButton(text="Темный режим")
     button23 = types.KeyboardButton(text="Дополнительные страницы")
     button26 = types.KeyboardButton(text="Назад в виды услуг")
     button27 = types.KeyboardButton(text="корзина")
     button28 = types.KeyboardButton(text="clear корзина")
     keyboard.add(button10, button11, button12, button13, button28, button26, button27, button23)
     bot.send_message(message.chat.id,"выберите услугу", reply_markup=keyboard)

def cohs(message):
     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
     button32 = types.KeyboardButton(text="разработка сайта")
     button33 = types.KeyboardButton(text="разарботка тг бота")
     button42 = types.KeyboardButton(text="назад к меню")
     keyboard.add(button33, button32, button42)
     bot.send_message(message.chat.id,"что вас интересует?", reply_markup=keyboard)

def ord(message):
     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
     button34 = types.KeyboardButton(text="одностраничный сайт")
     button35 = types.KeyboardButton(text="многостраничный сайт")
     button43 = types.KeyboardButton(text="назад к выбору разработки")
     keyboard.add(button34, button35, button43)
     bot.send_message(message.chat.id,"какое кол-во страниц на сайте вас интресует?", reply_markup=keyboard)

def ord2(message):
     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
     button36 = types.KeyboardButton(text="меньше 5 блоков на сайте")
     button37 = types.KeyboardButton(text="от 5 до 10 блоков на сайте")
     button38 = types.KeyboardButton(text="от 10 до 15 блоков на сайте")
     button39 = types.KeyboardButton(text="больше 15 блоков на сайте")
     button44 = types.KeyboardButton(text="назад к выбору количества страниц на сайте")
     keyboard.add(button36, button37, button38, button39, button44)
     bot.send_message(message.chat.id,"сколько блоков вас интересует?", reply_markup=keyboard)

def ord3(message):
     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
     button40 = types.KeyboardButton(text="да, интересует")
     button41 = types.KeyboardButton(text="нет, не интересует")
     button41 = types.KeyboardButton(text="очистить начальные услуги")
     button45 = types.KeyboardButton(text="назад к выбору количества блоков на сайте")
     keyboard.add(button40, button41, button45)
     bot.send_message(message.chat.id,"интересуют ли вас доп.услуги?", reply_markup=keyboard)
     
def fyn(message):
     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
     button14 = types.KeyboardButton(text="CMS")
     button15 = types.KeyboardButton(text="SEO оптимизация")
     button16 = types.KeyboardButton(text="Форма обратной связи")
     button17 = types.KeyboardButton(text="Домен и хостинг")
     button18 = types.KeyboardButton(text="Создание функционала Интернет Магазина")
     button19 = types.KeyboardButton(text="Создание функционального блога")
     button20 = types.KeyboardButton(text="Поддержка сайта после окончания проекта")
     button21 = types.KeyboardButton(text="Функциональные блоки")
     button22 = types.KeyboardButton(text="Настройка счетчиков и аналитики")
     button25 = types.KeyboardButton(text="Назад в виды услуг")
     button24 = types.KeyboardButton(text="корзина")
     button31 = types.KeyboardButton(text="clear корзина")
     keyboard.add(button14, button15, button16, button17, button18, button19, button20, button21, button22, button25, button24, button31)
     bot.send_message(message.chat.id,"добавление в корзину функционала", reply_markup=keyboard)
def corz_d1(message):
     corz_d.append(message.text)
     bot.send_message(message.chat.id, f"В корзину добавлено: {message.text}")
def corz_f2(message):
     corz_f.append(message.text)
     bot.send_message(message.chat.id, f"В корзину добавлено: {message.text}")
def all_corz(message):
     bot.send_message(message.chat.id, f"В корзина дизайна:")
     corz_f1 = list(dict.fromkeys(corz_f))
     corz_d1 = list(dict.fromkeys(corz_d))
     for i in corz_d1:
          ff =0
          if i == 'Наполнение текстами и картинками':
               pl.append('3000')
          if i == 'Адаптивный дизайн':
               pl.append('0')
          if i == 'Создание дизайна: Персонального или ультра':
               pl.append('0')
          if i == 'Темный режим':
               pl.append('4000')
          if i == 'Дополнительные страницы':
               pl.append('5000')
          bot.send_message(message.chat.id, i)
     for i in pl:
          ff += int(i)
     bot.send_message(message.chat.id, f' Примерная цена дизайна:{ff}')
     bot.send_message(message.chat.id, f"В корзина функционала:")
     for i in corz_f1:
          bb = 0
          if i == 'Домен и хостинг':
               po.append('6000')
          if i == 'Создание функционала Интернет Магазина':
               po.append('10000')
          if i == 'Функциональные блоки':
               po.append('8000')
          if i == 'CMS':
               po.append('8000')
          if i == 'SEO оптимизация':
               po.append('15000')
          if i == 'Форма обратной связи':
               po.append('2000')
          if i == 'Настройка счетчиков и аналитики':
               po.append('2000')
          if i == 'Создание функционального блога':
               po.append('0')
          if i == 'Поддержка сайта после окончания проекта':
               po.append('2000')
          if i == 'SEO оптимизация':
               po.append('15000')
          bot.send_message(message.chat.id, i)
     for i in po:
          bb += int(i)
     bot.send_message(message.chat.id, f' Примерная функционала:{bb}')
     aa = bb + ff
     bot.send_message(message.chat.id, f' Примерная общяя цена:{aa}')
     
     yn(message)
def clear_corz(message):
     corz_f.clear()
     corz_d.clear()
     bot.send_message(message.chat.id, 'корзина очистена')
def yn(message):
     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
     button50 = types.KeyboardButton(text="ДА, готов сделать заказ")
     button51 = types.KeyboardButton(text="НЕТ, хочу продолжить покупки")
     keyboard.add(button50, button51)
     bot.send_message(message.chat.id,"готовы сделать заказ?", reply_markup=keyboard)
def ready(message):
     cont(message)
     bot.send_message(message.chat.id,"")
def notready(message):
     bot.send_message(message.chat.id,"Продолжайте покупки")
     start2_message(message)
def clear_main(message):
     corz_b.clear()
     corz_c.clear()
     corz_p.clear()
     bot.send_message(message.chat.id, 'корзина очистена')
def pr(message):
     for i in priced:
          bot.send_message(message.chat.id, i)
     for elem in pricef:
          bot.send_message(message.chat.id, elem)


     
@bot.message_handler(content_types=["text"])
def menu_message(message):
     if message.text.lower() == 'о нас':
          info_message(message)
     elif message.text.lower() == 'сделать заказ':
          bot.send_message(message.chat.id, "будем рады вас обслужить! оставьте свои контактные данные:)")
          bot.register_next_step_handler(message,cont)
     elif message.text.lower() == 'услуги':
          make(message)
     elif message.text.lower() == 'заказ':
          bot.send_message(message.chat.id, "будем рады вас обслужить! оставьте свои контактные данные:)")
          bot.register_next_step_handler(message,cont)
     elif message.text.lower() == 'назад к меню':
          start2_message(message)
     elif message.text.lower() == 'дизайн':
          dis(message)
     elif message.text.lower() == 'функционал':
          fyn(message)
     elif message.text.lower() == "наполнение текстами и картинками":
          if f1 ==  True:
               f1 == False
               corz_d1(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'адаптивный дизайн':
          if f2 ==  True:
               f2 == False
               corz_d1(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'создание дизайна: персонального или ультра':
          if f3 ==  True:
               f3 == False
               corz_d1(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'темный режим':
          if f4 ==  True:
               f4 == False
               corz_d1(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'дополнительные страницы':
          if f5 ==  True:
               f5 == False
               corz_d1(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'cms':
          if f6 ==  True:
               f6 == False
               corz_f2(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'seo оптимизация':
          if f7 ==  True:
               f7 == False
               corz_f2(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'форма обратной связи':
          if f8 ==  True:
               f8 == False
               corz_f2(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'домен и хостинг':
          if f9 ==  True:
               f9 == False
               corz_f2(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'создание функционала интернет магазина':
          if f10 ==  True:
               f10 == False
               corz_f2(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'создание функционального блога':
          if f11 ==  True:
               f11 == False
               corz_f2(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'поддержка сайта после окончания проекта':
          if f12 ==  True:
               f12 == False
               corz_f2(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'функциональные блоки':
          if f13 ==  True:
               f13 == False
               corz_f2(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'поддержка сайта после окончания проекта':
          if f14 ==  True:
               f14 == False
               corz_f2(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'настройка счетчиков и аналитики':
          if f15 ==  True:
               f15 == False
               corz_f2(message)
          else:
               bot.send_message(message.chat.id, 'товар уже добавлен')
               dis(message)
     elif message.text.lower() == 'корзина':
          all_corz(message)
     elif message.text.lower() == 'назад в виды услуг':
          make(message)
     elif message.text.lower() == 'clear корзина':
          clear_corz(message)
     elif message.text.lower() == 'консультация':
          cohs(message)
     elif message.text.lower() == 'разработка сайта':
          corz_c.append(message.text)
          ord(message)
     elif message.text.lower() == 'разарботка тг бота':
          corz_c.append(message.text)
          ord(message)
     elif message.text.lower() == 'одностраничный сайт':
          corz_p.append(message.text)
          ord2(message)
     elif message.text.lower() == 'многостраничный сайт':
          corz_p.append(message.text)
          ord2(message)
     elif message.text.lower() == 'меньше 5 блоков на сайте':
          corz_b.append(message.text)
          ord3(message)
     elif message.text.lower() == 'от 5 до 10 блоков на сайте':
          corz_b.append(message.text)
          ord3(message)
     elif message.text.lower() == 'от 10 до 15 блоков на сайте':
          corz_b.append(message.text)
          ord3(message)
     elif message.text.lower() == 'больше 15 блоков на сайте':
          corz_b.append(message.text)
          ord3(message)
     elif message.text.lower() == 'да, интересует':
          make(message)
     elif message.text.lower() == 'нет, не интересует':
          bot.send_message(message.chat.id, "будем рады вас обслужить! оставьте свои контактные данные:)")
          bot.register_next_step_handler(message,cont)
     elif message.text.lower() == 'назад к выбору разработки':
          corz_c.clear()
          cohs(message)
     elif message.text.lower() == 'назад к выбору количества страниц на сайте':
          corz_p.clear()
          ord(message)
     elif message.text.lower() == 'назад к выбору количества блоков на сайте':
          corz_b.clear()
          ord2(message)
     elif message.text.lower() == 'да, интересует':
          make(message)
     elif message.text.lower() == 'да, готов сделать заказ':
          bot.send_message(message.chat.id, "будем рады вас обслужить! оставьте свои контактные данные:)")
          bot.register_next_step_handler(message,cont)
     elif message.text.lower() == 'нет, хочу продолжить покупки':
          notready(message)
     elif message.text.lower() == 'очистить начальные услуги':
          notready(message)
     elif message.text.lower() == 'цены':
          pr(message)
     else:
          help(message)


if __name__=='__main__':
    bot.infinity_polling()

for  i in range(0, 5):
    i += 1
    print('error')

    '''
    bot.send_message(message.chat.id,'Услуги разработки сайтов:', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Дополнительные страницы(по умолчанию одна)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Темный режим(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'CMS(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Функциональные блоки(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Наполнение текстами и картинками(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Настройка счетчиков и аналитики(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'CMS(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'SEO оптимизация(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Адаптивный дизайн(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Форма обратной связи(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Домен и хостинг(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Создание функционала Интернет Магазина(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Создание функционального блога(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Поддержка сайта после окончания проекта(по умолчанию нет)', reply_markup=keyboard)-
    bot.send_message(message.chat.id,'Создание дизайна "Персонального или ультра"(по умолчанию нет)', reply_markup=keyboard)-
    '''
