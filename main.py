import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib import rcParams
from collections import defaultdict, deque
import matplotlib.ticker as ticker
from datetime import datetime
import telebot
from telebot import types
bot = telebot.TeleBot('1822860564:AAE3sSPHpFf48-RnKRZXjDoVHbWbFVzH6UQ')


@bot.message_handler(commands=['start'])
def send_keyboard(message, text="Привет, про какую партию ты хочешь узнать побольше?"):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Единая Россия')
    itembtn2 = types.KeyboardButton('КПРФ')
    itembtn3 = types.KeyboardButton('ЛДПР')
    itembtn4 = types.KeyboardButton('Справедливая Россия')
    itembtn5 = types.KeyboardButton('Больше ничего не интересует')
    keyboard.add(itembtn1, itembtn2)
    keyboard.add(itembtn3, itembtn4)
    keyboard.add(itembtn5)
    # пришлем это все сообщением и запишем выбранный вариант
    bot.send_message(message.from_user.id, text=text, reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_text_messages(mes):
    text = "Что ты хочешь узнать про эту партию?"
    keyboard1 = types.ReplyKeyboardMarkup(row_width=2)  # наша клавиатура
    itembtn1 = types.KeyboardButton('Руководство')  # создадим кнопку
    itembtn2 = types.KeyboardButton('Краткая история')
    itembtn3 = types.KeyboardButton('Направленность программы')
    itembtn4 = types.KeyboardButton('Количество мест в СовФеде и ГосДуме')
    itembtn5 = types.KeyboardButton('Уровень поддержки')
    itembtn6 = types.KeyboardButton('Последняя новость')
    itembtn7 = types.KeyboardButton('Меня интересует другая партия')
    itembtn8 = types.KeyboardButton('Больше ничего не интересует')
    keyboard1.add(itembtn1, itembtn2)
    keyboard1.add(itembtn3, itembtn4)
    keyboard1.add(itembtn5, itembtn6)
    keyboard1.add(itembtn7, itembtn8)
    if mes.text == "Единая Россия":
        edro = 'https://upload.wikimedia.org/wikipedia/ru/thumb/d/d5/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%BF%D0%B0%D1%80%D1%82%D0%B8%D0%B8_%22%D0%95%D0%B4%D0%B8%D0%BD%D0%B0%D1%8F_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%22.svg/486px-%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%BF%D0%B0%D1%80%D1%82%D0%B8%D0%B8_%22%D0%95%D0%B4%D0%B8%D0%BD%D0%B0%D1%8F_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%22.svg.png'
        bot.send_photo(mes.from_user.id, edro)
        msg = bot.send_message(mes.from_user.id, text=text, reply_markup=keyboard1)
        bot.register_next_step_handler(msg, callback_worker1)

    elif mes.text == "КПРФ":
        kprf = 'https://image.jimcdn.com/app/cms/image/transf/dimension=origxorig:format=png/path/s8e05126784e866a2/image/ie3c544c7320c5fb2/version/1281775661/image.png'
        bot.send_photo(mes.from_user.id, kprf)
        msg = bot.send_message(mes.from_user.id, text=text, reply_markup=keyboard1)
        bot.register_next_step_handler(msg, callback_worker2)

    elif mes.text == "ЛДПР":
        ldpr = 'https://upload.wikimedia.org/wikipedia/ru/thumb/5/5e/LDPR_Emblem.svg/1200px-LDPR_Emblem.svg.png'
        bot.send_photo(mes.from_user.id, ldpr)
        msg = bot.send_message(mes.from_user.id, text=text, reply_markup=keyboard1)
        bot.register_next_step_handler(msg, callback_worker3)

    elif mes.text == "Справедливая Россия":
        spros = 'https://spravedlivo.ru/pictbank/051/05147606000600.png'
        bot.send_photo(mes.from_user.id, spros)
        msg = bot.send_message(mes.from_user.id, text=text, reply_markup=keyboard1)
        bot.register_next_step_handler(msg, callback_worker4)
    elif mes.text == 'Больше ничего не интересует':
        bot.send_message(mes.from_user.id, text='Хорошего дня! Если захочешь узнать что-то новое, нажми на команду ' \
                                              '/start')
    else:
        bot.send_message(mes.from_user.id, text='Прости, я не понимаю тебя, попробуй ввести /start')

@bot.message_handler(content_types=['audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact'])
def reaction(mes):
    bot.send_message(mes.from_user.id, text='Прости, но я не понимаю, как это расшифровать. Нажми /start')
# РУКОВОДСТВО
def rulers1(mes):
    url = 'https://er.ru/persons/predsedatel-partii'
    response = requests.get(url)
    tree = BeautifulSoup(response.content, 'html.parser')
    t = tree.find('a', {'class': "link link--several-lines link--theme-dark",
                        'href': "/person/6821ab0a-ab56-484e-847c-f0f4504d07fa"})
    t = t.text
    bot.send_message(mes.from_user.id, text = t)
def rulers2(mes):
    url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BC%D0%BC%D1%83%D0%BD%D0%B8%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%BF%D0%B0%D1%80%D1%82%D0%B8%D1%8F_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8'
    response = requests.get(url)
    tree = BeautifulSoup(response.content, 'html.parser')
    t = tree.find('a', {
        'href': "/wiki/%D0%97%D1%8E%D0%B3%D0%B0%D0%BD%D0%BE%D0%B2,_%D0%93%D0%B5%D0%BD%D0%BD%D0%B0%D0%B4%D0%B8%D0%B9_%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B5%D0%B2%D0%B8%D1%87"})
    t = t.text
    bot.send_message(mes.from_user.id, text = t)
def rulers3(mes):
    url = 'https://ru.wikipedia.org/wiki/%D0%9B%D0%94%D0%9F%D0%A0'
    response = requests.get(url)
    tree = BeautifulSoup(response.content, 'html.parser')
    t = tree.find('a', {
        'href': "/wiki/%D0%96%D0%B8%D1%80%D0%B8%D0%BD%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9,_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%92%D0%BE%D0%BB%D1%8C%D1%84%D0%BE%D0%B2%D0%B8%D1%87"})
    t = t.text
    bot.send_message(mes.from_user.id, text= t)
def rulers4(mes):
    url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%B5%D0%B4%D0%BB%D0%B8%D0%B2%D0%B0%D1%8F_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F_%E2%80%94_%D0%97%D0%B0_%D0%BF%D1%80%D0%B0%D0%B2%D0%B4%D1%83'
    response = requests.get(url)
    tree = BeautifulSoup(response.content, 'html.parser')
    t = tree.find('a', {
        'href': "/wiki/%D0%9C%D0%B8%D1%80%D0%BE%D0%BD%D0%BE%D0%B2,_%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B9_%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D0%B8%D1%87"})
    t = t.text
    bot.send_message(mes.from_user.id, text= t)

# ИСТОРИЯ
def story1(mes):
    text = '"Единая Россия" была образована на базе межрегионального движения "Единство",  а также объединенных ' \
           'общественно-политической организации "Отечество" и движения "Вся Россия", которые прошли на думских ' \
           'выборах в 1999 году. ' + '\n \n' + 'В мае 2000 года "Единство" было преобразовано в партию, \
                                                                                               в которую вошли '\
            'также члены ' \
           'движения  "Наш дом - Россия". Лидером партии стал Сергей Шойгу. ' + '\n \n' + '12 апреля 2001 года ' \
            '"Единство"  и "Отечество" заявили  о намерении создать единую партию "Союз "Единство и Отечество"",  ' \
            'к которой присоединилось движение  "Вся Россия". ' + '\n \n' + '1 декабря 2001 года союз был ' \
                                                                            'преобразован во'\
                                                             'Всероссийскую ' \
           'политическую  партию "Единство и Отечество" - Единая Россия". Современное название носит с 24 декабря ' \
           '2003 года. ' + '\n \n' + '*Источник:*' + ' https://tass.ru/info/7180379'
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")
def story2(mes):
    text = 'Коммунистическая партия РСФСР в составе КПСС была образована в июне 1990 года на конференции российских  ' \
           'коммунистов, преобразованной в I (учредительный) съезд КП РСФСР. В июне‑сентябре 1990 года был ' \
           'сформирован  состав Центрального комитета партии. ' + '\n \n' +'После событий августа 1991 года  ' \
                                                                        'коммунистические  ' \
           'организации на территории России были запрещены. В ноябре 1992 года Конституционный суд России отменил  ' \
           'запрет КП РСФСР. ' + '\n \n' + '13‑14 февраля 1993 года состоялся II чрезвычайный съезд Коммунистической  ' \
                                       'партии РСФСР.  ' \
           'Съезд заявил о возобновлении деятельности партии, которая стала именоваться Коммунистической партией  ' \
           'Российской Федерации. ' + '\n \n' + '*Источник:*'+' https://ria.ru/20130213/922336292.html'
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")
def story3(mes):
    text = 'ЛДПР — старейшая российская партия. Она получила регистрацию в 1992 году и была наследницей ЛДПСС (' \
           'Либерально-демократической партии Советского Союза), основанной в 1989-м Владимиром Жириновским и  ' \
           'Владимиром Богачевым. ' + '\n \n' + 'После распада Советского Союза партия получила нынешнее название —  ' \
           'Либерально-демократическая партия России при преобразовании ЛДПСС на III съезде политической партии (' \
                                                '18—19 апреля 1992 г.) ' \
           + '\n \n' + \
                                                'Исполняя требования принятого в 2001 году Федерального закона  ' \
                                                '«О политических партиях», решением XIII съезда партии  (13 декабря ' \
                                                '2001 г.) ЛДПР реорганизована из общероссийской ' \
                                                'общественно-политической  партии в политическую  партию.' + '\n \n' \
           + '*Источник:*'+' https://www.kommersant.ru/doc/3082418'
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")
def story4(mes):
    text = 'История партии "Справедливая Россия" началась 29 августа 2006 года, когда в пресс-центре еженедельника ' \
           '"Аргументы и факты" было подписано соглашение "Об основных принципах объединения партии "Родина", ' \
           'Российской партии жизни и Российской партии пенсионеров". ' + '\n \n' + 'В течение 2007-2008 годов  к ней ' \
                                                                                'присоединилось ' \
           'еще 8 различных партий. Полным названием партии к 2008 году являлось  "СПРАВЕДЛИВАЯ РОССИЯ:  РОДИНА / ' \
           'ПЕНСИОНЕРЫ / ЖИЗНЬ". ' + '\n \n' + '25 июня 2009 в Москве прошел IV Съезд Политической партии   ' \
                                            '"СПРАВЕДЛИВАЯ РОССИЯ".' \
           'Главными ' \
           'итогами Съезда стали принятие Программы партии, сокращение официального названия до ставших уже ' \
           'привычными для многих россиян слов СПРАВЕДЛИВАЯ РОССИЯ. ' + '\n \n' + '*Источник:*'+' ' \
                                                                               'https://spravedlivo.ru/4774510'
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")

# ГРАФИК ДАННЫХ + РЕЙТИНГ
def rating_1(mes):
    # ГРАФИК ДАННЫХ - ПАРСИНГ
    tables = pd.read_html('https://wciom.ru/ratings/reiting-politicheskikh-partii')
    df = tables[0]
    df = df.rename(columns={'Unnamed: 0': 'Дата'})
    datas = defaultdict(list)
    for i in range(len(df.columns)):
        if i != 0:
            datas[df.columns[0]].append(df.columns[i])
    lst = []
    d = defaultdict(list)
    for i in range(len(df.values)):
        lst.append(list(df.values[i]))
        for j in range(len(lst[0])):
            if j != 0:
                d[lst[i][0]].append(lst[i][j])
    datas.update(d)
    df = pd.DataFrame(datas)

    x = df['Дата']
    a = df[df.columns[1]]
    b = df[df.columns[2]]
    c = df[df.columns[3]]
    d = df[df.columns[4]]
    e = df[df.columns[5]]
    f = df[df.columns[6]]
    g = df[df.columns[7]]
    h = df[df.columns[8]]

    plt.figure(figsize=(10, 7))
    plt.plot(x, a, color='darkblue', lw=2, label=df.columns[1])
    plt.plot(x, b, color='red', lw=2, label=df.columns[2])
    plt.plot(x, c, color='violet', lw=2, label=df.columns[3])
    plt.plot(x, d, color='olive', lw=2, label=df.columns[4])
    plt.plot(x, e, color='green', lw=2, label=df.columns[5])
    plt.plot(x, f, color='black', lw=2, label=df.columns[6])
    plt.plot(x, g, color='c', lw=2, label=df.columns[7])
    plt.plot(x, h, color='brown', lw=2, label=df.columns[8])

    plt.title('Рейтинг политических партий', fontsize=25)
    plt.legend()
    plt.xlabel('Дата', fontsize=15)
    plt.ylabel('Проценты (%)', fontsize=15)
    plt.savefig('Мой график')

    dt_1 = datetime.strptime(df.values[-1][0], '%d.%m.%Y')
    dt_2 = datetime.strptime(df.values[-2][0], '%d.%m.%Y')
    dt_w = str(dt_1 - dt_2)
    diff = round(df.values[-1][1] - df.values[-2][1], 1)
    if diff < 0:
        edro = f"За {dt_w[0]} дней рейтинг партии Единая Россия снизился на {diff}% и на данный момент составляет {df.values[-1][1]}%."
    elif diff == 0:
        edro = f"За {dt_w[0]} дней рейтинг партии Единая Россия не изменился и на данный момент составляет {df.values[-1][1]}%."
    elif diff > 0:
        edro = f"За {dt_w[0]} дней рейтинг партии Единая Россия вырос на {diff}% и на данный момент составляет {df.values[-1][1]}%."

    with open('Мой график.png', 'rb') as f:
        bot.send_photo(mes.from_user.id, f)
    bot.send_message(mes.from_user.id, edro)
def rating_2(mes):
    # ГРАФИК ДАННЫХ - ПАРСИНГ
    tables = pd.read_html('https://wciom.ru/ratings/reiting-politicheskikh-partii')
    df = tables[0]
    df = df.rename(columns={'Unnamed: 0': 'Дата'})
    datas = defaultdict(list)
    for i in range(len(df.columns)):
        if i != 0:
            datas[df.columns[0]].append(df.columns[i])
    lst = []
    d = defaultdict(list)
    for i in range(len(df.values)):
        lst.append(list(df.values[i]))
        for j in range(len(lst[0])):
            if j != 0:
                d[lst[i][0]].append(lst[i][j])
    datas.update(d)
    df = pd.DataFrame(datas)

    x = df['Дата']
    a = df[df.columns[1]]
    b = df[df.columns[2]]
    c = df[df.columns[3]]
    d = df[df.columns[4]]
    e = df[df.columns[5]]
    f = df[df.columns[6]]
    g = df[df.columns[7]]
    h = df[df.columns[8]]

    plt.figure(figsize=(10, 7))
    plt.plot(x, a, color='darkblue', lw=2, label=df.columns[1])
    plt.plot(x, b, color='red', lw=2, label=df.columns[2])
    plt.plot(x, c, color='violet', lw=2, label=df.columns[3])
    plt.plot(x, d, color='olive', lw=2, label=df.columns[4])
    plt.plot(x, e, color='green', lw=2, label=df.columns[5])
    plt.plot(x, f, color='black', lw=2, label=df.columns[6])
    plt.plot(x, g, color='c', lw=2, label=df.columns[7])
    plt.plot(x, h, color='brown', lw=2, label=df.columns[8])

    plt.title('Рейтинг политических партий', fontsize=25)
    plt.legend()
    plt.xlabel('Дата', fontsize=15)
    plt.ylabel('Проценты (%)', fontsize=15)
    plt.savefig('Мой график')

    dt_1 = datetime.strptime(df.values[-1][0], '%d.%m.%Y')
    dt_2 = datetime.strptime(df.values[-2][0], '%d.%m.%Y')
    dt_w = str(dt_1 - dt_2)
    diff = round(df.values[-1][2] - df.values[-2][2], 1)
    if diff < 0:
        kprf = f"За {dt_w[0]} дней рейтинг партии КПРФ снизился на {diff}% и на данный момент составляет {df.values[-1][2]}%."
    elif diff == 0:
        kprf = f"За {dt_w[0]} дней рейтинг партии КПРФ не изменился и на данный момент составляет {df.values[-1][2]}%."
    elif diff > 0:
        kprf = f"За {dt_w[0]} дней рейтинг партии КПРФ вырос на {diff}% и на данный момент составляет {df.values[-1][2]}%."

    with open('Мой график.png', 'rb') as f:
        bot.send_photo(mes.from_user.id, f)
    bot.send_message(mes.from_user.id, kprf)
def rating_3(mes):
    # ГРАФИК ДАННЫХ - ПАРСИНГ
    tables = pd.read_html('https://wciom.ru/ratings/reiting-politicheskikh-partii')
    df = tables[0]
    df = df.rename(columns={'Unnamed: 0': 'Дата'})
    datas = defaultdict(list)
    for i in range(len(df.columns)):
        if i != 0:
            datas[df.columns[0]].append(df.columns[i])
    lst = []
    d = defaultdict(list)
    for i in range(len(df.values)):
        lst.append(list(df.values[i]))
        for j in range(len(lst[0])):
            if j != 0:
                d[lst[i][0]].append(lst[i][j])
    datas.update(d)
    df = pd.DataFrame(datas)

    x = df['Дата']
    a = df[df.columns[1]]
    b = df[df.columns[2]]
    c = df[df.columns[3]]
    d = df[df.columns[4]]
    e = df[df.columns[5]]
    f = df[df.columns[6]]
    g = df[df.columns[7]]
    h = df[df.columns[8]]

    plt.figure(figsize=(10, 7))
    plt.plot(x, a, color='darkblue', lw=2, label=df.columns[1])
    plt.plot(x, b, color='red', lw=2, label=df.columns[2])
    plt.plot(x, c, color='violet', lw=2, label=df.columns[3])
    plt.plot(x, d, color='olive', lw=2, label=df.columns[4])
    plt.plot(x, e, color='green', lw=2, label=df.columns[5])
    plt.plot(x, f, color='black', lw=2, label=df.columns[6])
    plt.plot(x, g, color='c', lw=2, label=df.columns[7])
    plt.plot(x, h, color='brown', lw=2, label=df.columns[8])

    plt.title('Рейтинг политических партий', fontsize=25)
    plt.legend()
    plt.xlabel('Дата', fontsize=15)
    plt.ylabel('Проценты (%)', fontsize=15)
    plt.savefig('Мой график')

    dt_1 = datetime.strptime(df.values[-1][0], '%d.%m.%Y')
    dt_2 = datetime.strptime(df.values[-2][0], '%d.%m.%Y')
    dt_w = str(dt_1 - dt_2)
    diff = round(df.values[-1][3] - df.values[-2][3], 1)
    if diff < 0:
        ldpr = f"За {dt_w[0]} дней рейтинг партии ЛДПР снизился на {diff}% и на данный момент составляет {df.values[-1][3]}%."
    elif diff == 0:
        ldpr = f"За {dt_w[0]} дней рейтинг партии ЛДПР не изменился и на данный момент составляет {df.values[-1][3]}%."
    elif diff > 0:
        ldpr = f"За {dt_w[0]} дней рейтинг партии ЛДПР вырос на {diff}% и на данный момент составляет {df.values[-1][3]}%."

    with open('Мой график.png', 'rb') as f:
        bot.send_photo(mes.from_user.id, f)
    bot.send_message(mes.from_user.id, text=ldpr)
def rating_4(mes):
    # ГРАФИК ДАННЫХ - ПАРСИНГ
    tables = pd.read_html('https://wciom.ru/ratings/reiting-politicheskikh-partii')
    df = tables[0]
    df = df.rename(columns={'Unnamed: 0': 'Дата'})
    datas = defaultdict(list)
    for i in range(len(df.columns)):
        if i != 0:
            datas[df.columns[0]].append(df.columns[i])
    lst = []
    d = defaultdict(list)
    for i in range(len(df.values)):
        lst.append(list(df.values[i]))
        for j in range(len(lst[0])):
            if j != 0:
                d[lst[i][0]].append(lst[i][j])
    datas.update(d)
    df = pd.DataFrame(datas)

    x = df['Дата']
    a = df[df.columns[1]]
    b = df[df.columns[2]]
    c = df[df.columns[3]]
    d = df[df.columns[4]]
    e = df[df.columns[5]]
    f = df[df.columns[6]]
    g = df[df.columns[7]]
    h = df[df.columns[8]]

    plt.figure(figsize=(10, 7))
    plt.plot(x, a, color='darkblue', lw=2, label=df.columns[1])
    plt.plot(x, b, color='red', lw=2, label=df.columns[2])
    plt.plot(x, c, color='violet', lw=2, label=df.columns[3])
    plt.plot(x, d, color='olive', lw=2, label=df.columns[4])
    plt.plot(x, e, color='green', lw=2, label=df.columns[5])
    plt.plot(x, f, color='black', lw=2, label=df.columns[6])
    plt.plot(x, g, color='c', lw=2, label=df.columns[7])
    plt.plot(x, h, color='brown', lw=2, label=df.columns[8])

    plt.title('Рейтинг политических партий', fontsize=25)
    plt.legend()
    plt.xlabel('Дата', fontsize=15)
    plt.ylabel('Проценты (%)', fontsize=15)
    plt.savefig('Мой график')

    dt_1 = datetime.strptime(df.values[-1][0], '%d.%m.%Y')
    dt_2 = datetime.strptime(df.values[-2][0], '%d.%m.%Y')
    dt_w = str(dt_1 - dt_2)
    diff = round(df.values[-1][4] - df.values[-2][4], 1)
    if diff < 0:
        sprav = f"За {dt_w[0]} дней рейтинг партии Справедливая Россия снизился на {diff}% и на данный момент составляет {df.values[-1][4]}%."
    elif diff == 0:
        sprav = f"За {dt_w[0]} дней рейтинг партии Справедливая Россия не изменился и на данный момент составляет {df.values[-1][4]}%."
    elif diff > 0:
        sprav = f"За {dt_w[0]} дней рейтинг партии Справедливая Россия вырос на {diff}% и на данный момент составляет {df.values[-1][4]}%."

    with open('Мой график.png', 'rb') as f:
        bot.send_photo(mes.from_user.id, f)
    bot.send_message(mes.from_user.id,
                     text=sprav + '\n' '\n' '* 22 февраля 2021 года партия «Справедливая Россия» официально провела объединение с партиями «Патриоты России» и «За правду»')

# КОЛИЧЕСТВО МЕСТ
def number1(mes):
    GD = []
    url = 'http://duma.gov.ru/duma/factions/'
    response = requests.get(url)
    tree = BeautifulSoup(response.content, 'html.parser')
    t = tree.find_all('span', {'class': "title--28 title--bold title--last-line"})
    for n in t:
        num = int(n.text)
        GD.append(num)
    t = GD[0]
    vals = [t, 450-t]
    labels = ["Единая Россия", "Оставшиеся места ГД"]
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels)
    ax.axis("equal")
    plt.savefig('Мой график')
    with open('Мой график.png', 'rb') as f:
        bot.send_photo(mes.from_user.id, f)
    tex = f"У Единой России {t} мест в Госдуме из 450. Количество мест в Совете Федерации - 121."
    bot.send_message(mes.from_user.id, text = tex)
