import telebot
from telebot import types
import psycopg2
import test
import datetime

TOKEN = '5295641600:AAHs_xz0K2rg2m1CJGaB2IxxzSzcBk4-bak' # bot token from @BotFather

bot = telebot.TeleBot(TOKEN)

host = "ec2-52-48-159-67.eu-west-1.compute.amazonaws.com"
user = "joftymmknydozl"
password = "96cfa1884db623762df84d99a74ca419d82e97a750b627780a7bd85404a2ea74"
db_name = "dkhv3tchcev28"

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name

)


# db = mysql.connector.connect(
#     user="root",
#     password="",
#     database="d7qt6q789nm9qq"
# )

cursor = connection.cursor()





# Картинка при команде старт

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # Начальные кнопки

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎥По жанру")
    item2 = types.KeyboardButton("🌏По стране")
    item3 = types.KeyboardButton("📚По книгам")
    item4 = types.KeyboardButton("🌻По настроению")
    item5 = types.KeyboardButton("📆Фильм дня")

    markup.add(item1, item2, item3, item4, item5)

    # Приветствие

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, и я помогу тебе выбрать идеальный фильм для просмотра, но для этого выбери интересующий тебя раздел.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@bot.message_handler(content_types=['text'])
def genre(message):
    # Начальный раздел жанров

    if message.text == '🎥По жанру':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("🌪Катастрофы")
        item2 = types.KeyboardButton("🕺Комедии")
        item3 = types.KeyboardButton("🥷Боевики")
        item4 = types.KeyboardButton("🕴Ужасы")
        item5 = types.KeyboardButton("🐥Мультфильмы")
        item6 = types.KeyboardButton("🧚‍♀️Приключения")
        item7 = types.KeyboardButton("↩Назад")

        markup.add(item1, item2, item3, item4, item5, item6, item7)

        bot.send_message(message.chat.id, 'Выберите интересующий вас жанр:', reply_markup=markup)


    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Раздел жанры катастрофа     
    if message.text == '🌪Катастрофы':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Титаник", callback_data='1.1')
        item2 = types.InlineKeyboardButton("Выжить", callback_data='1.2')
        item3 = types.InlineKeyboardButton("Смерч", callback_data='1.3')
        item4 = types.InlineKeyboardButton("Метро", callback_data='1.4')
        item5 = types.InlineKeyboardButton("Разлом", callback_data='1.5')
        item6 = types.InlineKeyboardButton("Тунель: опасно для жизни", callback_data='1.6')
        item7 = types.InlineKeyboardButton("И грянул шторм", callback_data='1.7')
        item8 = types.InlineKeyboardButton("В изоляции", callback_data='1.8')
        item9 = types.InlineKeyboardButton("Волна", callback_data='1.9')
        item10 = types.InlineKeyboardButton("Черный краб", callback_data='1.10')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм:', reply_markup=markup)

    # Раздел жанры комедии
    if message.text == '🕺Комедии':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Круэлла", callback_data='1.11')
        item2 = types.InlineKeyboardButton("Мальчишник в Вегасе", callback_data='1.12')
        item3 = types.InlineKeyboardButton("Мы - Миллеры", callback_data='1.13')
        item4 = types.InlineKeyboardButton("Третий лишний", callback_data='1.14')
        item5 = types.InlineKeyboardButton("Большой Лебовски", callback_data='1.15')
        item6 = types.InlineKeyboardButton("Впритык", callback_data='1.16')
        item7 = types.InlineKeyboardButton("Стажер", callback_data='1.17')
        item8 = types.InlineKeyboardButton("Майор Пейн", callback_data='1.18')
        item9 = types.InlineKeyboardButton("(НЕ)идеальный мужчина", callback_data='1.19')
        item10 = types.InlineKeyboardButton("Почему он?", callback_data='1.20')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм:', reply_markup=markup)

    # Раздел жанры боевики
    if message.text == '🥷Боевики':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Гнев человеческий", callback_data='1.21')
        item2 = types.InlineKeyboardButton("Леон", callback_data='1.22')
        item3 = types.InlineKeyboardButton("Карты, деньги, два ствола", callback_data='1.23')
        item4 = types.InlineKeyboardButton("Бесславные ублюдки", callback_data='1.24')
        item5 = types.InlineKeyboardButton("Майор Гром: Чумной Доктор", callback_data='1.25')
        item6 = types.InlineKeyboardButton("Джон Уик", callback_data='1.26')
        item7 = types.InlineKeyboardButton("Троя", callback_data='1.27')
        item8 = types.InlineKeyboardButton("Механик", callback_data='1.28')
        item9 = types.InlineKeyboardButton("Стрелок", callback_data='1.29')
        item10 = types.InlineKeyboardButton("Город грехов", callback_data='1.30')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм:', reply_markup=markup)

    # Раздел жанры ужасы
    if message.text == '🕴Ужасы':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Поезд в Пусан", callback_data='1.31')
        item2 = types.InlineKeyboardButton("Война миров Z", callback_data='1.32')
        item3 = types.InlineKeyboardButton("Добро пожаловать в Zомбилэнд", callback_data='1.33')
        item4 = types.InlineKeyboardButton("Заклятие", callback_data='1.34')
        item5 = types.InlineKeyboardButton("28 дней спустя", callback_data='1.35')
        item6 = types.InlineKeyboardButton("Мгла", callback_data='1.36')
        item7 = types.InlineKeyboardButton("Мумия", callback_data='1.37')
        item8 = types.InlineKeyboardButton("Живое", callback_data='1.38')
        item9 = types.InlineKeyboardButton("Дракула", callback_data='1.39')
        item10 = types.InlineKeyboardButton("Хижина в лесу", callback_data='1.40')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм:', reply_markup=markup)

        # Раздел жанры мультфильмы
    if message.text == '🐥Мультфильмы':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Лука", callback_data='1.41')
        item2 = types.InlineKeyboardButton("Моана", callback_data='1.42')
        item3 = types.InlineKeyboardButton("Ходячий замок", callback_data='1.43')
        item4 = types.InlineKeyboardButton("Унесенные призраками", callback_data='1.44')
        item5 = types.InlineKeyboardButton("Король лев", callback_data='1.45')
        item6 = types.InlineKeyboardButton("Зов предков", callback_data='1.46')
        item7 = types.InlineKeyboardButton("Валли", callback_data='1.47')
        item8 = types.InlineKeyboardButton("Корпорация монстров", callback_data='1.48')
        item9 = types.InlineKeyboardButton("Мулан", callback_data='1.49')
        item10 = types.InlineKeyboardButton("Вокруг света за 80 дней", callback_data='1.50')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм:', reply_markup=markup)

        # Раздел жанры приключения    
    if message.text == '🧚‍♀️Приключения':

        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Выживший", callback_data='1.51')
        item2 = types.InlineKeyboardButton("Парк Юрского периода", callback_data='1.52')
        item3 = types.InlineKeyboardButton("Анчартед: На картах не значится", callback_data='1.53')
        item4 = types.InlineKeyboardButton("Кон - тики", callback_data='1.54')
        item5 = types.InlineKeyboardButton("Круиз по джунглям", callback_data='1.55')
        item6 = types.InlineKeyboardButton("Время первых", callback_data='1.56')
        item7 = types.InlineKeyboardButton("Тайны печати дракона", callback_data='1.57')
        item8 = types.InlineKeyboardButton("Восточный ветер", callback_data='1.58')
        item9 = types.InlineKeyboardButton("Эбигейл", callback_data='1.59')
        item10 = types.InlineKeyboardButton("Эспен в королевстве троллей", callback_data='1.60')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм:', reply_markup=markup)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Начальный раздел по стране

    if message.text == '🌏По стране':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("🇧🇻Норвегия")
        item2 = types.KeyboardButton("🇷🇺Россия")
        item3 = types.KeyboardButton("🇬🇧Великобритания")
        item4 = types.KeyboardButton("🇫🇷Франция")
        item5 = types.KeyboardButton("🇺🇸США")
        item6 = types.KeyboardButton("↩Назад")

        markup.add(item1, item2, item3, item4, item5, item6)

        bot.send_message(message.chat.id, 'Выберите интересующую вас страну:', reply_markup=markup)

 

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Раздел по стране - Новервегия     

    if message.text == '🇧🇻Норвегия':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Худший человек на свете", callback_data='2.1')
        item2 = types.InlineKeyboardButton("Тысячу раз «спокойной ночи»", callback_data='2.2')
        item3 = types.InlineKeyboardButton("Охотники за головами", callback_data='2.3')
        item4 = types.InlineKeyboardButton("Король чёртова острова", callback_data='2.4')
        item5 = types.InlineKeyboardButton("Гунда", callback_data='2.5')

        markup.add(item1, item2, item3, item4, item5)

        bot.send_message(message.chat.id, 'Топ-5 фильмов Норвегии:', reply_markup=markup)

    # Раздел по стране - Россия      

    if message.text == '🇷🇺Россия':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Брат", callback_data='2.6')
        item2 = types.InlineKeyboardButton("Дурак", callback_data='2.7')
        item3 = types.InlineKeyboardButton("Легенда №17", callback_data='2.8')
        item4 = types.InlineKeyboardButton("О чём говорят мужчины", callback_data='2.9')
        item5 = types.InlineKeyboardButton("Огонь", callback_data='2.10')

        markup.add(item1, item2, item3, item4, item5)

        bot.send_message(message.chat.id, 'Топ-5 фильмов России:', reply_markup=markup)

    # Раздел по стране - Великобритания      

    if message.text == '🇬🇧Великобритания':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Эмма", callback_data='2.11')
        item2 = types.InlineKeyboardButton("Три секунды", callback_data='2.12')
        item3 = types.InlineKeyboardButton("Гонка века", callback_data='2.13')
        item4 = types.InlineKeyboardButton("Две королевы", callback_data='2.14')
        item5 = types.InlineKeyboardButton("Код «Красный»", callback_data='2.15')

        markup.add(item1, item2, item3, item4, item5)

        bot.send_message(message.chat.id, 'Топ-5 фильмов Великобритании:', reply_markup=markup)

    # Раздел по стране - Франция     

    if message.text == '🇫🇷Франция':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Расправь крылья", callback_data='2.16')
        item2 = types.InlineKeyboardButton("Прекрасная эпоха", callback_data='2.17')
        item3 = types.InlineKeyboardButton("Как прогулять школу с пользой", callback_data='2.18')
        item4 = types.InlineKeyboardButton("Приключения Реми", callback_data='2.19')
        item5 = types.InlineKeyboardButton("Обещание на рассвете", callback_data='2.20')

        markup.add(item1, item2, item3, item4, item5)

        bot.send_message(message.chat.id, 'Топ-5 фильмов Франции:', reply_markup=markup)

    # Раздел по стране - США     

    if message.text == '🇺🇸США':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Побег из Шоушенка", callback_data='2.21')
        item2 = types.InlineKeyboardButton("Начало", callback_data='2.22')
        item3 = types.InlineKeyboardButton("Темный рыцарь", callback_data='2.23')
        item4 = types.InlineKeyboardButton("Зеленая книга", callback_data='2.24')
        item5 = types.InlineKeyboardButton("Волк с Уолл-стрит", callback_data='2.25')

        markup.add(item1, item2, item3, item4, item5)

        bot.send_message(message.chat.id, 'Топ-5 фильмов США:', reply_markup=markup)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Начальный раздел по книгам

    if message.text == '📚По книгам':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Фантастические твари и где они обитают", callback_data='3.1')
        item2 = types.InlineKeyboardButton("Голодные игры", callback_data='3.2')
        item3 = types.InlineKeyboardButton("Марсианин", callback_data='3.3')
        item4 = types.InlineKeyboardButton("Бегущий в лабиринте", callback_data='3.4')
        item5 = types.InlineKeyboardButton("Дивергент", callback_data='3.5')
        item6 = types.InlineKeyboardButton("Сумерки", callback_data='3.6')
        item7 = types.InlineKeyboardButton("День триффидов", callback_data='3.7')
        item8 = types.InlineKeyboardButton("Я – легенда", callback_data='3.8')
        item9 = types.InlineKeyboardButton("Война миров", callback_data='3.9')
        item10 = types.InlineKeyboardButton("Властелин колец", callback_data='3.10')

        markup.add(item1, item2, item3, item4, item5, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм по книге:', reply_markup=markup)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Начальный раздел по настроению

    if message.text == '🌻По настроению':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("😄Веселое")
        item2 = types.KeyboardButton("😭Грустное")
        item3 = types.KeyboardButton("🧐Загадочное")
        item4 = types.KeyboardButton("🤩Мотивирующее")
        item5 = types.KeyboardButton("😍Романтичное")
        item6 = types.KeyboardButton("↩Назад")

        markup.add(item1, item2, item3, item4, item5, item6)

        bot.send_message(message.chat.id, 'Какое у вас настроение:', reply_markup=markup)


    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Раздел по настроению - веселое     

    if message.text == '😄Веселое':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отпуск по обмену", callback_data='4.1')
        item2 = types.InlineKeyboardButton("Маска", callback_data='4.2')
        item3 = types.InlineKeyboardButton("Привет, Джули!", callback_data='4.3')
        item4 = types.InlineKeyboardButton("Мамма миа!", callback_data='4.4')
        item5 = types.InlineKeyboardButton("Октябрьское небо", callback_data='4.5')
        item6 = types.InlineKeyboardButton("Хорошо быть тихоней", callback_data='4.6')
        item7 = types.InlineKeyboardButton("Между небом и землей", callback_data='4.7')
        item8 = types.InlineKeyboardButton("Семья напрокат", callback_data='4.8')
        item9 = types.InlineKeyboardButton("10 причин моей ненависти", callback_data='4.9')
        item10 = types.InlineKeyboardButton("Тайная жизнь пчел", callback_data='4.10')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм:', reply_markup=markup)

        # Раздел по настроению - грустное

    if message.text == '😭Грустное':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Мальчик в полосатой пижаме", callback_data='4.11')
        item2 = types.InlineKeyboardButton("Хорошие дети не плачут", callback_data='4.12')
        item3 = types.InlineKeyboardButton("Дневник памяти", callback_data='4.13')
        item4 = types.InlineKeyboardButton("До встречи с тобой", callback_data='4.14')
        item5 = types.InlineKeyboardButton("В метре друг от друга", callback_data='4.15')
        item6 = types.InlineKeyboardButton("Мост в Терабитию", callback_data='4.16')
        item7 = types.InlineKeyboardButton("Куда приводят мечты", callback_data='4.17')
        item8 = types.InlineKeyboardButton("Виноваты звезды", callback_data='4.18')
        item9 = types.InlineKeyboardButton("Я Кристина", callback_data='4.19')
        item10 = types.InlineKeyboardButton("Класс", callback_data='4.20')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм:', reply_markup=markup)

        # Раздел по настроению - таинственное

    if message.text == '🧐Загадочное':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Другие", callback_data='4.21')
        item2 = types.InlineKeyboardButton("Знакомьтесь, Джо Блэк", callback_data='4.22')
        item3 = types.InlineKeyboardButton("Дориан Грей", callback_data='4.23')
        item4 = types.InlineKeyboardButton("Тело", callback_data='4.24')
        item5 = types.InlineKeyboardButton("Сомния", callback_data='4.25')
        item6 = types.InlineKeyboardButton("Сонная лощина", callback_data='4.26')
        item7 = types.InlineKeyboardButton("Ключ от всех дверей", callback_data='4.27')
        item8 = types.InlineKeyboardButton("Знамение", callback_data='4.28')
        item9 = types.InlineKeyboardButton("Гоголь. Вий", callback_data='4.29')
        item10 = types.InlineKeyboardButton("Приют", callback_data='4.30')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм:', reply_markup=markup)

        # Раздел по настроению - мотивирующее

    if message.text == '🤩Мотивирующее':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Одержимость", callback_data='4.31')
        item2 = types.InlineKeyboardButton("Скрытые фигуры", callback_data='4.32')
        item3 = types.InlineKeyboardButton("Каждое воскресенье", callback_data='4.33')
        item4 = types.InlineKeyboardButton("Не волнуйся, он далеко не уйдет", callback_data='4.34')
        item5 = types.InlineKeyboardButton("В погоне за счастьем", callback_data='4.35')
        item6 = types.InlineKeyboardButton("Человек, который изменил все", callback_data='4.36')
        item7 = types.InlineKeyboardButton("Я — Сэм", callback_data='4.37')
        item8 = types.InlineKeyboardButton("127 часов", callback_data='4.38')
        item9 = types.InlineKeyboardButton("Серфер души", callback_data='4.39')
        item10 = types.InlineKeyboardButton("Спасительный рассвет", callback_data='4.40')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм:', reply_markup=markup)
        
        
            # Раздел по настроению - Романтичное

    if message.text == '😍Романтичное':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("365 дней", callback_data='4.41')
        item2 = types.InlineKeyboardButton("После", callback_data='4.42')
        item3 = types.InlineKeyboardButton("Секретарша", callback_data='4.43')
        item4 = types.InlineKeyboardButton("Будка поцелуев", callback_data='4.44')
        item5 = types.InlineKeyboardButton("Предложение", callback_data='4.45')
        item6 = types.InlineKeyboardButton("Звезда родилась", callback_data='4.46')
        item7 = types.InlineKeyboardButton("Тепло наших тел", callback_data='4.47')
        item8 = types.InlineKeyboardButton("Пятьдесят оттенков серого", callback_data='4.48')
        item9 = types.InlineKeyboardButton("Золушка", callback_data='4.49')
        item10 = types.InlineKeyboardButton("Он - дракон", callback_data='4.50')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        bot.send_message(message.chat.id, 'Выберите интересующий вас фильм:', reply_markup=markup)

    if message.text == "↩Назад":
        welcome(message)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if message.text == '📆Фильм дня':
        postgreSQL_select_query= "SELECT * FROM movie_day"
        cursor.execute(postgreSQL_select_query)
        movie_day_records = cursor.fetchall()
        for movie in movie_day_records:
            today_date = datetime.date.today() # datetime.date(2017, 4, 5)
            if movie[1]==today_date:
                print(movie[2])
                name = movie[2]
                year = movie[3]
                country = movie[4]
                genre = movie[5]
                slogan = movie[6]
                director = movie[7]
                skript = movie[8]
                # photo = movie[9]
                description = movie[10]
                link = movie[11]
                # img = open(photo, 'rb')
                bot.send_message(message.chat.id, f"И фильмом дня становится... *{name}* !!!!!", parse_mode="Markdown") 
                bot.send_message(message.chat.id, f"*Год производства* - {year}\n*Страна* - {country}\n*Жанр* - {genre}\n*Слоган* - {slogan}\n*Режиссер* - {director}\n*Сценарий* - {skript}\n", parse_mode="Markdown")
                # bot.send_photo(message.chat.id, img)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", link)
                markup.add(item1)
                bot.send_message(message.chat.id, f"*Описание*\n        {description}", reply_markup=markup, parse_mode="Markdown")




















# Делает текст жирным
def test_send_message_with_markdown(self):
    tb = telebot.TeleBot(TOKEN)
    markdown = """
        *bold text* _italic text_ [text](URL) """
    ret_msg = tb.send_message(CHAT_ID, markdown, parse_mode="Markdown")
    assert ret_msg.message_id


test.test(bot)

bot.polling(none_stop=True)