def number2(mes):
    GD = []
    url = 'http://duma.gov.ru/duma/factions/'
    response = requests.get(url)
    tree = BeautifulSoup(response.content, 'html.parser')
    t = tree.find_all('span', {'class': "title--28 title--bold title--last-line"})
    for n in t:
        num = int(n.text)
        GD.append(num)
    t = GD[1]
    vals = [t, 450-t]
    labels = ["КПРФ", "Оставшиеся места ГД"]
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels)
    ax.axis("equal")
    plt.savefig('Мой график')
    with open('Мой график.png', 'rb') as f:
        bot.send_photo(mes.from_user.id, f)
    tex = f"У КПРФ {t} мест в Госдуме из 450. Количество мест в Совете Федерации - 2."
    bot.send_message(mes.from_user.id, text = tex)
def number3(mes):
    GD = []
    url = 'http://duma.gov.ru/duma/factions/'
    response = requests.get(url)
    tree = BeautifulSoup(response.content, 'html.parser')
    t = tree.find_all('span', {'class': "title--28 title--bold title--last-line"})
    for n in t:
        num = int(n.text)
        GD.append(num)
    t = GD[2]
    vals = [t, 450-t]
    labels = ["ЛДПР", "Оставшиеся места ГД"]
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels)
    ax.axis("equal")
    plt.savefig('Мой график')
    with open('Мой график.png', 'rb') as f:
        bot.send_photo(mes.from_user.id, f)
    tex = f"У ЛДПР {t} мест в Госдуме из 450. Количество мест в Совете Федерации - 5."
    bot.send_message(mes.from_user.id, text = tex)
def number4(mes):
    GD = []
    url = 'http://duma.gov.ru/duma/factions/'
    response = requests.get(url)
    tree = BeautifulSoup(response.content, 'html.parser')
    t = tree.find_all('span', {'class': "title--28 title--bold title--last-line"})
    for n in t:
        num = int(n.text)
        GD.append(num)
    t = GD[3]
    vals = [t, 450-t]
    labels = ["Справедливая Россия", "Оставшиеся места ГД"]
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels)
    ax.axis("equal")
    plt.savefig('Мой график')
    with open('Мой график.png', 'rb') as f:
        bot.send_photo(mes.from_user.id, f)
    tex = f"У Справедливой России {t} мест в Госдуме из 450. Количество мест в Совете Федерации - 3."
    bot.send_message(mes.from_user.id, text = tex)

# ПРОГРАММЫ
def programm_1(mes):
    text = '*На данный момент предвыборная программа Единой России не была представлена общественности.*' '\n' '\n' \
           'В  скором времени с ней можно будет ознакомиться на сайте https://er.ru/party/program'
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")
def programm_2(mes):
    text = '*Ключевые аспекты программы:*' '\n' ' 1) Установить власть трудящихся, народно-патриотических сил''\n' \
           ' ' \
           '2) Национализировать природные богатства России и стратегические отрасли экономики''\n' ' 3) Ввести ' \
           'государственный контроль над ценами на товары первой необходимости''\n' ' 4) Ввести прогрессивную шкалу ' \
           'налогообложения, освободить от уплаты налогов граждан с низкими доходами''\n' ' 5) Воссоздать сеть ' \
           'общедоступных детских садов' '\n' '\n'  'Ознакомиться с предвыборной программой можно на сайте ' \
           'https://kprf.ru/party/program'
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")
def programm_3(mes):
    text = '*Ключевые аспекты программы:*' '\n' ' 1) Ограничить сроки пребывания у власти губернаторов, чиновников ' \
           'и ' \
           'лидеров  партий десятью годами' '\n' ' 2) Введение государственной монополии на внешнюю торговлю сырьем ' \
           'и энергоносителями, торговлю алкоголем, табаком и сахаром' '\n' ' 3) Ужесточение контроля над финансовым ' \
           'рынком' '\n'  ' 4) Объединении силовых структур' '\n' ' 5) Понизить тарифы в сфере ЖКХ и на ' \
           'общественный транспорт' '\n' '\n'  'Ознакомиться с предвыборной программой можно на сайте ' \
           'https://ldpr.ru/party'
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")
def programm_4(mes):
    text = '*Ключевые аспекты программы:*' '\n' ' 1) Повысить уровень прожиточного минимума и минимальный размер ' \
           'оплаты труда до 31  тысячи рублей' '\n' ' 2) Ввести справедливый базовый доход' '\n'  ' 3) Повысить ' \
           'налоги на вывоз сырья' '\n' ' 4) Разработать "Госплан 2.0"' '\n'  ' 5) Приравнять коррупцию к госизмене' \
           '\n' '\n'  'На данный момент партия предоставила проект предвыборной программы, с ним можно ознакомиться ' \
           'на сайте https://obj.spravedlivo.ru/sr73/112903.pdf'
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")

# НОВОСТЬ
def news1(mes):
    newsi1 = []
    url = 'https://er.ru/'
    response = requests.get(ьurl)y
    tree = BeautifulSoup(response.content, 'html.parser')
    novost = tree.find_all('div', {'class': 'title title__news-item'})
    m = novost[0].a.get('href')
    urlnew = 'https://er.ru' + m
    responew = requests.get(urlnew)
    treenew = BeautifulSoup(responew.content, 'html.parser')
    zag = treenew.find('h1')
    zagi1 = ['*']
    flag = True
    for i in list(str(zag)):
        if i == '<':
            flag = False
        if flag == True:
            zagi1.append(i)
        if i == '>':
            flag = True
    zagi1.append('*')
    zagi1 = ''.join(zagi1)
    novonew = list(treenew.find_all('p'))
    for k in range(len(novonew)):
        s = []
        flag = True
        for i in list(str(novonew[k])):
            if i == '<':
                flag = False
            if flag == True:
                s.append(i)
            if i == '>':
                flag = True
        s = ''.join(s)
        newsi1.append(s)
    newsi1 = "\n \n".join(newsi1)
    istoch1 = '*Источник: *' + urlnew
    if len(newsi1) > 2000:
        newsi1 = newsi1[0:2000] + "..."
        istoch1 = '*Читать продолжение в источнике: *' + urlnew
    text = zagi1 + '\n \n' + newsi1 + '\n \n' + istoch1
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")
def news2(mes):
    newsi2 = []
    url = 'https://kprf.ru/'
    response = requests.get(url)
    tree = BeautifulSoup(response.content, 'html.parser')
    novost = tree.find('div', {'id': 'important_list'})
    new = novost.find('a')
    m = new.get('href')
    urlnew = 'https://kprf.ru' + m
    responew = requests.get(urlnew)
    treenew = BeautifulSoup(responew.content, 'html.parser')
    novonew = list(treenew.find_all('p'))
    zag = treenew.find('h1')
    zagi2 = ['*']
    flag = True
    for i in list(str(zag)):
        if i == '<':
            flag = False
        if flag == True:
            zagi2.append(i)
        if i == '>':
            flag = True
    zagi2.append('*')
    zagi2 = ''.join(zagi2)
    for k in range(len(novonew)):
        s = []
        flag = True
        for i in list(str(novonew[k])):
            if i == '<':
                flag = False
            if flag == True:
                s.append(i)
            if i == '>':
                flag = True
        s = ''.join(s)
        newsi2.append(s)
    newsi2 = "\n \n".join(newsi2)
    istoch2 = '*Источник: *' + urlnew
    if len(newsi2) > 2000:
        newsi2 = newsi2[0:2000] + "..."
        istoch2 = '*Читать продолжение в источнике: *' + urlnew
    text = zagi2 + '\n \n' + newsi2 + '\n \n' + istoch2
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")
def news3(mes):
    newsi3 = []
    url = 'https://ldpr.ru/'
    response = requests.get(url)
    tree = BeautifulSoup(response.content, 'html.parser')
    novost = tree.find_all('a', {'class': ""})
    m = novost[-3].get('href')
    urlnew = 'https://ldpr.ru' + m
    responew = requests.get(urlnew)
    treenew = BeautifulSoup(responew.content, 'html.parser')
    zag = treenew.find('div', {'class': 'e-title text-center small'})
    zagi3 = ['*']
    flag = True
    for i in list(str(zag)):
        if i == '<':
            flag = False
        if flag == True:
            zagi3.append(i)
        if i == '>':
            flag = True
    zagi3.append('*')
    zagi3 = ''.join(zagi3)
    novonew = list(treenew.find_all('p'))
    for k in range(len(novonew)):
        s = []
        flag = True
        for i in list(str(novonew[k])):
            if i == '<':
                flag = False
            if flag == True:
                s.append(i)
            if i == '>':
                flag = True
        s = ''.join(s)
        newsi3.append(s)
    newsi3 = "\n \n".join(newsi3)
    istoch3 = '*Источник: *' + urlnew
    if len(newsi3) > 2000:
        newsi3 = newsi3[0:2000] + "..."
        istoch3 = '*Читать продолжение в источнике: *' + urlnew
    text = zagi3 + '\n \n' + newsi3 + '\n \n' + istoch3
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")
def news4(mes):
    newsi4 = []
    url = 'https://spravedlivo.ru/11101'
    response = requests.get(url)
    tree = BeautifulSoup(response.content, 'html.parser')
    novost = tree.find_all('a', {'class': 'n022_listitem'})
    m = novost[0].get('href')
    urlnew = 'https://spravedlivo.ru/' + str(m)
    responew = requests.get(urlnew)
    treenew = BeautifulSoup(responew.content, 'html.parser')
    novonew = list(treenew.find_all('p'))
    zag = novonew[0]
    novonew = novonew[2: len(novonew)]
    zagi4 = ['*']
    flag = True
    for i in list(str(zag)):
        if i == '<':
            flag = False
        if flag == True:
            zagi4.append(i)
        if i == '>':
            flag = True
    zagi4.append('*')
    zagi4 = ''.join(zagi4)
    for k in range(len(novonew)):
        s = []
        flag = True
        for i in list(str(novonew[k])):
            if i == '<':
                flag = False
            if flag == True:
                s.append(i)
            if i == '>':
                flag = True
        s = ''.join(s)
        newsi4.append(s)
    newsi4 = "\n \n".join(newsi4)
    istoch4 = '*Источник: *' + urlnew
    if len(newsi4) > 2000:
        newsi4 = newsi4[0:2000] + "..."
        istoch4 = '*Читать продолжение в источнике: *' + urlnew
    text = zagi4 + '\n \n' + newsi4 + '\n \n' + istoch4
    bot.send_message(mes.from_user.id, text=text, parse_mode="Markdown")

# КОЛБЭКИ
def callback_worker1(call):  # на каждую партию нужен такой, впишем в конце
    if call.text == 'Руководство':
        rulers1(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker1)
    elif call.text == 'Краткая история':
        story1(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker1)
    elif call.text == 'Направленность программы':
        programm_1(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker1)
    elif call.text == 'Уровень поддержки':
        rating_1(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker1)
    elif call.text == 'Последняя новость':
        news1(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker1)
    elif call.text == 'Количество мест в СовФеде и ГосДуме':
        number1(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker1)
    elif call.text == 'Меня интересует другая партия':
        send_keyboard(call)
    elif call.text == 'Больше ничего не интересует':
        bot.send_message(call.chat.id, text='Хорошего дня!''\n''Если захочешь узнать что-то новое, нажми на команду ' \
                                              '/start')
    else:
        bot.send_message(call.chat.id, text='Прости, я не понимаю тебя, попробуй ввести "/start"')
def callback_worker2(call):  # на каждую партию нужен такой, впишем в конце
    if call.text == 'Руководство':
        rulers2(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker2)
    elif call.text == 'Краткая история':
        story2(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker2)
    elif call.text == 'Направленность программы':
        programm_2(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker2)
    elif call.text == 'Уровень поддержки':
        rating_2(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?' )
        bot.register_next_step_handler(msg, callback_worker2)
    elif call.text == 'Последняя новость':
        news2(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?' )
        bot.register_next_step_handler(msg, callback_worker2)
    elif call.text == 'Количество мест в СовФеде и ГосДуме':
        number2(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker2)
    elif call.text == 'Меня интересует другая партия':
        send_keyboard(call)
    elif call.text == 'Больше ничего не интересует':
        bot.send_message(call.chat.id, text='Хорошего дня! ''\n''Если захочешь узнать что-то новое, нажми на команду ' \
                                              '/start')
    else:
        bot.send_message(call.chat.id, text='Прости, я не понимаю тебя, попробуй ввести "/start"')
def callback_worker3(call):  # на каждую партию нужен такой, впишем в конце
    if call.text == 'Руководство':
        rulers3(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?' )
        bot.register_next_step_handler(msg, callback_worker3)
    elif call.text == 'Краткая история':
        story3(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?' )
        bot.register_next_step_handler(msg, callback_worker3)
    elif call.text == 'Направленность программы':
        programm_3(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?' )
        bot.register_next_step_handler(msg, callback_worker3)
    elif call.text == 'Уровень поддержки':
        rating_3(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?' )
        bot.register_next_step_handler(msg, callback_worker3)
    elif call.text == 'Последняя новость':
        news3(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?' )
        bot.register_next_step_handler(msg, callback_worker3)
    elif call.text == 'Количество мест в СовФеде и ГосДуме':
        number3(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию? ')
        bot.register_next_step_handler(msg, callback_worker3)
    elif call.text == 'Меня интересует другая партия':
        send_keyboard(call)
    elif call.text == 'Больше ничего не интересует':
        bot.send_message(call.chat.id, text='Хорошего дня!''\n''Если захочешь узнать что-то новое, нажми на команду ' \
                                              '/start')
    else:
        bot.send_message(call.chat.id, text='Прости, я не понимаю тебя, попробуй ввести "/start"')
def callback_worker4(call):  # на каждую партию нужен такой, впишем в конце
    if call.text == 'Руководство':
        rulers4(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker4)
    elif call.text == 'Краткая история':
        story4(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker4)
    elif call.text == 'Направленность программы':
        programm_4(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker4)
    elif call.text == 'Уровень поддержки':
        rating_4(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker4)
    elif call.text == 'Последняя новость':
        news4(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker4)
    elif call.text == 'Количество мест в СовФеде и ГосДуме':
        number4(call)
        msg = bot.send_message(call.chat.id,
                               'Что еще хотите узнать про эту партию?')
        bot.register_next_step_handler(msg, callback_worker4)
    elif call.text == 'Меня интересует другая партия':
        send_keyboard(call)
    elif call.text == 'Больше ничего не интересует':
        bot.send_message(call.chat.id, text='Хорошего дня!''\n''Если захочешь узнать что-то новое, нажми на команду ' \
                                              '/start')
    else:
        bot.send_message(call.chat.id, text='Прости, я не понимаю тебя, попробуй ввести "/start"')

bot.polling(none_stop=True)
