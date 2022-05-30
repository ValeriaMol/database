from telebot import types


def test(bot):
    # книги - фантастические твари (Инлайн кнопки)
    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        try:
#катастрофы - Титаник     
            if call.message:
                if call.data == '1.1':
                    img = open('titanic.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1997\n*Страна* - США, Мексика, Австралия \n*Жанр* - мелодрама, история, триллер, драма\n*Слоган* - «Ничто на Земле не сможет разлучить их»\n*Режиссер* - Джеймс Кэмерон\n*Сценарий* - Джеймс Кэмерон", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://ah.lordfilms-s.tv/44684-film-titanik-1997.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        В первом и последнем плавании шикарного «Титаника» встречаются двое. Пассажир нижней палубы Джек выиграл билет в карты, а богатая наследница Роза отправляется в Америку, чтобы выйти замуж по расчёту. Чувства молодых людей только успевают расцвести, и даже не классовые различия создадут испытания влюблённым, а айсберг, вставший на пути считавшегося непотопляемым лайнера.", reply_markup=markup, parse_mode="Markdown")
                
            # убирает инлайн кнопку
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Титаник*", parse_mode="Markdown")
 
#катастрофы - Выжить  
            if call.message:
                if call.data == '1.2':
                    img = open('alive.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1992\n*Страна* - США, Канада \n*Жанр* - триллер, драма, приключения, история\n*Слоган* - «The triumph of the human spirit»\n*Режиссер* - Фрэнк Маршалл\n*Сценарий* - Джон Патрик Шэнли, Пирс Пол Рид", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://ah.lordfilms-s.tv/33664-film-vyzhit-1992.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Осенью 1972 года в пятницу тринадцатого октября над Андами потерпел катастрофу авиалайнер, на борту которого находилась школьная сборная по регби из Уругвая. Самолет рухнул на высокогорное плато, которое было полностью отрезано от внешнего мира. \n        Здесь, среди дикой стужи и трупов, горстке оставшихся в живых школьников предстоял жестокий, нечеловеческий тест на выживание. Семьдесят два бесконечных, мучительных дня молодые люди боролись за свою жизнь. \n        Убежищем им служили обломки самолета, пищей - тела погибших товарищей. Иногда приходится превратиться в зверя, чтобы остаться человеком...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Выжить*", parse_mode="Markdown")


#катастрофы - Смерч 
            if call.message:
                if call.data == '1.3':
                    img = open('smert.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1996\n*Страна* - США\n*Жанр* - боевик, триллер, приключения\n*Слоган* - «Темная сторона природы»\n*Режиссер* - Ян де Бонт\n*Сценарий* - Майкл Крайтон, Энн-Мари Мартин", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://ah.lordfilms-s.tv/32235-film-smerch-1996.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Рушащиеся, словно карточные домики, здания, разорванные линии электропередач, поднятые в воздух автомобили и животные, гибнущие люди. Мелкими и незначительными оказываются личные неурядицы героев перед лицом разбушевавшейся стихии. Метеорологи вступают в поединок с грозным и малоизученным явлением природы.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Смерч*", parse_mode="Markdown")

#катастрофы - Метро 

            if call.message:
                if call.data == '1.4':
                    img = open('metro.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2012\n*Страна* - Россия\n*Жанр* - триллер, драма\n*Слоган* - «Осторожно! Двери закрываются!»\n*Режиссер* - Антон Мегердичев\n*Сценарий* - Денис Курышев, Виктория Евсеева, Антон Мегердичев", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://l.lordfilm-smotret.one/764-metro-film-2012-24")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Широко развернувшееся в центре Москвы строительство новых зданий приводит к тому, что в одном из тоннелей метро между двумя станциями возникает трещина. Никто себе и представить не мог, что в результате нарушения герметичности перекрытия в тоннель хлынет вода из Москва-реки, и сотни пассажиров поезда окажутся во власти надвигающегося потопа. Бешеный поток воды грозит не только обрушением тоннелей метро, но и разрушением всего города. \n        Среди попавших в беду людей – врач городской больницы Андрей Гарин и его дочь Ксюша. Гарин сражается с катастрофой, пытаясь спасти оставшихся в живых пассажиров, в компании любовника своей жены. Гарину придется побороть обиду, гнев и страх. Он должен выжить, чтобы вернуть свою любовь, семью… свою прежнюю счастливую жизнь.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Метро*", parse_mode="Markdown")

#катастрофы - Разлом 

            if call.message:
                if call.data == '1.5':
                    img = open('razlom.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2018\n*Страна* - Норвегия\n*Жанр* - боевик, триллер, драма\n*Слоган* - «The Wave was only the beginning»\n*Режиссер* - Йон Андреас Андерсен\n*Сценарий* - Юн Коре Роке, Харальд Розенлёв-Эег", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://ah.lordfilms-s.tv/43810-film-razlom-2018.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        В 1904 году норвежская столица пострадала от землетрясения силой 5,4 балла по шкале Рихтера. Стихия привела к разрушениям в городе, но ни один человек не пострадал. В настоящее время геологические исследования показывают, что в Осло почти еженедельно происходят слабые подземные толчки, которые могут служить предвестниками ещё более сильного землетрясения.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Разлом*", parse_mode="Markdown")

#катастрофы - Туннель: Опасно для жизни

            if call.message:
                if call.data == '1.6':
                    img = open('tunel.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2019\n*Страна* - Норвегия\n*Жанр* - триллер, драма\n*Слоган* - «Сотни машин, тысячи людей, один шанс спастись»\n*Режиссер* - Пол Ойе\n*Сценарий* - Хьерсти Расмуссен", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://ah.lordfilms-s.tv/49136-film-tunnel-opasno-dlja-zhizni-2019.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Каждый день въезжая в туннель, думаете ли вы о том, что в нем нет аварийного выхода? Что вы будете делать, если начнется пожар? Сотни машин, тысячи людей оказались в плену между снежной бурей и бушующим пламенем. Им осталось надеяться только на себя.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Туннель: Опасно для жизни*", parse_mode="Markdown")

#катастрофы - И грянул шторм 

            if call.message:
                if call.data == '1.7':
                    img = open('i_granul_shotorm.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2016\n*Страна* - США\n*Жанр* - боевик, триллер, драма, история\n*Слоган* - «32 survivors, room for 12»\n*Режиссер* - Крэйг Гиллеспи\n*Сценарий* - Скотт Сильвер, Пол Тэймеси, Эрик Джонсон", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://ah.lordfilms-s.tv/38651-film-i-grjanul-shtorm-2016.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Сюжет фильма основан на реальных событиях, произошедших в 1952 году, когда сотрудники береговой охраны в самый разгар шторма, используя деревянные моторные лодки, пытались спасти экипаж двух нефтяных танкеров.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*И грянул шторм*", parse_mode="Markdown")

#катастрофы - В изоляции 

            if call.message:
                if call.data == '1.8':
                    img = open('v_izolatii.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2015\n*Страна* - Канада\n*Жанр* - триллер, драма\n*Слоган* - «Hope is power»\n*Режиссер* - Патриция Розема\n*Сценарий* - Патриция Розема, Джин Хегланд", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/10063-film-v-izoljacii-2015.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Недалёкое будущее. Сёстры Нэлл и Эва живут вместе с отцом в умном доме посреди леса. Жизнь людей очень сильно зависит от электричества, поэтому когда случается повсеместное отключение электроэнергии, жизнь человечества в корне меняется. Сначала семья едет в город за продуктами, но потом решает держаться подальше от людей. Им придётся научиться выживать без преимуществ цивилизации.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*В изоляции*", parse_mode="Markdown")

#катастрофы - Волна 

            if call.message:
                if call.data == '1.9':
                    img = open('volna.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2015\n*Страна* - Норвегия, Швеция\n*Жанр* - боевик, триллер, драма\n*Слоган* - «It was only a matter of time»\n*Режиссер* - Роар Утхауг\n*Сценарий* - Юн Коре Роке, Харальд Розенлёв-Эег", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/11158-film-volna-2015.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Сигнал тревоги разносится над спящим городом. То, чего так боялись сейсмологи, сбылось – сильнейший тектонический сдвиг вызывает обрушение горного массива. Теперь гигантское смертоносное цунами движется прямо на людей. Опытный геолог Кристиан Айкорд оказывается в эпицентре самого страшного кошмара своей жизни.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Волна*", parse_mode="Markdown")

#катастрофы - Чёрный краб 

            if call.message:
                if call.data == '1.10':
                    img = open('crab.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2022\n*Страна* - Швеция\n*Жанр* - фантастика, боевик, триллер, драма, приключения\n*Слоган* - «Hope Burns Brightest in The Cold»\n*Режиссер* - Адам Берг\n*Сценарий* - Адам Берг, Пелле Рострём, Йеркер Вирдборг", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://oi.lordfilm.frl/47158-svart-krabba-film-2022.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        В постапокалиптическом мире шесть солдат, выполняющих секретную миссию, должны перевезти особый груз через замерзший архипелаг.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Чёрный краб*", parse_mode="Markdown")
        
        
       
       
        
        
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
        
        
    
    
        
        
        
#Комедии - Круэлла     
            if call.message:
                if call.data == '1.11':
                    img = open('kruela.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2021\n*Страна* - США \n*Жанр* - комедия, криминал, драма\n*Слоган* - «Hello cruel world»\n*Режиссер* - Крэйг Гиллеспи\n*Сценарий* - Дэна Фокс, Тони МакНамара, Алин Брош МакКенна", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://oi.lordfilm.frl/26807-cruella-2021.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Великобритания, 1960-е годы. Эстелла была необычным ребёнком, и особенно трудно ей было мириться со всякого рода несправедливостью. Вылетев из очередной школы, она с мамой отправляется в Лондон. По дороге они заезжают в особняк известной модельерши по имени Баронесса, где в результате ужасного несчастного случая мама погибает. Добравшись до Лондона, Эстелла знакомится с двумя мальчишками — уличными мошенниками Джаспером и Хорасом. \n        10 лет спустя та же компания промышляет на улицах британской столицы мелким воровством, но Эстелла никак не может оставить мечту сделать карьеру в мире моды. Хитростью устроившись в фешенебельный универмаг, девушка привлекает внимание Баронессы, и та берёт её к себе в штат дизайнеров.", reply_markup=markup, parse_mode="Markdown")
                
        # убирает инлайн кнопку
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Круэлла*", parse_mode="Markdown")
 
#Комедии - Мальчишник в Вегасе  
            if call.message:
                if call.data == '1.12':
                    img = open('malchishnic.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2009\n*Страна* - США \n*Жанр* - комедия\n*Слоган* - «Некоторым Вегас просто не по зубам»\n*Режиссер* - Тодд Филлипс\n*Сценарий* - Джон Лукас, Скотт Мур", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://oi.lordfilm.frl/3844-malchishnik-v-vegase-2009.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Они мечтали устроить незабываемый мальчишник в Вегасе. Но теперь им необходимо вспомнить, что именно произошло: что за ребенок сидит в шкафу номера отеля? Как в ванную попал тигр? Почему у одного из них нет зуба? И, самое главное, куда делся жених? То, что парни вытворяли на вечеринке, не идет ни в какое сравнение с тем, что им придется сделать на трезвую голову, когда они будут шаг за шагом восстанавливать события прошлой ночи.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Мальчишник в Вегасе*", parse_mode="Markdown")


#Комедии - Мы - Миллеры 
            if call.message:
                if call.data == '1.13':
                    img = open('milleri.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2013\n*Страна* - США, Великобритания\n*Жанр* - комедия, криминал\n*Слоган* - «Если что, мы - Миллеры»\n*Режиссер* - Роусон Маршалл Тёрбер\n*Сценарий* - Боб Фишер, Стив Фабер, Шон Андерс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://oi.lordfilm.frl/6597-my-millery-2013.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Дэвид Кларк — мелкий торговец наркотиками. Среди его клиентов — повара и скучающие домохозяйки. Детям он наркотики не продаёт и поэтому считает себя принципиальным человеком. Дэвид действительно хорошо относится к детям, но это не остается безнаказанным — он пытается помочь подросткам, попавшим в беду, и на него нападают хулиганы-панки. Они отбирают у него наркотики и деньги, и наш герой оказывается в отчаянном положении. Ведь ему нечем расплатиться с его поставщиком Брэдом. Единственный выход — подрядиться на доставку крупной партии наркотиков через границу…", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Мы - Миллеры*", parse_mode="Markdown")

#Комедии - Третий лишний 

            if call.message:
                if call.data == '1.14':
                    img = open('lishnie.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2012\n*Страна* - США\n*Жанр* - комедия\n*Слоган* - «В любви не без медведя»\n*Режиссер* - Сет МакФарлейн\n*Сценарий* - Сет МакФарлейн, Алек Салкин, Уэллесли Уайлд", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://oi.lordfilm.frl/20865-tretij-lishnij-2012.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Джон влюблен в красавицу Лори. Он работает в прокате автомобилей и имеет большие планы на будущее. Но в их отношения вмешивается третий, давний друг Джона – Тед. Он отрывается сутки напролет, предпочитает случайные связи и не желает терять друга. Но никто на самом деле не знает на что он способен, ведь Тед – большой плюшевый медведь.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Третий лишний*", parse_mode="Markdown")

#Комедии - Большой Лебовски 

            if call.message:
                if call.data == '1.15':
                    img = open('lebovski.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1998\n*Страна* - США, Великобритания\n*Жанр* - комедия, криминал\n*Слоган* - «It takes guys as simple as the Dude and Walter to make a story this complicated... and they'd really rather be bowling»\n*Режиссер* - Джоэл Коэн, Итан Коэн\n*Сценарий* - Итан Коэн, Джоэл Коэн", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://oi.lordfilm.frl/28759-bolshoj-lebovski-1998.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Лос-Анджелес, 1991 год, война в Персидском заливе. Главный герой по прозвищу Чувак считает себя совершенно счастливым человеком. Его жизнь составляют игра в боулинг и выпивка. Но внезапно его счастье нарушается, гангстеры по ошибке принимают его за миллионера-однофамильца, требуют деньги, о которых он ничего не подозревает, и, ко всему прочему, похищают жену миллионера, будучи уверенными, что «муж» выплатит за нее любую сумму.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Большой Лебовски*", parse_mode="Markdown")

#Комедии - Впритык

            if call.message:
                if call.data == '1.16':
                    img = open('vpritik.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2010\n*Страна* - США\n*Жанр* - комедия\n*Слоган* - «Когда всё через...»\n*Режиссер* - Тодд Филлипс\n*Сценарий* - Адам Штикель, Тодд Филлипс, Алан Коэн", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://oi.lordfilm.frl/8265-1-vprityk-2010.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Питер готовится стать отцом и находится на грани нервного срыва. И его нервам не идет на пользу тот факт, что ему предстоит предпринять целое путешествие, да еще и в компании честолюбивого актера, чтобы успеть добраться домой к рождению собственного ребенка.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Впритык*", parse_mode="Markdown")

#Комедии - Стажер 

            if call.message:
                if call.data == '1.17':
                    img = open('stazher.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2015\n*Страна* - США\n*Жанр* - мелодрама, комедия\n*Слоган* - «Опыт всегда в моде»\n*Режиссер* - Нэнси Майерс\n*Сценарий* - Нэнси Майерс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/9501-film-stazher-2015.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        70-летний вдовец Бен Уитакер обнаруживает, что выход на пенсию — еще не конец. Пользуясь случаем, он становится старшим стажером в интернет-магазине модной одежды под руководством Джулс Остин.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Стажер*", parse_mode="Markdown")

#Комедии - Майор Пейн 

            if call.message:
                if call.data == '1.18':
                    img = open('major-pjejn.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1995\n*Страна* - США\n*Жанр* - комедия, приключения\n*Слоган* - «He's looking for a few good men... or a few guys old enough to shave»\n*Режиссер* - Ник Касл\n*Сценарий* - Уильям Робертс, Peter Penduik, Дин Лори", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/4697-film-major-pjejn-1995.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Майору никак не присвоят звание полковника по одной причине - он умеет только убивать, ни на что другое он просто не способен. Его отправляют в отставку. Работа в полиции ему не подходит, и наш герой умирает от скуки в одном из номеров отеля. \n        Неожиданно он получает предложение стать инструктором по военной подготовке в военном учебном заведении. О том, как сложатся отношения «жестокосердного солдафона» с юными подопечными и одной весьма привлекательной преподавательницей рассказывает эта веселая комедия, полная забавных шуток и смешных ситуаций.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Майор Пейн*", parse_mode="Markdown")

#Комедии - (НЕ)идеальный мужчина 

            if call.message:
                if call.data == '1.19':
                    img = open('neidealnyj-muzhchina.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2019\n*Страна* - Россия\n*Жанр* - комедия, фантастика, мелодрама\n*Слоган* - —\n*Режиссер* - Марюс Вайсберг\n*Сценарий* - Евгения Хрипкова, Жора Крыжовников", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/41868-film-neidealnyj-muzhchina-2019.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Свете не везет с отношениями: она вечно подстраивается под парней, унижается и терпит измены. После расставания с очередным непутевым бойфрендом девушка идет работать в компанию по продаже роботов. Те уже стали частью обычной жизни, их не отличить от людей, но не в пример своим создателям роботы чутко реагируют на характер человека, его потребности, привычки и слабости. Когда у одного из роботов обнаруживается программный сбой и его хотят вернуть производителю, Света упрашивает продать его ей, так как… влюбляется в него, приняв технический дефект за проявление личности. Более того, Света хочет связать свою жизнь с чутким, внимательным и заботливым роботом, и это приводит к самым неожиданным последствиям...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*(НЕ)идеальный мужчина*", parse_mode="Markdown")

#Комедии - Почему он? 

            if call.message:
                if call.data == '1.20':
                    img = open('pochemu-on.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2016\n*Страна* - США, Камбоджа\n*Жанр* - комедия\n*Слоган* - «Его дочь могла выбрать любого...»\n*Режиссер* - Джон Гамбург\n*Сценарий* - Джон Гамбург, Йен Хелфер, Джона Хилл", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/12235-film-pochemu-on-2016.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Глава семейства вступает в противостояние с молодым и богатым парнем своей дочери.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Почему он?*", parse_mode="Markdown")
                



       
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------          


        
        
        
        
#Боевики - Гнев человеческий     
            if call.message:
                if call.data == '1.21':
                    img = open('gnev-chelovecheskij.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2021\n*Страна* - Великобритания, США \n*Жанр* - боевик, триллер\n*Слоган* - —\n*Режиссер* - Гай Ричи\n*Сценарий* - Николя Бухриф, Эрик Беснард, Гай Ричи", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/40340-film-gnev-chelovecheskij-2021.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Грузовики лос-анджелесской инкассаторской компании Fortico Security часто подвергаются нападениям, и во время очередного ограбления погибают оба охранника. Через некоторое время в компанию устраивается крепкий немногословный британец Патрик Хилл. Он получает от босса прозвище Эйч и, впритык к необходимому минимуму пройдя тесты по фитнесу, стрельбе и вождению, отправляется на первое задание. Вскоре и его грузовик пытаются ограбить вооруженные налётчики, но Эйч в одиночку расправляется с целой бандой и становится героем. Кажется, слава и уважение коллег его совершенно не интересуют, ведь он преследует свои цели.", reply_markup=markup, parse_mode="Markdown")
                
        # убирает инлайн кнопку
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Гнев человеческий*", parse_mode="Markdown")
 
#Боевики - Леон  
            if call.message:
                if call.data == '1.22':
                    img = open('leon.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1994\n*Страна* - Франция, США \n*Жанр* - боевик, триллер, драма, криминал\n*Слоган* - «Вы не можете остановить того, кого не видно»\n*Режиссер* - Люк Бессон\n*Сценарий* - Люк Бессон", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://go.lordfilmx.biz/23668-leon.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Профессиональный убийца Леон неожиданно для себя самого решает помочь 12-летней соседке Матильде, семью которой убили коррумпированные полицейские.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Леон*", parse_mode="Markdown")


#Боевики - Карты, деньги, два ствола 
            if call.message:
                if call.data == '1.23':
                    img = open('karty-dengi-dva-stvola.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1998\n*Страна* - Великобритания\n*Жанр* - боевик, комедия, криминал\n*Слоган* - «They lost half a million at cards but they've still got a few tricks up their sleeve»\n*Режиссер* - Гай Ричи\n*Сценарий* - Гай Ричи", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://go.lordfilmx.biz/23667-karty-dengi-dva-stvola.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Четверо молодых парней накопили каждый по 25 тысяч фунтов, чтобы один из них мог сыграть в карты с опытным шулером и матерым преступником, известным по кличке Гарри-Топор. Парень в итоге проиграл 500 тысяч, на уплату долга ему дали неделю.\n        В противном случае и ему и его «спонсорам» каждый день будут отрубать по пальцу, а потом... Чтобы выйти из положения, ребята решили ограбить бандитов, решивших ограбить трех «ботаников», выращивающих марихуану для местного наркобарона. Но на этом приключения четверки не заканчиваются...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Карты, деньги, два ствола*", parse_mode="Markdown")

#Боевики - Бесславные ублюдки 

            if call.message:
                if call.data == '1.24':
                    img = open('besslavnye-ubljudki.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2009\n*Страна* - Германия, США\n*Жанр* - боевик, драма, комедия, военный\n*Слоган* - «Они мстят бодро, весело, со вкусом»\n*Режиссер* - Квентин Тарантино\n*Сценарий* - Квентин Тарантино", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/4279-film-besslavnye-ubljudki-2009.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Вторая мировая война, в оккупированной немцами Франции группа американских солдат-евреев наводит страх на нацистов, жестоко убивая и скальпируя солдат.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Бесславные ублюдки*", parse_mode="Markdown")

#Боевики - Майор Гром: Чумной Доктор 

            if call.message:
                if call.data == '1.25':
                    img = open('major-grom-chumnoj-doktor.jpeg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2021\n*Страна* - Россия\n*Жанр* - боевик, криминал, детектив, комедия\n*Слоган* - «Кто твой герой?»\n*Режиссер* - Олег Трофим\n*Сценарий* - Артем Габрелянов, Роман Котков, Евгений Еронин", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/41042-film-major-grom-chumnoj-doktor-2021.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Майор полиции Игорь Гром известен всему Санкт-Петербургу пробивным характером и непримиримой позицией по отношению к преступникам всех мастей. Неимоверная сила, аналитический склад ума и неподкупность — всё это делает майора Грома идеальным полицейским. Но всё резко меняется с появлением человека в маске Чумного Доктора. Заявив, что его город «болен чумой беззакония», он принимается за «лечение», убивая людей, которые в своё время избежали наказания при помощи денег и влияния. Общество взбудоражено. Полиция бессильна. Игорь впервые сталкивается с трудностями в расследовании, от итогов которого может зависеть судьба всего города.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Майор Гром: Чумной Доктор*", parse_mode="Markdown")

#Боевики - Джон Уик

            if call.message:
                if call.data == '1.26':
                    img = open('dzhon-uik.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2014\n*Страна* - США, Китай\n*Жанр* - боевик, триллер, криминал\n*Слоган* - «Его лучше не трогать»\n*Режиссер* - Чад Стахелски, Дэвид Литч\n*Сценарий* - Дерек Колстад", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/10301-film-dzhon-uik-2014.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Джон Уик - на первый взгляд, самый обычный среднестатистический американец, который ведет спокойную мирную жизнь. Однако мало кто знает, что он был наёмным убийцей, причём одним из лучших профессионалов в своём деле.\n        После того как сынок главы бандитской группы со своими приятелями угоняет его любимый «Мустанг» 1969 года выпуска, при этом убив его собаку Дейзи, которая была подарком недавно почившей супруги, Джон вынужден вернуться к своему прошлому. Теперь Уик начинает охоту за теми, кто имел неосторожность перейти ему дорогу, и он готов на всё, чтобы отомстить.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Джон Уик*", parse_mode="Markdown")

#Боевики - Троя 

            if call.message:
                if call.data == '1.27':
                    img = open('troja.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2004\n*Страна* - США, Мальта, Великобритания\n*Жанр* - боевик, история, драма, мелодрама\n*Слоган* - «For Troy»\n*Режиссер* - Вольфганг Петерсен\n*Сценарий* - Дэвид Бениофф, Гомер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/3348-film-troja-2004.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        1193 год до нашей эры. Парис украл прекрасную Елену, жену царя Спарты Менелая. За честь Менелая вступается его брат – царь Агамемнон. Его армия под предводительством Ахиллеса подошла к Трое и взяла город в кровавую осаду, длившуюся долгих десять лет… Два мира будут воевать за честь и власть. Тысячи умрут за славу. И за любовь нация сгорит дотла.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Троя*", parse_mode="Markdown")

#Боевики - Механик 

            if call.message:
                if call.data == '1.28':
                    img = open('mehanik.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2010\n*Страна* - США\n*Жанр* - боевик, триллер, криминал\n*Слоган* - «Someone has to fix the problems»\n*Режиссер* - Саймон Уэст\n*Сценарий* - Льюис Джон Карлино, Ричард Уэнк", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://oi.lordfilm.frl/20114-mehanik-2010.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Артур Бишоп - Механик, высокопрофессиональный безукоризненный киллер, который всегда работает по правилам - чисто и без следов. Такая работа требует полного самообладания и беспристрастности, и в своём деле ему нет равных. Бишоп всегда работал один, но ему пришлось стать наставником молодого и отчаянного Стива. Методичный профессионал и импульсивный ученик теперь на пару устраняют проблемы, но рано или поздно они сойдутся в смертельной схватке.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Механик*", parse_mode="Markdown")

#Боевики - Стрелок 

            if call.message:
                if call.data == '1.29':
                    img = open('strelok.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2007\n*Страна* - США\n*Жанр* - боевик, триллер, драма\n*Слоган* - «Раньше он верил в справедливость. Теперь - в возмездие»\n*Режиссер* - Антуан Фукуа\n*Сценарий* - Джонатан Лемкин, Стивен Хантер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/6538-film-strelok-2007.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Опытный снайпер Боб Ли оказывается втянутым в заговор с целью убийства президента. Похоже, что его хотят подставить и «сдать» властям, поэтому ему необходимо как можно быстрее найти и обезвредить настоящего убийцу…", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Стрелок*", parse_mode="Markdown")

#Боевики - Город грехов 

            if call.message:
                if call.data == '1.30':
                    img = open('gorod-grehov.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2005\n*Страна* - США\n*Жанр* - боевик, триллер, криминал, детектив\n*Слоган* - «Deadly little Miho»\n*Режиссер* - Фрэнк Миллер, Квентин Тарантино, Роберт Родригес\n*Сценарий* - Фрэнк Миллер, Роберт Родригес", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/5627-film-gorod-grehov-2005.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Город грехов - это бездна преступлений. Здесь полиция коррумпирована, а улицы смертельно опасны. Тем не менее один из жителей пытается найти убийцу своей подруги. Другой, фотограф, случайно становится свидетелем убийства полицейского и старается скрыть преступление. Спуститесь по глухому переулку города, и вы найдете кое-что еще.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Город грехов*", parse_mode="Markdown")
 
 
 
 
 
 
                
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
 
      
        
        
        
        
#Ужасы - Поезд в Пусан     
            if call.message:
                if call.data == '1.31':
                    img = open('poezd-v-pusan.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2016\n*Страна* - Корея Южная \n*Жанр* - ужасы, боевик\n*Слоган* - «Остаться в живых или остаться человеком»\n*Режиссер* - Ён Сан-хо\n*Сценарий* - Пак Чу-сок, Ён Сан-хо", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/12957-film-poezd-v-pusan-2016.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        У маленькой Су-ан день рождения. Девочка живет с отцом в Сеуле и очень хочет отправиться к маме в Пусан. По дороге случается непредвиденное, и на страну обрушивается загадочный вирус. Пассажирам поезда в Пусан — единственного города, отразившего атаки вируса — придется бороться за выживание. 442 километра в пути. Добро пожаловать на борт и помните — в этой гонке недостаточно выжить, чтобы остаться человеком.", reply_markup=markup, parse_mode="Markdown")
                
        # убирает инлайн кнопку
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Поезд в Пусан*", parse_mode="Markdown")
 
#Ужасы - Война миров Z  
            if call.message:
                if call.data == '1.32':
                    img = open('film-vojna-mirov-z.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2013\n*Страна* - США \n*Жанр* - ужасы, фантастика, боевик, приключения\n*Слоган* - «I can't leave my family»\n*Режиссер* - Марк Форстер\n*Сценарий* - Мэттью Майкл Карнахан, Дрю Годдард, Дэймон Линделоф", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/6627-film-vojna-mirov-z-2013.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Бывший сотрудник ООН Джерри Лэйн оказывается в эпицентре эпидемии неизвестного вируса, который за считанные секунды превращает людей в зомби. Пытаясь найти противоядие против вируса, Лэйн путешествует вместе со своей группой почти по всему миру, поражённому эпидемией. Теперь судьба всего мира висит на волоске, и Джерри — его единственная надежда.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Война миров Z*", parse_mode="Markdown")


#Ужасы - Добро пожаловать в Zомбилэнд 
            if call.message:
                if call.data == '1.33':
                    img = open('dobro-pozhalovat-v-zombiljend.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2009\n*Страна* - США\n*Жанр* - ужасы, комедия, боевик\n*Слоган* - «Живой мертвому не товарищ»\n*Режиссер* - Рубен Фляйшер\n*Сценарий* - Ретт Риз, Пол Верник", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/7474-film-dobro-pozhalovat-v-zombiljend-2009.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        После нашествия зомби в США небольшая группа выживших скитается по стране от побережья к побережью, сражаясь с живыми мертвецами. Они решают остановиться в парке развлечений, надеясь, что там будут в безопасности.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Добро пожаловать в Zомбилэнд*", parse_mode="Markdown")

#Ужасы - Заклятие 

            if call.message:
                if call.data == '1.34':
                    img = open('zakljatie.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2013\n*Страна* - США\n*Жанр* - ужасы, детектив\n*Слоган* - «Основано на реальной истории Уорренов»\n*Режиссер* - Джеймс Ван\n*Сценарий* - Чад Хэйес, Кэри Хэйес", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/7926-film-zakljatie-2013.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Эд и Лоррейн Уоррены — детективы, которые расследуют паранормальные дела. Однажды к ним обращается семья, страдающая от злого духа. Уоррены, вынужденные сражаться с могущественной демонической сущностью, сталкиваются с самым пугающим случаем в своей жизни.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Заклятие*", parse_mode="Markdown")

#Ужасы - 28 дней спустя 

            if call.message:
                if call.data == '1.35':
                    img = open('28-dnej-spustja.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2002\n*Страна* - Великобритания\n*Жанр* - ужасы, фантастика, триллер, драма\n*Слоган* - «Твои дни сочтены!»\n*Режиссер* - Дэнни Бойл\n*Сценарий* - Алекс Гарленд", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/42888-film-28-dnej-spustja-2002.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Группа «зеленых» экстремистов вторгается в центр исследования приматов и выпускает из секретной научной лаборатории обезьяну, зараженную вирусом неудержимой агрессии. Смертельный вирус, передающийся через кровь за считанные секунды, приводит к мгновенному заражению и, соприкоснувшись с любым живым существом, превращает его в кровожадного монстра.\n        28 дней спустя вся Великобритания охвачена страшной эпидемией: многие эвакуируются, другие ищут безопасные места в надежде спастись. Те, кому посчастливилось не заразиться, вместе с группой военных прячутся в заброшенном доме.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*28 дней спустя*", parse_mode="Markdown")

#Ужасы - Мгла

            if call.message:
                if call.data == '1.36':
                    img = open('mgla.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2007\n*Страна* - США\n*Жанр* - ужасы, триллер, фантастика\n*Слоган* - «Fear Changes Everything»\n*Режиссер* - Фрэнк Дарабонт\n*Сценарий* - Фрэнк Дарабонт, Стивен Кинг", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/44900-film-mgla-2007.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Маленький городок накрывает сверхъестественный туман, отрезая людей от внешнего мира. Группе героев, оказавшихся в этот момент в супермаркете, приходится вступить в неравный бой с обитающими в тумане монстрами.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Мгла*", parse_mode="Markdown")

#Ужасы - Мумия 

            if call.message:
                if call.data == '1.37':
                    img = open('mumija.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1999\n*Страна* - США, Великобритания, Марокко\n*Жанр* - фэнтези, приключения, боевик\n*Слоган* - «Death is only the beginning»\n*Режиссер* - Стивен Соммерс\n*Сценарий* - Стивен Соммерс, Джон Л. Болдерстон, Ллойд Фонвиелл", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/32903-film-mumija-1999.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        На бескрайних просторах египетской пустыни компания сорвиголов разных национальностей рыщет в поисках несметных сокровищ фараона, над которыми тяготеет жуткое древнее проклятие.\n        Рядом с кладом покоится мумия коварного жреца, жестоко казненного за ужасное убийство могущественного правителя Египта. Золотоискатели потревожили многовековой покой гробницы, и мумия встает из могилы, чтобы погрузить мир в царство кошмара...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Мумия*", parse_mode="Markdown")

#Ужасы - Живое 

            if call.message:
                if call.data == '1.38':
                    img = open('zhivoe.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2017\n*Страна* - США, Великобритания\n*Жанр* - ужасы, фантастика, триллер\n*Слоган* - «Умное. Сильное. Бездушное»\n*Режиссер* - Даниэль Эспиноса\n*Сценарий* - Ретт Риз, Пол Верник", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/12785-film-zhivoe-2017.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Группа исследователей с международного космического корабля обнаруживает жизнь на Марсе. Они еще не подозревают, какие события повлечет за собой их открытие.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Живое*", parse_mode="Markdown")

#Ужасы - Дракула 

            if call.message:
                if call.data == '1.39':
                    img = open('drakula.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2014\n*Страна* - США, Великобритания, Ирландия\n*Жанр* - ужасы, фэнтези, боевик, драма\n*Слоган* - «Легенда обретёт бессмертие»\n*Режиссер* - Гари Шор\n*Сценарий* - Мэтт Сазама, Берк Шарплесс, Брэм Стокер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/7074-film-drakula-2014.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Влад Дракула был величайшим правителем, доблестным воином и страстным мужчиной. Но судьба свела его с врагом, коварство которого не знало границ. И тогда Дракула заключил сделку – нечеловеческая сила в обмен на самую малость – бессмертную душу…", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Дракула*", parse_mode="Markdown")

#Ужасы - Хижина в лесу 

            if call.message:
                if call.data == '1.40':
                    img = open('hizhina-v-lesu.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2011\n*Страна* - США\n*Жанр* - ужасы, комедия, фэнтези\n*Слоган* - «Думаете, знакомая история?»\n*Режиссер* - Дрю Годдард\n*Сценарий* - Джосс Уидон, Дрю Годдард", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/7391-film-hizhina-v-lesu-2012.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Компания из пяти студентов отправляется на выходные в лесной домик, который недавно купил брат одного из них, — подальше от учёбы, где можно оторваться по-настоящему. Слегка поднабравшись, ребята обнаруживают дверь в подвал, где находят странную книгу и читают вслух заклинание, которое выпускает на волю полчища зомби. И это только начало невообразимых ужасов, с которыми придётся столкнуться незадачливым студентам.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Хижина в лесу*", parse_mode="Markdown")
   
   
   
   
   
   
   
             
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
 
  
 
      
        
        
        
#Мультфильмы - Лука     
            if call.message:
                if call.data == '1.41':
                    img = open('luka.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2021\n*Страна* - США \n*Жанр* - мультфильм, фэнтези, комедия, приключения, семейный\n*Слоган* - —\n*Режиссер* - Энрико Касароса\n*Сценарий* - Майк Джонс, Энрико Касароса, Джесси Эндрюс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/41385-multfilm-luka-2021.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Незабываемые каникулы, в которых есть место и домашней пасте, и мороженому, и бесконечным поездкам на мопеде, мальчик Лука проводит в красивом приморском городке на итальянской Ривьере. Ни одно приключение Луки не обходится без участия его нового лучшего друга, и беззаботность отдыха омрачает только лишь тот факт, что на самом деле в облике мальчика скрывается морской монстр из глубин лагуны, на берегу которой стоит городок.", reply_markup=markup, parse_mode="Markdown")
                
        # убирает инлайн кнопку
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Лука*", parse_mode="Markdown")
 
#Мультфильмы - Моана  
            if call.message:
                if call.data == '1.42':
                    img = open('moana.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2016\n*Страна* - США \n*Жанр* - мультфильм, мюзикл, фэнтези, комедия, приключения, семейный\n*Слоган* - «The ocean is calling»\n*Режиссер* - Рон Клементс, Джон Маскер, Дон Холл\n*Сценарий* - Джаред Буш, Рон Клементс, Джон Маскер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/17731-multfilm-moana-2016.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Бесстрашная Моана, дочь вождя маленького племени на острове в Тихом океане, больше всего на свете мечтает о приключениях и решает отправиться в опасное морское путешествие. Вместе с некогда могущественным полубогом Мауи им предстоит пересечь океан, сразиться со страшными чудовищами и разрушить древнее заклятие.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Моана*", parse_mode="Markdown")


#Мультфильмы - Ходячий замок 
            if call.message:
                if call.data == '1.43':
                    img = open('hodjachij-zamok.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2004\n*Страна* - Япония\n*Жанр* - аниме, мультфильм, фэнтези, мелодрама, приключения\n*Слоган* - —\n*Режиссер* - Хаяо Миядзаки\n*Сценарий* - Хаяо Миядзаки, Диана Уинн Джонс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://re.lordfilm.frl/15890-hodjachij-zamok-2004.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Злая ведьма заточила 18-летнюю Софи в тело старухи. Девушка-бабушка бежит из города куда глаза глядят и встречает удивительный дом на ножках, где знакомится с могущественным волшебником Хаулом и демоном Кальцифером. Кальцифер должен служить Хаулу по договору, условия которого он не может разглашать. Девушка и демон решают помочь друг другу избавиться от злых чар.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ходячий замок*", parse_mode="Markdown")

#Мультфильмы - Унесенные призраками 

            if call.message:
                if call.data == '1.44':
                    img = open('unesennye-prizrakami.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2001\n*Страна* - Япония\n*Жанр* - аниме, мультфильм, фэнтези, приключения, семейный\n*Слоган* - «The tunnel led Chihiro to a mysterious town...»\n*Режиссер* - Хаяо Миядзаки\n*Сценарий* - Хаяо Миядзаки", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://re.lordfilm.frl/15969-unesennye-prizrakami-2001.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Тихиро с мамой и папой переезжает в новый дом. Заблудившись по дороге, они оказываются в странном пустынном городе, где их ждет великолепный пир. Родители с жадностью набрасываются на еду и к ужасу девочки превращаются в свиней, став пленниками злой колдуньи Юбабы. Теперь, оказавшись одна среди волшебных существ и загадочных видений, Тихиро должна придумать, как избавить своих родителей от чар коварной старухи.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Унесенные призраками*", parse_mode="Markdown")

#Мультфильмы - Король лев 

            if call.message:
                if call.data == '1.45':
                    img = open('korol-lev.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2019\n*Страна* - США, Великобритания\n*Жанр* - мультфильм, мюзикл, драма, приключения, семейный\n*Слоган* - «The King Has Returned»\n*Режиссер* - Джон Фавро\n*Сценарий* - Джефф Натансон, Ирен Меччи, Джонатан Робертс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://re.lordfilm.frl/18079-korol-lev-2019.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        История об отважном львенке по имени Симба. Знакомые с детства герои взрослеют, влюбляются, познают себя и окружающий мир, совершают ошибки и делают правильный выбор.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Король лев*", parse_mode="Markdown")

#Мультфильмы - Зов предков

            if call.message:
                if call.data == '1.46':
                    img = open('zov-predkov.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2020\n*Страна* - США, Канада\n*Жанр* - драма, приключения, семейный\n*Слоган* - «Based on the Legendary Novel»\n*Режиссер* - Крис Сандерс\n*Сценарий* - Майкл Грин, Эгертон Райерсон Янг, Джек Лондон", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://re.lordfilm.frl/3660-zov-predkov-2020.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        История Бака, дружелюбного пса, чья размеренная домашняя жизнь перевернулась с ног на голову во времена золотой лихорадки в 1880-х, когда его вырвали из дома в Калифорнии и перевезли в дикую и холодную Аляску. Будучи новичком в упряжке почтовой службы, а впоследствии лидером, Бак попадает в невероятное приключение, находит свое место в мире и становится хозяином своей жизни.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Зов предков*", parse_mode="Markdown")

#Мультфильмы - Валл-и 

            if call.message:
                if call.data == '1.47':
                    img = open('vall-i.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2008\n*Страна* - США \n*Жанр* - мультфильм, фантастика, приключения, семейный\n*Слоган* - «Любовь - дело техники»\n*Режиссер* - Эндрю Стэнтон\n*Сценарий* - Эндрю Стэнтон, Джим Рирдон, Пит Доктер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/17905-multfilm-vall-i-2008.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Робот ВАЛЛ·И из года в год прилежно трудится на опустевшей Земле, очищая нашу планету от гор мусора, которые оставили после себя улетевшие в космос люди. Он и не представляет, что совсем скоро произойдут невероятные события, благодаря которым он встретит друзей, поднимется к звездам и даже сумеет изменить к лучшему своих бывших хозяев, совсем позабывших родную Землю.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Валли*", parse_mode="Markdown")

#Мультфильмы - Корпорация монстров 

            if call.message:
                if call.data == '1.48':
                    img = open('korporacija-monstrov.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2001\n*Страна* - США\n*Жанр* - мультфильм, фэнтези, комедия, приключения, семейный\n*Слоган* - «We Think They Are Scary, But Really We Scare Them!»\n*Режиссер* - Пит Доктер, Дэвид Силверман, Ли Анкрич\n*Сценарий* - Эндрю Стэнтон, Дэниел Герсон, Пит Доктер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/3710-multfilm-korporacija-monstrov-2001.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Склизкий гад в сливном бачке, мохнатый зверь, похожий на чудовище из «Аленького цветочка», гигантские мокрицы под кроватью — все они существуют на самом деле. Все, что им нужно — пугать детей, потому что из детских криков они получают электричество. \n        Полнометражный мультфильм рассказывает о кризисах в мире монстров, их жизни. Но однажды вся мирная жизнь монстров оказывается под угрозой: в их мир попадает ребенок. А с детьми столько хлопот, что они могут довести даже монстров.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Корпорация монстров*", parse_mode="Markdown")

#Мультфильмы - Мулан 

            if call.message:
                if call.data == '1.49':
                    img = open('mulan.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2020\n*Страна* - США, Китай, Канада\n*Жанр* - боевик, фэнтези, драма\n*Слоган* - «Loyal, Brave, True»\n*Режиссер* - Антуан Фукуа\n*Сценарий* - Ники Каро", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/575-film-mulan-2020.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Изданный императором Китая указ о призыве на службу в армии одного мужчины из каждой семьи для защиты страны от северных захватчиков вдохновляет Мулан, старшую дочь почетного воина, занять в войсках место больного отца. Одевшись мужчиной, девушка подвергается испытаниям на каждом шагу, проявляя свои внутреннюю силу и истинный потенциал. Мулан ждет эпичное путешествие, которое превратит её в доблестного воина, позволит заслужить уважение народа и стать гордостью отца.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Мулан*", parse_mode="Markdown")

#Мультфильмы - Вокруг света за 80 дней 

            if call.message:
                if call.data == '1.50':
                    img = open('vokrug-sveta-za-80-dnej.jpeg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2021\n*Страна* - Франция, Бельгия\n*Жанр* - мультфильм, комедия, приключения, семейный\n*Слоган* - —\n*Режиссер* - Самуэль Турно\n*Сценарий* - Джерри Суоллоу, Дэвид Мишель, Дерек Дресслер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/7927-multfilm-vokrug-sveta-za-80-dnej-2021.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Умнейший Паспарту всегда мечтал о путешествиях. На его удачу безрассудный Филеас согласился на безумное пари — обогнуть земной шар всего за 80 дней. Теперь двум совершенно непохожим друзьям предстоит совершить невозможное, а заодно увидеть весь мир, полный фантастических созданий, живописных мест и умопомрачительных приключений.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Вокруг света за 80 дней*", parse_mode="Markdown")
   
   
   
   
   
                
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
 
  
 
  
      
        
        
#Приключения - Выживший     
            if call.message:
                if call.data == '1.51':
                    img = open('vyzhivshij.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2015\n*Страна* - США, Гонконг, Тайвань \n*Жанр* - приключения, вестерн, боевик, драма, биография\n*Слоган* - «До последней капли крови»\n*Режиссер* - Алехандро Гонсалес Иньярриту\n*Сценарий* - Марк Л. Смит, Алехандро Гонсалес Иньярриту, Майкл Панке", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/1883-film-vyzhivshij-2015.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Охотник Хью Гласс серьезно ранен на неизведанных просторах американского Дикого Запада. Товарищ Хью по отряду покорителей новых земель Джон Фицжеральд предательски оставляет его умирать в одиночестве. Теперь у Гласса осталось только одно оружие – его сила воли. Он готов бросить вызов первобытной природе, суровой зиме и враждебным племенам индейцев, только чтобы выжить и отомстить Фицжеральду.", reply_markup=markup, parse_mode="Markdown")
                
        # убирает инлайн кнопку
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Выживший*", parse_mode="Markdown")
 
#Приключения - Парк Юрского периода  
            if call.message:
                if call.data == '1.52':
                    img = open('park-jurskogo-perioda.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1993\n*Страна* - США \n*Жанр* - приключения, фантастика, семейный\n*Слоган* - «The most phenomenal discovery of our time... becomes the greatest adventure of all time»\n*Режиссер* - Стивен Спилберг\n*Сценарий* - Майкл Крайтон, Дэвид Кепп", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/1920-film-park-jurskogo-perioda-1993.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Экспансивный богач и профессор уговаривает двух палеонтологов приехать на остров у побережья Коста-Рики, где он устроил парк Юрского периода. Парк населен давно вымершими динозаврами, воссозданными профессором по образцам крови из ископаемого комара, которые должны стать гвоздем программы нового аттракциона. До открытия остается несколько дней, а один из сотрудников, пытаясь украсть бесценные эмбрионы, нарушает систему охраны, что вместе с грозовым ливнем приводит к отключению электричества и защитных барьеров. Как раз в тот момент, когда палеонтологи с внуками профессора отправились на пробную экскурсию.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Парк Юрского периода*", parse_mode="Markdown")


#Приключения - Анчартед: На картах не значится 
            if call.message:
                if call.data == '1.53':
                    img = open('ancharted-na-kartah-ne-znachitsja.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2022\n*Страна* - США, Испания\n*Жанр* - приключения, боевик\n*Слоган* - —\n*Режиссер* - Рубен Фляйшер\n*Сценарий* - Артур Маркам, Мэтт Холлоуэй, Рэйф Джадкинс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/7846-film-ancharted-na-kartah-ne-znachitsja-2022.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Нейтан Дрейк не видел старшего брата Сэма 15 лет, с тех пор как тот сбежал из сиротского приюта. Парень работает барменом и промышляет мелким воровством, когда на него выходит Виктор Салливан по прозвищу Салли и предлагает отправиться на поиски давно потерянных сокровищ Магеллана. Узнав, что Салли знаком с Сэмом, Нейтан соглашается на авантюру, надеясь также отыскать и брата.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Анчартед: На картах не значится*", parse_mode="Markdown")

#Приключения - Кон - тики 

            if call.message:
                if call.data == '1.54':
                    img = open('kon-tiki.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2012\n*Страна* - Норвегия, Великобритания, Дания, Германия, Швеция\n*Жанр* - приключения, биография, история, драма\n*Слоган* - «Через океан в поисках истины»\n*Режиссер* - Хоаким Роннинг, Эспен Сандберг\n*Сценарий* - Петтер Скавлан", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/8303-film-kon-tiki-2012.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        История о всемирно известном путешественнике Туре Хейердале, совершившем в 1947 году эпическую экспедицию – пересечение Тихого океана на плоту Кон-Тики. Гигантские киты, схватки с голодными акулами, грозовой шторм, раздирающий ветер, битва за жизнь посреди бушующей стихии. Героям предстоит проявить немалую силу и трудолюбие, чтобы этот день не стал последним. Это невероятное путешествие навсегда изменит людей, которые рискнули в него отправиться.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Кон - тики*", parse_mode="Markdown")

#Приключения - Круиз по джунглям 

            if call.message:
                if call.data == '1.55':
                    img = open('kruiz-po-dzhungljam.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2021\n*Страна* - США\n*Жанр* - приключения, комедия, фэнтези\n*Слоган* - —\n*Режиссер* - Жауме Кольет-Серра\n*Сценарий* - Майкл Грин, Гленн Фикарра, Джон Рекуа", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/1268-film-kruiz-po-dzhungljam-2021.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Хитростью и немалой сноровкой раздобыв бесценную карту верховьев Амазонки, бойкая археолог Лили Хоутон отправляется в экспедицию, чтобы найти волшебное дерево, цветок которого — согласно легенде — обладает невероятными целебными свойствами. Прихватив с собой младшего брата, который не в восторге от перспективы поездки в дикие джунгли, девушка нанимает проводника — капитана круизного пароходика по имени Фрэнк. Вся компания пускается в приключение, где их подстерегают не только смертельно опасные представители амазонской флоры и фауны, но и ловушки, подстроенные участниками конкурирующей экспедиции.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Круиз по джунглям*", parse_mode="Markdown")

#Приключения - Время первых

            if call.message:
                if call.data == '1.56':
                    img = open('vremja-pervyh.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2017\n*Страна* - Россия\n*Жанр* - приключения, триллер, биография, история\n*Слоган* - «Подними голову!»\n*Режиссер* - Дмитрий Киселёв\n*Сценарий* - Юрий Коротков, Сергей Калужанов, Ирина Пивоварова", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/41994-film-vremja-pervyh-2017.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        1960-е, разгар холодной войны. Две супердержавы - СССР и США - бьются за первенство в космической гонке. Пока СССР впереди, на очереди — выход человека в открытый космос. За две недели до старта взрывается тестовый корабль. Времени на выявление причин нет. Опытный военный лётчик Павел Беляев и его напарник Алексей Леонов, необстрелянный и горячий, мечтающий о подвиге, — два человека, готовые шагнуть в неизвестность. Но никто не мог даже предположить всего, с чем им предстояло столкнуться в полёте. В этой миссии всё, что только могло, пошло не так.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Время первых*", parse_mode="Markdown")

#Приключения - Тайны печати дракона 

            if call.message:
                if call.data == '1.57':
                    img = open('tajna-pechati-drakona.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2019\n*Страна* - Россия, Китай\n*Жанр* - приключения, фэнтези\n*Слоган* - —\n*Режиссер* - Олег Степченко\n*Сценарий* - Олег Степченко, Алексей А. Петрухин, Дмитрий Пальцев", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://2022-88.lordfilm0.com/films/173-tajna-pechati-drakona-07-01.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Английский путешественник Джонатан Грин получает от Петра I заказ на изготовление карт Дальнего Востока России. Ему вновь предстоит долгий путь, полный невероятных приключений, который приведет его в Китай. Картограф столкнется с массой головокружительных открытий, неожиданных встреч с диковинными существами, китайскими принцессами, мастерами смертоносных боевых искусств и самим Лун-Ван, Царем всех драконов. Что может быть опаснее, чем посмотреть в глаза Вию? Разве что встретиться с ним вновь. Что на этот раз окажется сильнее – непоколебимый скептицизм ученого или древняя черная магия, уже давно захватившая власть в Восточных землях?", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Тайны печати дракона*", parse_mode="Markdown")

#Приключения - Восточный ветер 

            if call.message:
                if call.data == '1.58':
                    img = open('ostvind-vostochnyj-veter.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2013\n*Страна* - Германия\n*Жанр* - приключения, семейный, драма\n*Слоган* - —\n*Режиссер* - Кристина Магдалена Хенн, Леа Шмидбауэр\n*Сценарий* - Ева Карлстрём, Андреас Ульмке-Смитон, Мартин Мошкович", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/33737-film-ostvind-vostochnyj-veter-2013.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Из-за плохой успеваемости родители отправляют 14-летнюю Мику в поместье к строгой бабушке. Поездка преподносит один сюрприз за другим: оказывается, бабушка, Мария Кальтенбах – знаменитая всадница в прошлом, которая теперь тренирует молодые таланты и разводит лошадей. Несмотря на то, что сама Мика ни разу в жизни не ездила верхом, да и не горит желанием научиться, один из обитателей конюшни - вороной жеребец по имени Оствинд неожиданно привлекает её внимание. Девушка легко находит с ним общий язык, даже не подозревая о том, что все вокруг считают коня диким и опасным. Так начинается их необыкновенная дружба.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Восточный ветер*", parse_mode="Markdown")

#Приключения - Эбигейл 

            if call.message:
                if call.data == '1.59':
                    img = open('jebigejl.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2019\n*Страна* - Россия\n*Жанр* - приключения, фэнтези, семейный\n*Слоган* - «В мире всё не то, чем кажется»\n*Режиссер* - Александр Богуславский\n*Сценарий* - Дмитрий Жигалов, Александр Богуславский, Александра Примаченко", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/13224-film-jebigejl-2019.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Молодая девушка Эбигейл живет в городе, границы которого закрыли много лет назад из-за эпидемии загадочной болезни. Отец Эбби был одним из заболевших – и его забрали, когда ей было шесть лет. Пойдя наперекор властям, чтобы разыскать отца, Эбби узнает о том, что ее город на самом деле полон магии. И в ней самой пробуждаются необыкновенные магические способности…", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Эбигейл*", parse_mode="Markdown")

#Приключения - Эспен в королевстве троллей 

            if call.message:
                if call.data == '1.60':
                    img = open('jespen-v-korolevstve-trollej.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2017\n*Страна* - Норвегия\n*Жанр* - приключения, семейный\n*Слоган* - «Something big is coming»\n*Режиссер* - Миккель Бренне Сандемусе\n*Сценарий* - Александр Кирквуд Браун, Эспен Энгер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/13011-film-jespen-v-korolevstve-trollej-2017.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Эспен живет с отцом и братьями на ферме. Однажды из-за своей неуёмной фантазии и неуклюжести он сжигает дом. Также выясняется, что девушка, которую он повстречал в лесу за день до этого - сбежавшая принцесса, и за помощь в ее поисках полагается вознаграждение. Эспен с братьями ввязываются в опасное приключение и идут спасать принцессу из рук Горного Короля - тролля, который по легенде пробуждается, если принцесса не выходит замуж до своего 18-летия. Однако братья - не единственные, кто ищет принцессу, её также разыскивает принц, который хочет жениться на ней из корыстных побуждений.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Эспен в королевстве троллей*", parse_mode="Markdown")
   
   
   
   
   
                
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
 
 
     
    
        
        
        
#Норвегия - Худший человек на свете
  
            if call.message:
                if call.data == '2.1':
                    img = open('hudshiy-chelovek-na-svete.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,4/10\n*Год производства* - 2021 \n*Жанр* - Норвегия, Франция, Швеция, Дания\n*Слоган* - —\n*Режиссер* - Йоаким Триер\n*Сценарий* - Йоаким Триер, Эскиль Вогт", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://w1.fullsee.site/movies/10069-hudshiy-chelovek-na-svete/watch/MTAwNjk6OjMwMTI5/")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Юная студентка Юлия из хорошей норвежской семьи начинает взрослую жизнь, думая, что станет врачом. Её главные черты — беспокойство и рефлексия. Ни одно событие и переживание Юлия не оставляет просто так, ставит под сомнение собственные и чужие ценности и живёт в постоянном внутреннем конфликте. После первых месяцев учёбы она решает, что психология ей куда ближе, чем медицина — а потом увлекается писательством, фотографией и книжным делом. Фильм разбит на 12 последовательных глав: Юлия меняет профессии и возлюбленных, переживает длительные отношения и лёгкие увлечения, приспосабливается к новым обстоятельствам и открывает разные стороны своей личности.", reply_markup=markup, parse_mode="Markdown")
                
        # убирает инлайн кнопку
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Худший человек на свете*", parse_mode="Markdown")
 
#Норвегия - Тысячу раз «спокойной ночи»  
            if call.message:
                if call.data == '2.2':
                    img = open('tysjachu-raz-spokojnoj-nochi.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,3/10\n*Год производства* - 2013 \n*Жанр* - драма, военный\n*Слоган* - «She risked life and family to change the world»\n*Режиссер* - Эрик Поппе\n*Сценарий* - Эрик Поппе, Харальд Розенлёв-Эег, Jan Trygve Røyneland", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/46401-film-tysjachu-raz-spokojnoj-nochi-2013.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Ребекка выдающийся военный фотограф. Её муж и дочери не могут больше мириться с тем, что она подвергает свою жизнь опасности, и ставят ей ультиматум: работа или семья. Выбор, кажется, очевиден...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Тысячу раз «спокойной ночи»*", parse_mode="Markdown")


#Норвегия - Охотники за головами 
            if call.message:
                if call.data == '2.3':
                    img = open('ohotniki-za-golovami.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,5/10\n*Год производства* - 2011 \n*Жанр* - боевик, триллер, криминал\n*Слоган* - «The hunt is on»\n*Режиссер* - Мортен Тильдум\n*Сценарий* - Ульф Рюберг, Ларс Гудместад, Ю Несбё", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/44003-film-ohotniki-za-golovami-2011.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Роджер Браун - блестящий «охотник за головами», незаменимый специалист по подбору топ-менеджеров для крупнейших фирм. Он может найти нужного человека на любую должность и его рекомендация - залог получения работы. Чтобы удержать красавицу жену, открывшую на деньги мужа картинную галерею в модном районе, Роджер давно уже живет не по средствам, и, пользуясь своим служебным положением, крадет дорогие картины у претендентов на руководящие должности.\n        Однажды Роджер встречает голландца Класа Граафа: идеального кандидата для фирмы, специализирующейся на навигационном оборудовании, и - вот удача! - владельца картины Рубенса, считавшейся утерянной во время Второй мировой войны. Кража и последующая продажа шедевра может помочь Роджеру навсегда решить все финансовые проблемы.\n        Но, внезапно, «охотник за головами» сам превращается в добычу.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Охотники за головами*", parse_mode="Markdown")

#Норвегия - Король чёртова острова 

            if call.message:
                if call.data == '2.4':
                    img = open('korol-chertova-ostrova.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,5/10\n*Год производства* - 2010 \n*Жанр* - Норвегия, Франция, Швеция, Польша\n*Слоган* - «Norway, 1915, a home for boys»\n*Режиссер* - Мариус Хольст\n*Сценарий* - Деннис Магнуссон, Эрик Шмид, Метте М. Больстад", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/40240-film-korol-chertova-ostrova-2010.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Норвегия начала XX века. Зима. На острове Бастёй, что в Осло фьорде, расположена колония для бездомных подростков. Их содержат в поистине садистских условиях: психологическое давление и унижение – это методы, с помощью которых охрана держит их в узде. Им не дают никакого образования, зато используют в качестве дешевой рабочей силы. 11-18 летние подростки выживают, благодаря вынужденной адаптации к нечеловеческим условиям. Они жестоки, они вынуждены договариваться друг с другом, они покупают и продают.\n        Эрлинг, очередной отщепенец 17 лет, волей судьбы попавший на остров, в целях самозащиты случайно убивает офицера, и следующей весной, когда ему исполнится 18, его должны переправить в тюрьму для взрослых. По сути, Эрлинг доживает свою последнюю зиму, потому что перевод в другую тюрьму означает для него неминуемую смерть. Но у него совсем другие планы. Он решает сделать невозможное - сбежать с Бастёя, острова Дьявола.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Король чёртова острова*", parse_mode="Markdown")

#Норвегия - Гунда 

            if call.message:
                if call.data == '2.5':
                    img = open('gunda.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,5/10\n*Год производства* - 2020 \n*Жанр* - документальный\n*Слоган* - —\n*Режиссер* - Виктор Косаковский\n*Сценарий* - Виктор Косаковский, Айнара Вера", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://w1.fullsee.site/movies/10148-gunda/watch/MTAxNDg6OjMwMzM3/")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Мы делим нашу планету с миллиардами других животных. Через встречи со свиноматкой Гундой, двумя коровами и курицей мы можем задуматься о врожденной ценности жизни и тайне всего животного сознания, в том числе и нашего собственного.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Гунда*", parse_mode="Markdown")





       
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------          


        
        
        
        
#Россия - Брат     
            if call.message:
                if call.data == '2.6':
                    img = open('brat.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 8,3/10\n*Год производства* - 1997 \n*Жанр* - драма, криминал, боевик\n*Слоган* - —\n*Режиссер* - Алексей Балабанов\n*Сценарий* - Алексей Балабанов", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/4331-film-brat-1997.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Демобилизовавшись, Данила Багров вернулся в родной городок. Но скучная жизнь российской провинции не устраивала его, и он решился податься в Петербург, где, по слухам, уже несколько лет процветает его старший брат. Данила нашел брата. Но все оказалось не так просто — брат работает наемным убийцей.", reply_markup=markup, parse_mode="Markdown")
                
        # убирает инлайн кнопку
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Брат*", parse_mode="Markdown")
 
#Россия - Дурак  
            if call.message:
                if call.data == '2.7':
                    img = open('durak.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 8,1/10\n*Год производства* - 2014 \n*Жанр* - драма\n*Слоган* - «Успеет ли он спасти всех»\n*Режиссер* - Юрий Быков\n*Сценарий* - Юрий Быков", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/3859-film-durak-2014.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Жизни 800 человек общежития висят буквально на волоске из-за безразличия местных властей. В любую секунду здание может рухнуть. И кто бы мог подумать, что судьбы людей окажутся в руках простого сантехника. Но удастся ли ему что-то изменить и предотвратить катастрофу?", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Дурак*", parse_mode="Markdown")


#Россия - Легенда №17 
            if call.message:
                if call.data == '2.8':
                    img = open('legenda-17.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 8,0/10\n*Год производства* - 2012 \n*Жанр* - спорт, драма, биография\n*Слоган* - —\n*Режиссер* - Николай Лебедев\n*Сценарий* - Михаил Местецкий, Николай Куликов, Николай Лебедев", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://max.lordfilmx.biz/24404-legenda-17.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        История жизни хоккеиста Валерия Харламова.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Легенда №17*", parse_mode="Markdown")

#Россия - О чём говорят мужчины 

            if call.message:
                if call.data == '2.9':
                    img = open('o-chem-govoryat-muzhchiny.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,8/10\n*Год производства* - 2010 \n*Жанр* - комедия\n*Слоган* - —\n*Режиссер* - Дмитрий Дьяченко\n*Сценарий* - Леонид Барац, Сергей Петрейков, Ростислав Хаит", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://1may.lordfillm1.net/2472-o-chem-govoryat-muzhchiny-0203.html?ysclid=l2ng92qtux")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        О чем говорят мужчины? Конечно, о женщинах. Нет, еще о работе, о деньгах, о машинах, о футболе,… но в основном, все-таки, о женщинах. А уж если у них впереди два дня, которые они, вырвавшись из офисов и семей, уехав от всех забот и обязательств, проведут в дороге – два дня, насыщенные событиями и приключениями – то можете быть уверены, что за это время они успеют обсудить немало тем… \n        И еще. Из этих разговоров – это мы точно знаем – многие женщины узнают о себе очень много нового...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*О чём говорят мужчины*", parse_mode="Markdown")

#Россия - Огонь 

            if call.message:
                if call.data == '2.10':
                    img = open('ogon.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,7/10\n*Год производства* - 2020 \n*Жанр* - драма, боевик\n*Слоган* - —\n*Режиссер* - Алексей Нужный\n*Сценарий* - Николай Куликов, Алексей Нужный, Константин Майер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://ok.ru/video/3482239504699")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        После гибели подчинённого бывалый инструктор бригады пожарных Алексей Соколов хотел было уволиться, но лето в России — жаркая пора. Взяв в команду шестым нахального новичка, парня своей дочери, Соколов отправляется на очередное задание в Карелию. И это задание будет гораздо сложнее, чем он мог себе представить.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Огонь*", parse_mode="Markdown")


 
 
 
 
 
                
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
 
      
        
        
        
        
#Великобритания - Эмма     
            if call.message:
                if call.data == '2.11':
                    img = open('jemma.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 6,9/10\n*Год производства* - 2020 \n*Жанр* - комедия, мелодрама\n*Слоган* - «Очаровательна, остроумна, обеспеченна»\n*Режиссер* - Отем де Уайлд\n*Сценарий* - Элинор Каттон, Джейн Остин", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/1973-film-jemma-2020.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Англия, XIX век. 21-летняя провинциалка Эмма Вудхаус красива, богата, остроумна и считает, что прекрасно разбирается в людях. Девушка решила, что никогда не выйдет замуж и не оставит отца одного. Когда её подруга в связи с собственным замужеством переезжает в дом супруга, Эмма находит себе новую компаньонку — сироту Гарриет Смит — и теперь, используя все свои хитрости, пытается устроить девушке личную жизнь.", reply_markup=markup, parse_mode="Markdown")
                
        # убирает инлайн кнопку
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Эмма*", parse_mode="Markdown")
 
#Великобритания - Три секунды  
            if call.message:
                if call.data == '2.12':
                    img = open('tri-sekundy.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 8,9/10\n*Год производства* - 2019 \n*Жанр* - триллер, криминал, боевик\n*Слоган* - «Против мафии. Против полиции. Против всех»\n*Режиссер* - Андреа Ди Стефано\n*Сценарий* - Мэтт Кук, Роуэн Жоффе, Андреа Ди Стефано", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/41-film-tri-sekundy-2019.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Бывший заключенный специально попадает под арест, чтобы стать одним из членов преступной группировки в наиболее охраняемой тюрьме в мире.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Три секунды*", parse_mode="Markdown")


#Великобритания - Гонка века 
            if call.message:
                if call.data == '2.13':
                    img = open('gonka-veka.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 9,6/10\n*Год производства* - 2017 \n*Жанр* - драма, детектив, приключения, биография\n*Слоган* - «Узнай неразгаданную тайну, потрясшую мир»\n*Режиссер* - Джеймс Марш\n*Сценарий* - Скотт З. Бёрнс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/1844-film-gonka-veka-2017.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        В 1968 году британский яхтсмен-любитель Дональд Кроухёрст, заложив все свое состояние, решил осуществить мечту всей жизни, совершив в одиночку рискованное кругосветное путешествие в рамках регаты за приз газеты Sunday Times. Вскоре после отплытия он понял, что это соревнование ему не выиграть, и задумал совершенно безумную авантюру.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Гонка века*", parse_mode="Markdown")

#Великобритания - Две королевы 

            if call.message:
                if call.data == '2.14':
                    img = open('dve-korolevy.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 8,5/10\n*Год производства* - 2018 \n*Жанр* - драма, биография, история\n*Слоган* - «Две сестры — одна судьба»\n*Режиссер* - Джози Рурк\n*Сценарий* - Бо Уиллимон, Джон Гай", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/2863-film-dve-korolevy-2018.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        1561 год, после смерти молодого мужа Франциска 18-летняя Мария Стюарт возвращается в Шотландию. Она католичка и по крови имеет право претендовать на престол Англии, чем изрядно нервирует нынешнюю протестантскую королеву Елизавету I. Прислушавшись к советникам, королева отправляет к Марии делегацию, в состав которой входит фаворит Елизаветы граф Роберт Дадли, по мнению большинства, - идеальный кандидат в супруги Марии.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Две королевы*", parse_mode="Markdown")

#Великобритания - Код «Красный» 

            if call.message:
                if call.data == '2.15':
                    img = open('kod-krasnyj.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,1/10\n*Год производства* - 2018 \n*Жанр* - биография, драма, история\n*Слоган* - «Реальная история русской шпионки, предотвратившей Третью мировую войну»\n*Режиссер* - Тревор Нанн\n*Сценарий* - Линдсэй Шаперо, Jennie Rooney", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/930-film-kod-krasnyj-2018.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Реальная история русской шпионки, которая предотвратила Третью мировую войну. Британская разведка долгие годы гонялась за ней, ее имя стало легендой, но о ее подвиге мы узнали только сейчас, когда был снят гриф секретности.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Код «Красный»*", parse_mode="Markdown")


   
   
   
   
   
   
             
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
 
  
 
      
        
        
        
#Франция - Расправь крылья     
            if call.message:
                if call.data == '2.16':
                    img = open('rasprav-krylja.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 8,0/10\n*Год производства* - 2019 \n*Жанр* - драма, приключения, семейный\n*Слоган* - —\n*Режиссер* - Николя Ванье\n*Сценарий* - Лилу Фогли, Николя Ванье, Кристиан Муллек", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/1941-film-rasprav-krylja-2019.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Подросток Тома навещает во время отдыха своего отца Кристиана, чудаковатого орнитолога. Но для юноши, увлеченного гаджетами и играми, разведение диких гусей во французской деревне и эксперименты отца наводят лишь тоску. Однако все меняется, когда Тома решает спасти исчезающий вид диких гусей и отправляется в воодушевляющее путешествие с «небесными ангелами», как их называет Кристиан.", reply_markup=markup, parse_mode="Markdown")
                
        # убирает инлайн кнопку
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Расправь крылья*", parse_mode="Markdown")
 
#Франция - Прекрасная эпоха  
            if call.message:
                if call.data == '2.17':
                    img = open('prekrasnaja-jepoha.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,7/10\n*Год производства* - 2019 \n*Жанр* - мелодрама, драма, комедия\n*Слоган* - «What if you could relive the happiest day of your life?»\n*Режиссер* - Николя Бедос\n*Сценарий* - Николя Бедос", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/691-film-prekrasnaja-jepoha-2019.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Что, если бы Вы могли отправиться в любое время в прошлом по своему выбору? Именно такую услугу предоставляет компания, которая готова скрупулёзно восстановить детали любой эпохи на заказ. Одним из ее клиентов становится талантливый художник, переживающий кризис в отношениях с любимой женой. Он использует этот шанс, чтобы снова пережить тот день, когда много лет назад он встретил любовь всей своей жизни.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Прекрасная эпоха*", parse_mode="Markdown")


#Франция - Как прогулять школу с пользой 
            if call.message:
                if call.data == '2.18':
                    img = open('kak-proguljat-shkolu-s-polzoj.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,9/10\n*Год производства* - 2017 \n*Жанр* - драма, комедия, семейный\n*Слоган* - —\n*Режиссер* - Николя Ванье\n*Сценарий* - Жером Тоннер, Николя Ванье", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/4422-film-kak-proguljat-shkolu-s-polzoj-2017.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Вслед за городским мальчиком Полем зрителям предстоит узнать то, чему в школе не учат. А именно — как жить в реальном мире. По крайней мере, если это мир леса. Здесь есть хозяин — мрачный граф, есть власть — добродушный, но строгий лесничий Борель, и есть браконьер Тотош — человек, решивший быть вне закона, да и вообще подозрительный и неприятный тип. \n        Чью сторону выберет Поль: добропорядочного лесничего Бореля или браконьера Тотоша? А может, юный сорванец и вовсе станет лучшим другом надменному графу?", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Как прогулять школу с пользой*", parse_mode="Markdown")

#Франция - Приключения Реми 

            if call.message:
                if call.data == '2.19':
                    img = open('prikljuchenija-remi.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,9/10\n*Год производства* - 2018 \n*Жанр* - мелодрама, приключения\n*Слоган* - —\n*Режиссер* - Антуан Блоссье\n*Сценарий* - Антуан Блоссье, Гектор Мало", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/1046-film-prikljuchenija-remi-2018.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Удивительное путешествие по Франции маленького Реми в компании уличного музыканта, обезьянки и цирковой собаки. Вместе им предстоит пережить неожиданные встречи, приключения и испытания, чтобы раскрыть тайну происхождения мальчика.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Приключения Реми*", parse_mode="Markdown")

#Франция - Обещание на рассвете 

            if call.message:
                if call.data == '2.20':
                    img = open('obeschanie-na-rassvete.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,8/10\n*Год производства* - 2017 \n*Жанр* - драма, мелодрама, военный, биография\n*Слоган* - —\n*Режиссер* - Эрик Барбье\n*Сценарий* - Эрик Барбье, Мари Эйнар, Ромен Гари", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/3142-film-obeschanie-na-rassvete-2017.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Экранизация автобиографического романа писателя Ромена Гари. Еще когда будущий лауреат Гонкуровской премии был ребенком, его мать твердо решила, что он станет дипломатом и всемирно известным писателем. Несмотря на то, что над ней смеялись окружающие, а сын сомневался в собственных силах, она продолжала в него верить — и все ее невероятные мечты сбылись. Материнская любовь и безусловная поддержка вели Ромена через все испытания и приключения его жизни, полной тайн, сражений и невероятных поворотов.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Обещание на рассвете*", parse_mode="Markdown")


   
   
   
   
                
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
 
  
 
  
      
        
        
#США - Побег из Шоушенка     
            if call.message:
                if call.data == '2.21':
                    img = open('pobeg-iz-shoushenka.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 9,1/10\n*Год производства* - 1994 \n*Жанр* - драма\n*Слоган* - «Страх - это кандалы. Надежда - это свобода»\n*Режиссер* - Фрэнк Дарабонт\n*Сценарий* - Фрэнк Дарабонт, Стивен Кинг", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://220429.lordfilm.black/699-film-pobeg-iz-shoushenka-1994.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание* \n        Бухгалтер Энди Дюфрейн обвинён в убийстве собственной жены и её любовника. Оказавшись в тюрьме под названием Шоушенк, он сталкивается с жестокостью и беззаконием, царящими по обе стороны решётки. Каждый, кто попадает в эти стены, становится их рабом до конца жизни. Но Энди, обладающий живым умом и доброй душой, находит подход как к заключённым, так и к охранникам, добиваясь их особого к себе расположения.", reply_markup=markup, parse_mode="Markdown")
                
        # убирает инлайн кнопку
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Побег из Шоушенка*", parse_mode="Markdown")
 
#США - Начало  
            if call.message:
                if call.data == '2.22':
                    img = open('nachalo.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 8,7/10\n*Год производства* - 2010 \n*Жанр* - фантастика, боевик, триллер, драма, детектив\n*Слоган* - «Твой разум - место преступления»\n*Режиссер* - Кристофер Нолан\n*Сценарий* - Кристофер Нолан", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://l.lordfilm-smotret.one/319-nachalo-film-2010-25")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Кобб – талантливый вор, лучший из лучших в опасном искусстве извлечения: он крадет ценные секреты из глубин подсознания во время сна, когда человеческий разум наиболее уязвим. Редкие способности Кобба сделали его ценным игроком в привычном к предательству мире промышленного шпионажа, но они же превратили его в извечного беглеца и лишили всего, что он когда-либо любил. \n        И вот у Кобба появляется шанс исправить ошибки. Его последнее дело может вернуть все назад, но для этого ему нужно совершить невозможное – инициацию. Вместо идеальной кражи Кобб и его команда спецов должны будут провернуть обратное. Теперь их задача – не украсть идею, а внедрить ее. Если у них получится, это и станет идеальным преступлением. \n        Но никакое планирование или мастерство не могут подготовить команду к встрече с опасным противником, который, кажется, предугадывает каждый их ход. Врагом, увидеть которого мог бы лишь Кобб.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Начало*", parse_mode="Markdown")


#США - Темный рыцарь 
            if call.message:
                if call.data == '2.23':
                    img = open('temnyy-rycar.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 8,5/10\n*Год производства* - 2008 \n*Жанр* - фантастика, боевик, триллер, криминал, драма\n*Слоган* - «Добро пожаловать в мир Хаоса!»\n*Режиссер* - Кристофер Нолан\n*Сценарий* - Кристофер Нолан, Джонатан Нолан, Дэвид С. Гойер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://www.lordfilm-smotret.one/49974-temnyy-rycar-film-2008-17")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Бэтмен поднимает ставки в войне с криминалом. С помощью лейтенанта Джима Гордона и прокурора Харви Дента он намерен очистить улицы Готэма от преступности. Сотрудничество оказывается эффективным, но скоро они обнаружат себя посреди хаоса, развязанного восходящим криминальным гением, известным напуганным горожанам под именем Джокер.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Темный рыцарь*", parse_mode="Markdown")

#США - Зеленая книга 

            if call.message:
                if call.data == '2.24':
                    img = open('zelenaya-kniga.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 8,4/10\n*Год производства* - 2018 \n*Жанр* - биография, комедия, драма\n*Слоган* - «Inspired by a True Friendship»\n*Режиссер* - Питер Фаррелли\n*Сценарий* - Ник Валлелонга, Брайан Хэйес Карри, Питер Фаррелли", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://www.lordfilm-smotret.one/23305-zelenaya-kniga-film-2018-22")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        1960-е годы. После закрытия нью-йоркского ночного клуба на ремонт вышибала Тони по прозвищу Болтун ищет подработку на пару месяцев. Как раз в это время Дон Ширли — утонченный светский лев, богатый и талантливый чернокожий музыкант, исполняющий классическую музыку — собирается в турне по южным штатам, где ещё сильны расистские убеждения и царит сегрегация. Он нанимает Тони в качестве водителя, телохранителя и человека, способного решать текущие проблемы. У этих двоих так мало общего, и эта поездка навсегда изменит жизнь обоих.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Зеленая книга*", parse_mode="Markdown")

#США - Волк с Уолл-стрит 

            if call.message:
                if call.data == '2.25':
                    img = open('volk-s-uoll-strit.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Рейтинг на Кинопоиск* - 7,9/10\n*Год производства* - 2013 \n*Жанр* - драма, криминал, биография, комедия\n*Слоган* - «Earn. Spend. Party»\n*Режиссер* - Мартин Скорсезе\n*Сценарий* - Теренс Уинтер, Джордан Белфорт", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://www.lordfilm-smotret.one/52421-volk-s-uoll-strit-film-2013-24")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        1987 год. Джордан Белфорт становится брокером в успешном инвестиционном банке. Вскоре банк закрывается после внезапного обвала индекса Доу-Джонса. По совету жены Терезы Джордан устраивается в небольшое заведение, занимающееся мелкими акциями. Его настойчивый стиль общения с клиентами и врождённая харизма быстро даёт свои плоды. Он знакомится с соседом по дому Донни, торговцем, который сразу находит общий язык с Джорданом и решает открыть с ним собственную фирму. В качестве сотрудников они нанимают нескольких друзей Белфорта, его отца Макса и называют компанию «Стрэттон Оукмонт». В свободное от работы время Джордан прожигает жизнь: лавирует от одной вечеринки к другой, вступает в сексуальные отношения с проститутками, употребляет множество наркотических препаратов, в том числе кокаин и кваалюд. Однажды наступает момент, когда быстрым обогащением Белфорта начинает интересоваться агент ФБР...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Волк с Уолл-стрит*", parse_mode="Markdown")

 
 
 
 
 
 
 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
   
   
   
   
   
            
# книги - Фантастические твари и где они обитают            
            if call.message:
                if call.data == '3.1':
                    img = open('tvari.jpg', 'rb')
                    bot.send_message(call.message.chat.id,"*Год производства* - 2016\n*Страна* - Великобритания, США \n*Жанр* - фэнтези, приключения, семейный\n*Слоган* - «Открой новую главу волшебного мира Дж.К.Роулинг»\n*Режиссер* - Дэвид Йейтс\n*Сценарий* - Дж.К. Роулинг", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://vikimult.net/q10055-fantasticheskie-tvari-1-2-chast/")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Поиск и изучение необычайных волшебных существ приводят магозоолога Ньюта Саламандера в Нью-Йорк. Скорее всего, он отбыл бы на поезде дальше, если бы не немаг (так в Америке называют магглов) по имени Якоб, оставленный в неположенном месте магический чемодан и побег из него фантастических животных Ньюта.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Фантастические твари и где они обитают*", parse_mode="Markdown")

# книги - голодные игры
            if call.message:
                if call.data == '3.2':
                    img = open('hunger_game.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2012\n*Страна* - США \n*Жанр* - фантастика, боевик, триллер, приключения\n*Слоган* - «Весь мир смотрит»\n*Режиссер* - Гэри Росс\n*Сценарий* - Сьюзен Коллинз, Гэри Росс, Билли Рэй", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://ae.lordfilms-s.tv/42190-film-golodnye-igry-2012.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id,  "*Описание*\n        Будущее. Деспотичное государство ежегодно устраивает показательные игры на выживание, за которыми в прямом эфире следит весь мир. Жребий участвовать в Играх выпадает юной Китнисс и тайно влюбленному в нее Питу. Они знакомы с детства, но теперь должны стать врагами. Ведь по нерушимому закону Голодных игр победить может только один из 24 участников. Судьям не важно кто выиграет, главное - зрелище. И на этот раз зрелище будет незабываемым.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Голодные игры*", parse_mode="Markdown")

# книги - Марсианин
            if call.message:
                if call.data == '3.3':
                    img = open('Marsianin.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2015\n*Страна* - Великобритания, США, Венгрия, Иордания\n*Жанр* - фантастика, приключения\n*Слоган* - «Верните его домой»\n*Режиссер* - Ридли Скотт\n*Сценарий* - Дрю Годдард, Энди Уир", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://ae.lordfilms-s.tv/34245-film-marsianin-2015.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Марсианская миссия «Арес-3» в процессе работы была вынуждена экстренно покинуть планету из-за надвигающейся песчаной бури. Инженер и биолог Марк Уотни получил повреждение скафандра во время песчаной бури. Сотрудники миссии, посчитав его погибшим, эвакуировались с планеты, оставив Марка одного. \n        Очнувшись, Уотни обнаруживает, что связь с Землёй отсутствует, но при этом полностью функционирует жилой модуль. Главный герой начинает искать способ продержаться на имеющихся запасах еды, витаминов, воды и воздуха ещё 4 года до прилёта следующей миссии «Арес-4».", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*Марсианин*", parse_mode="Markdown")

# книги - Бегущий в лабиринте

            if call.message:
                if call.data == '3.4':
                    img = open('maze_runner.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2014\n*Страна* - США, Великобритания\n*Жанр* - фантастика, триллер, приключения\n*Слоган* - «Только не останавливайся»\n*Режиссер* - Уэс Болл\n*Сценарий* - Ной Оппенхайм, Грант Пирс Майерс, Т.С. Наулин", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://ae.lordfilms-s.tv/33026-film-beguschij-v-labirinte-2014.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Главный герой — подросток Томас, который просыпается в лифте, но ничего не помнит, кроме своего имени. Он оказывается среди других подростков, научившихся выживать в замкнутом пространстве. Раз в 30 дней прибывает новый мальчик. Группа ребят проживает в «Приюте» уже три года. Они кормятся тем, что удается вырастить на земле, и пытаются найти выход из лабиринта, окружающего их место жительства. Но однажды появляется девочка в состоянии комы...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*Бегущий в лабиринте*", parse_mode="Markdown")

# книги - Дивергент

            if call.message:
                if call.data == '3.5':
                    img = open('Divergent.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2014\n*Страна* - США\n*Жанр* - фантастика, детектив, боевик, мелодрама\n*Слоган* - «Ты опасен, если ты другой»\n*Режиссер* - Нил Бёргер\n*Сценарий* - Ивэн Догерти, Ванесса Тейлор, Вероника Рот", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://ae.lordfilms-s.tv/28993-film-divergent-2014.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        В антиутопическом Чикаго будущего существует общество, члены которого придумали способ избегать конфликтов и поддерживать вокруг незыблемый порядок. Каждый человек по достижении 16 лет должен определить, к чему лежит его душа, и в зависимости от своих личностных качеств присоединиться к одной из пяти фракций – Искренность, Бесстрашие, Эрудиция, Дружелюбие или Отречение. \n        Для того, чтобы и не ошибиться с фракцией, накануне церемонии выбора подростки проходят специальное тестирование. Юная Беатрис оказывается угрозой для всей сложившейся системы, когда тесты выявляют в ней дивергента – человека, которого невозможно однозначно определить в одну из фракций. Способные мыслить независимо и не питающие особого уважения к правительству, дивергенты одним своим существованием дискредитируют принципы, на которых строится общество. И теперь Беатрис – одна из таких людей, живущих вне закона и борющихся с системой, которая намерена любой ценой от них избавиться.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Дивергент*", parse_mode="Markdown")

# книги - Сумерки

            if call.message:
                if call.data == '3.6':
                    img = open('twilight.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2008\n*Страна* - США\n*Жанр* - фэнтези, драма, мелодрама\n*Слоган* - «Запретный плод сладок»\n*Режиссер* - Кэтрин Хардвик\n*Сценарий* - Мелисса Розенберг, Стефани Майер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://ae.lordfilms-s.tv/33864-film-sumerki-2008.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Семнадцатилетняя девушка Белла переезжает к отцу в небольшой городок Форкс. Она влюбляется в загадочного одноклассника, который, как оказалось, происходит из семьи вампиров, отказавшихся от нападений на людей. Влюбиться в вампира. Это страшно? Это романтично, это прекрасно и мучительно, но это не может кончиться добром, особенно в вечном противостоянии вампирских кланов, где малейшее отличие от окружающих уже превращает вас во врага.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Сумерки*", parse_mode="Markdown")

# книги - День триффидов

            if call.message:
                if call.data == '3.7':
                    img = open('Day_Triffids.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2009\n*Страна* - Великобритания, Канада\n*Жанр* - ужасы, фантастика, боевик, триллер\n*Слоган* - «Когда мир погрузится во мрак»\n*Режиссер* - Ник Копус\n*Сценарий* - Патрик Харбинсон, Ричард Мьюис, Джон Уиндэм", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://ae.lordfilms-s.tv/14587-serial-den-triffidov-2009.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        После всеобщего наблюдения необычного астрономического явления — «звездопада» большая часть людей на Земле ослепла (за исключением тех, кто по какой-либо причине не смотрел на небо во время этого явления).", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*День триффидов*", parse_mode="Markdown")

# книги - Я – легенда

            if call.message:
                if call.data == '3.8':
                    img = open('I_legend.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2007\n*Страна* - США\n*Жанр* - фантастика, боевик, триллер, драма, приключения\n*Слоган* - «Последний человек на Земле не одинок»\n*Режиссер* - Френсис Лоуренс\n*Сценарий* - Марк Протосевич, Акива Голдсман, Джон Уильям Коррингтон", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://vk.com/im?peers=435813643_196125886_263374719_246227451&sel=396554871&z=video-209477587_456239959%2Fc08fc07d60e0c0bb24")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Неизвестный вирус унёс жизни половины населения земного шара, а остальную половину превратил в вампиров. Единственный уцелевший человек с иммунитетом к заболеванию ночами держит осаду упырей, а днем пытается найти противоядие и докопаться до причин эпидемии.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Я – легенда*", parse_mode="Markdown")

# книги - Война миров

            if call.message:
                if call.data == '3.9':
                    img = open('War_Worlds.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2005\n*Страна* - США\n*Жанр* - фантастика, боевик, приключения\n*Слоган* - «Они уже здесь»\n*Режиссер* - Стивен Спилберг\n*Сценарий* - Джош Фридман, Дэвид Кепп, Герберт Джордж Уэллс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://ae.lordfilms-s.tv/32247-film-vojna-mirov-2005.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Никто не поверил бы в начале 21 столетия, что за всем происходящим на Земле зорко и внимательно следят существа более развитые, чем человек; что в то время, как люди занимались своими делами, их исследовали и изучали.\n        С бесконечным самодовольством сновали люди по всему земному шару, занятые своими делишками, уверенные в своей власти над материей. А между тем через бездну пространства на Землю смотрели глазами полными зависти, существа с высокоразвитым, холодным, бесчувственным интеллектом, и медленно, но верно вырабатывали свои враждебные нам планы...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Война миров*", parse_mode="Markdown")

# книги - Властелин колец

            if call.message:
                if call.data == '3.10':
                    img = open('Lord_ Rings.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2001\n*Страна* - Новая Зеландия, США\n*Жанр* - фэнтези, приключения, драма\n*Слоган* - «Power can be held in the smallest of things...»\n*Режиссер* - Питер Джексон\n*Сценарий* - Фрэн Уолш, Филиппа Бойенс, Питер Джексон", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://vlastelin-kolets-online.ru/")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Сказания о Средиземье — это хроника Великой войны за Кольцо, длившейся не одну тысячу лет. Тот, кто владел Кольцом, получал неограниченную власть, но был обязан служить злу. \n        Тихая деревня, где живут хоббиты. Придя на 111-й день рождения к своему старому другу Бильбо Бэггинсу, волшебник Гэндальф начинает вести разговор о кольце, которое Бильбо нашел много лет назад. Это кольцо принадлежало когда-то темному властителю Средиземья Саурону, и оно дает большую власть своему обладателю. Теперь Саурон хочет вернуть себе власть над Средиземьем. Бильбо отдает Кольцо племяннику Фродо, чтобы тот отнёс его к Роковой Горе и уничтожил.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Властелин колец *", parse_mode="Markdown")

 
 
 
 
 
 
 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
   
   
   
   
   



# Веселое - Отпуск по обмену            
            if call.message:
                if call.data == '4.1':
                    img = open('otpusk-po-obmenu.jpg', 'rb')
                    bot.send_message(call.message.chat.id,"*Год производства* - 2006\n*Страна* - США \n*Жанр* - мелодрама, комедия\n*Слоган* - —\n*Режиссер* - Нэнси Майерс\n*Сценарий* - Нэнси Майерс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/28414-film-otpusk-po-obmenu-2006.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Айрис Симпкинс, автор популярной свадебной колонки в лондонской «Daily Telegraph», живет в очаровательном коттедже в английской провинции. Она влюблена в мужчину, который любит другую. Далеко от нее в Южной Калифорнии живет Аманда Вудс, владелица процветающего рекламного агентства, занимающегося созданием роликов для фильмов. Она вдруг обнаруживает, что любимый человек ей изменяет. \n        Две незнакомые друг с другом женщины, живущие на расстоянии 10 000 километров друг от друга, оказываются в схожей ситуации. И они находят друг друга. В Интернете, на сайте обмена жильем на время отпуска. Перед Рождеством Айрис и Аманда решают отдохнуть от своих проблем, договорившись поменяться континентами и пожить друг у друга в течение двух недель. Айрис переезжает в дом Аманды в солнечной Калифорнии, а Аманда приезжает в засыпанную снегом английскую провинцию…", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Отпуск по обмену*", parse_mode="Markdown")

# Веселое - Маска
            if call.message:
                if call.data == '4.2':
                    img = open('maska.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1994\n*Страна* - США \n*Жанр* - комедия, фэнтези, криминал\n*Слоган* - «Был никем - стал героем»\n*Режиссер* - Чак Рассел\n*Сценарий* - Майк Уэрб, Майкл Фэллон, Марк Верхайден", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/32142-film-maska-1994.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id,  "*Описание*\n        Скромный и застенчивый служащий банка чувствует себя неуверенно с красивыми девушками и вообще рядом с людьми. Волей судьбы к нему попадает волшебная маска, и Стенли Ипкис приобретает способность превращаться в неуязвимое мультяшное существо с озорным характером.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Маска*", parse_mode="Markdown")

# Веселое - Привет, Джули!
            if call.message:
                if call.data == '4.3':
                    img = open('privet-dzhuli.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2010\n*Страна* - США\n*Жанр* - драма, мелодрама, комедия\n*Слоган* - «You never forget your first love»\n*Режиссер* - Роб Райнер\n*Сценарий* - Роб Райнер, Эндрю Шайнмен, Вэнделин Ван Драанен", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/27416-film-privet-dzhuli-2010.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Джули Бейкер влюбляется в Брайса Лоски, однако девушка его не интересует. В старших классах Джули охладевает к Брайсу, однако парень, наоборот, начинает ею увлекаться.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*Привет, Джули!*", parse_mode="Markdown")

# Веселое - Мамма миа!

            if call.message:
                if call.data == '4.4':
                    img = open('mamma-mia.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2008\n*Страна* - США, Великобритания, Германия\n*Жанр* - мюзикл, мелодрама, комедия\n*Слоган* - «Добро пожаловать под венец»\n*Режиссер* - Филлида Ллойд\n*Сценарий* - Кэтрин Джонсон", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="https://id22.lordfilm.codes/7382-mamma-mia.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Молодая девушка Софи собирается выйти замуж и мечтает о том, чтобы церемония прошла по всем правилам. Она хочет пригласить на свадьбу своего отца, чтобы он отвел ее к алтарю. Но она не знает, кто он, так как ее мать Донна никогда не рассказывала о нем. \n        Софи находит дневник матери, в котором та описывает отношения с тремя мужчинами. Софи решает отправить приглашения всем троим! Все самое интересное начинает происходить, когда на свадьбу приезжают гости…", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*Мамма миа!*", parse_mode="Markdown")

# Веселое - Октябрьское небо

            if call.message:
                if call.data == '4.5':
                    img = open('oktjabrskoe-nebo.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1999\n*Страна* - США\n*Жанр* - драма, семейный, биография\n*Слоган* - «Фильм основан на реальных событиях»\n*Режиссер* - Джо Джонстон\n*Сценарий* - Льюис Колик, Гомер Х. Хикэм мл.", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/37609-film-oktjabrskoe-nebo-1999.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        В октябре 1957 года произошло событие эпохального значения. Советский Союз впервые в истории человечества запустил на земную орбиту первый «Спутник». Мир стал другим. \n        Запуск советской ракеты произвел неизгладимое впечатление на мальчика по имени Хомер Хикэм из небольшого шахтерского городка Колвуд в Западной Вирджинии. Всерьез «заболевший» космосом, Хомер решает построить собственную ракету. В этом ему начинают помогать трое друзей и школьная учительница. Однако отец Хомера, шахтер - работяга, видящий сына только в роли продолжателя своего нелегкого дела, категорически противится стремлениям своего ребенка. \n        Но, несмотря ни на что, мальчик сделает все возможное и невозможное, чтобы его мечта стала явью...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Октябрьское небо*", parse_mode="Markdown")

# Веселое - Хорошо быть тихоней

            if call.message:
                if call.data == '4.6':
                    img = open('horosho-byt-tihonej.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2012\n*Страна* - США\n*Жанр* - драма, мелодрама\n*Слоган* - «Будь фильтром, а не губкой!»\n*Режиссер* - Стивен Чбоски\n*Сценарий* - Стивен Чбоски", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/37797-film-horosho-byt-tihonej-2012.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        История о Чарли, ученике старшей школы в Питтсбурге, стеснительном и непопулярном. На наших глазах Чарли взрослеет, меняется круг его общения, меняется его мнение о мире.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Хорошо быть тихоней*", parse_mode="Markdown")

# Веселое - Между небом и землей

            if call.message:
                if call.data == '4.7':
                    img = open('mezhdu-nebom-i-zemlej.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2005\n*Страна* - США\n*Жанр* - фэнтези, драма, мелодрама, комедия\n*Слоган* - «Только любви все под силу»\n*Режиссер* - Марк Уотерс\n*Сценарий* - Питер Толан, Лесли Диксон, Марк Леви", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/37272-film-mezhdu-nebom-i-zemlej-2005.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Вселившись в арендованную квартиру в Сан-Франциско и начав наводить там порядок, Дэвид неожиданно встречает в своем новом жилище привлекательную молодую женщину Элизабет, которая уверяет его, что именно она является хозяйкой этих апартаментов. \n        Когда же Дэвид начинает склоняться к мысли, что произошло какое-то недоразумение, Элизабет исчезает так же внезапно и загадочно, как и появилась. Замена замков не останавливает красотку: ее таинственные появления и исчезновения продолжают вносить сумятицу в жизнь Дэвида. Убедившись в том, что она привидение, Дэвид старается помочь ей навсегда остаться в потустороннем мире. \n        Однако, открыв в себе невероятные возможности - например, способность проходить сквозь стены, - Элизабет начинает убеждать себя в том, что она каким-то образом еще жива и поэтому не собирается перебираться на тот свет насовсем. По мере того как оба пытаются выяснить истинную причину происходящего, Дэвид и Элизабет влюбляются друг в друга. Однако перспективы их совместной жизни становятся все более и более призрачными…", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Между небом и землей*", parse_mode="Markdown")

# Веселое - Семья напрокат

            if call.message:
                if call.data == '4.8':
                    img = open('semja-naprokat.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1997\n*Страна* - Канада\n*Жанр* - фэнтези, драма, мелодрама\n*Слоган* - —\n*Режиссер* - Тед Котчефф\n*Сценарий* - Памела Уоллес, Эрл У. Уоллес", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/28509-film-semja-naprokat-1997.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Кэтлин и ее семилетняя дочь Зои мечтают о собственном доме. И в канун Рождества они случайно знакомятся с Сэмом, богатым и симпатичным парнем, у которого «горит» сделка с мексиканским бизнесменом Ксавьером Дель Кампо, потому, что тот не любит холостяков. А Сэм, как назло, - холостяк. \n        И он предлагает Кэтлин и Зои изобразить за хорошую плату его семью. Все бы прошло «как по маслу», но Зои решила, что Ксавьер - ее ангел-хранитель, который вернет ей отца. Ангел ли Ксавьер на самом деле или нет, но Сэм и Кэтлин полюбили друг друга...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Семья напрокат*", parse_mode="Markdown")

# Веселое - 10 причин моей ненависти

            if call.message:
                if call.data == '4.9':
                    img = open('10-prichin-moej-nenavisti.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1999\n*Страна* - США\n*Жанр* - драма, мелодрама, комедия\n*Слоган* - «I pine, I perish!»\n*Режиссер* - Джил Джангер\n*Сценарий* - Карен МакКулла, Кирстен Смит, Уильям Шекспир", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/37694-film-10-prichin-moej-nenavisti-1999.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Строгий отец поставил условие: Бьянка пойдет на свидание, если ее сестра Кэт тоже согласится встретиться с парнем. Но Кэт — синий чулок и отчаянная мужененавистница. Бьянка пытается найти для сестры такого же зануду, как она.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*10 причин моей ненависти*", parse_mode="Markdown")

# Веселое - Тайная жизнь пчел

            if call.message:
                if call.data == '4.10':
                    img = open('tajnaja-zhizn-pchel.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2008\n*Страна* - США\n*Жанр* - драма\n*Слоган* - «Bring Your Girlfriends, Sisters, Mothers and Daughters»\n*Режиссер* - Джина Принс-Байтвуд\n*Сценарий* - Джина Принс-Байтвуд, Сью Монк Кидд", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/39194-film-tajnaja-zhizn-pchel-2008.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        1964 год. Лили Оуэнс потеряла мать и, будучи не в силах жить с отцом, сбегает из дома вместе со своей единственной подругой — Розалин — в городок в Южной Каролине.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Тайная жизнь пчел*", parse_mode="Markdown")
                



       
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------          


        
        
        
        
# Грустное - Мальчик в полосатой пижаме            
            if call.message:
                if call.data == '4.11':
                    img = open('malchik-v-polosatoj-pizhame.jpg', 'rb')
                    bot.send_message(call.message.chat.id,"*Год производства* - 2008\n*Страна* - Великобритания, США \n*Жанр* - драма, военный, история\n*Слоган* - «Взрослое детство войны»\n*Режиссер* - Марк Херман\n*Сценарий* - Марк Херман, Джон Бойн", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/33311-film-malchik-v-polosatoj-pizhame-2008.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        История, происходящая во время Второй мировой войны и показанная сквозь глаза невинного и ничего не подозревающего о происходящих событиях Бруно, восьмилетнего сына коменданта концентрационного лагеря. Его случайное знакомство и дружба с еврейским мальчиком по другую сторону ограды лагеря, в конечном счете, приводит к самым непредсказуемым и ошеломительным последствиям.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Мальчик в полосатой пижаме*", parse_mode="Markdown")

# Грустное - Хорошие дети не плачут
            if call.message:
                if call.data == '4.12':
                    img = open('horoshie-deti-ne-plachut.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2012\n*Страна* - Нидерланды \n*Жанр* - драма, семейный, спорт\n*Слоган* - —\n*Режиссер* - Деннис Ботс\n*Сценарий* - Карин ван Хольст Пеллекан, Жак Вринс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/43395-film-horoshie-deti-ne-plachut-2012.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id,  "*Описание*\n        Шестиклассница Акки настоящая хулиганка: она любит футбол, дерётся с мальчишками и ничего не боится. Ничего, кроме любви. Однако, когда ей ставят диагноз лейкемия, именно любовь дает ей силы бороться с болезнью и принять неизбежное.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Хорошие дети не плачут*", parse_mode="Markdown")

# Грустное - Дневник памяти
            if call.message:
                if call.data == '4.13':
                    img = open('dnevnik-pamjati.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2004\n*Страна* - США\n*Жанр* - драма, мелодрама\n*Слоган* - «За каждой большой любовью стоит большая история»\n*Режиссер* - Ник Кассаветис\n*Сценарий* - Джереми Левин, Ян Сарди, Николас Спаркс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/41621-film-dnevnik-pamjati-2004.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Это история отношений юноши и девушки из разных социальных слоев, живших в Южной Каролине. Ной и Элли провели вместе незабываемое лето, пока их не разделили вначале родители, а затем Вторая мировая война. \n        После войны все изменилось: Элли обручилась с удачливым бизнесменом, а Ной жил наедине со своими воспоминаниями в старинном доме, который ему удалось отреставрировать. Когда Элли прочла об этом в местной газете, она поняла: ей нужно найти его и решить наконец судьбу их любви...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*Дневник памяти*", parse_mode="Markdown")

# Грустное - До встречи с тобой

            if call.message:
                if call.data == '4.14':
                    img = open('do-vstrechi-s-toboj.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2016\n*Страна* - США, Великобритания\n*Жанр* - драма, мелодрама\n*Слоган* - «Live boldly»\n*Режиссер* - Теа Шэррок\n*Сценарий* - Джоджо Мойес", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/26145-film-do-vstrechi-s-toboj-2016.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Лу Кларк знает, сколько шагов от автобусной остановки до ее дома. Она знает, что ей очень нравится работа в кафе и что, скорее всего, она не любит своего бойфренда Патрика. Но Лу не знает, что вот-вот потеряет свою работу и что в ближайшем будущем ей понадобятся все силы, чтобы преодолеть свалившиеся на нее проблемы. \n        Уилл Трейнор знает, что сбивший его мотоциклист отнял у него желание жить. И он точно знает, что надо сделать, чтобы положить конец всему этому. Но он не знает, что Лу скоро ворвется в его мир буйством красок. И они оба не знают, что навсегда изменят жизнь друг друга.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*До встречи с тобой*", parse_mode="Markdown")

# Грустное - В метре друг от друга

            if call.message:
                if call.data == '4.15':
                    img = open('v-metre-drug-ot-druga.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2019\n*Страна* - США\n*Жанр* - драма, мелодрама\n*Слоган* - «When Life Keeps You Apart, Fight For Every Inch»\n*Режиссер* - Джастин Бальдони\n*Сценарий* - Микки Доутри, Тобиас Иаконис", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/58524-film-v-metre-drug-ot-druga-2019.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Пространство, в котором они существуют, диктует жестокое условие – влюбленные должны находиться не ближе метра друг от друга, им недоступно даже прикосновение. Но истинная любовь не знает границ, и чем сильнее чувства, тем больше соблазн нарушить правила…", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*В метре друг от друга*", parse_mode="Markdown")

# Грустное - Мост в Терабитию

            if call.message:
                if call.data == '4.16':
                    img = open('most-v-terabitiju.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2006\n*Страна* - США\n*Жанр* - фэнтези, драма, приключения, семейный\n*Слоган* - «Сказка становится реальностью»\n*Режиссер* - Габор Чупо\n*Сценарий* - Джефф Стокуэлл, Дэвид Патерсон, Кэтрин Патерсон", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/35044-film-most-v-terabitiju-2006.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Надежды ученика пятого класса Джесса Аарона стать самым быстрым бегуном в классе разбились после того, как новичок Лесли Берк одержала победу в соревнованиях. \n        Оснований для враждебности по отношению друг к друг у Джесса и Лесли более чем достаточно, и тем не менее между ними завязывается дружба. Как тут не подружиться, если приходится быть королем и королевой в обнаруженном в лесу волшебном царстве?", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Мост в Терабитию*", parse_mode="Markdown")

# Грустное - Куда приводят мечты

            if call.message:
                if call.data == '4.17':
                    img = open('kuda-privodjat-mechty.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1998\n*Страна* - США, Новая Зеландия\n*Жанр* - фэнтези, драма, мелодрама\n*Слоган* - «After life there is more. The end is just the beginning»\n*Режиссер* - Винсент Уорд\n*Сценарий* - Роналд Бэсс, Ричард Мэтисон", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/28503-film-kuda-privodjat-mechty-hd-1998.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        После гибели Криса Нилсена в автокатастрофе он, обретя бессмертие, пытается остаться рядом со своей прекрасной, но смертной женой Энни. С помощью дружественного духа, приставленного к нему в качестве проводника, он начинает привыкать к своему новому существованию в окружении, которое иначе как райским не назовешь. Но когда его обезумевшая от горя жена кончает жизнь самоубийством, ее проклинают и навечно изгоняют в ад. Крис изо всех сил пытается отыскать любимую, чтобы всегда быть с ней, но еще никому и никогда не удавалось спасти грешную душу от ужасного, но заслуженного возмездия. Благодаря помощи своих небесных друзей Крис отправляется в самое опасное и мучительное путешествие в своей жизни, точнее, в жизни после смерти.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Куда приводят мечты*", parse_mode="Markdown")

# Грустное - Виноваты звезды

            if call.message:
                if call.data == '4.18':
                    img = open('vinovaty-zvezdy.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2014\n*Страна* - США\n*Жанр* - драма, мелодрама\n*Слоган* - «История, покорившая миллионы женских сердец»\n*Режиссер* - Джош Бун\n*Сценарий* - Скотт Нойстедтер, Майкл Х. Уэбер, Джон Грин", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/41851-film-vinovaty-zvezdy-2014.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Хэйзел больна раком. Несмотря на то, что болезнь временно отступила, девушка не чувствует ни капли радости. Она ходит в группу поддержки, где однажды знакомится с Огастусом Уотерсом и моментально влюбляется в него. Огастус и Хэйзел отправляются в полное страсти и жизни путешествие, которое лишний раз покажет им, что весь смысл жизни можно найти в любом ее отрезке.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Виноваты звезды*", parse_mode="Markdown")

# Грустное - Я Кристина

            if call.message:
                if call.data == '4.19':
                    img = open('ja-kristina.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1981\n*Страна* - Германия (ФРГ)\n*Жанр* - драма, биография\n*Слоган* - «Наркотики... Проституция... Смерть?»\n*Режиссер* - Ули Эдель\n*Сценарий* - Герман Вайгель, Ули Эдель, Кай Херманн", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/29084-film-ja-kristina-1981.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Я Кристина. Мне 14 лет. Большинство моих друзей наркоманы. Первый раз я попробовала наркотики, чтобы понять, зачем их принимает мой парень... С тех пор прошло несколько месяцев. \n        Я устала каждый день искать дозу. Я и мой парень пробовали завязать... Трое моих знакомых уже умерли. Неужели я следующая?", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Я Кристина*", parse_mode="Markdown")

# Грустное - Класс

            if call.message:
                if call.data == '4.20':
                    img = open('klass.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2007\n*Страна* - Эстония\n*Жанр* - драма\n*Слоган* - «Я не умру вам назло…»\n*Режиссер* - Ильмар Рааг\n*Сценарий* - Ильмар Рааг, Валло Кирс, Пярт Уусберг", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://2022.filmhd1080.me/2374-film-klass-2007-smotret.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Обычная эстонская школа, выпускной класс. Парень по имени Йозеп постоянно терпит насмешки и издевательства со стороны одноклассников. Никогда не отвечая на выпады, он провоцирует их заходить в глупых «шутках» все дальше и дальше, до тех пор, пока за него не заступился один из бывших насмешников - Каспар. В классе начинается противостояние, которое постепенно накаляется, приближая неминуемую развязку...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Класс*", parse_mode="Markdown")
                



       
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------          


        
        
        
        
# Загадочное - Другие            
            if call.message:
                if call.data == '4.21':
                    img = open('drugie.jpg', 'rb')
                    bot.send_message(call.message.chat.id,"*Год производства* - 2001\n*Страна* - Испания, США, Франция, Италия \n*Жанр* - ужасы, триллер, детектив\n*Слоган* - «Рано или поздно они найдут тебя...»\n*Режиссер* - Алехандро Аменабар\n*Сценарий* - Алехандро Аменабар", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/31389-film-drugie-2001.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Грейс прячет своих детей в уединенном особняке на острове, где семейство дожидается окончания Второй мировой войны. Войны, с которой должен вернуться муж Грейс. \n        Её дочь и сын страдают странным заболеванием, они не выносят прямого дневного света. Когда в доме появляются трое новых слуг, им приходится соблюдать правила: все комнаты всегда должны быть в полумраке, и нельзя открывать дверь, пока не заперта предыдущая. Но мерному течению жизни дома вскоре приходит конец - некая потусторонняя сущность пытается нарушить заведённый порядок.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Другие*", parse_mode="Markdown")

# Загадочное - Знакомьтесь, Джо Блэк
            if call.message:
                if call.data == '4.22':
                    img = open('znakomtes-dzho-bljek.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1998\n*Страна* - США \n*Жанр* - мелодрама, фэнтези, драма\n*Слоган* - «Meet Joe Black: Sooner or Later Everyone Does»\n*Режиссер* - Мартин Брест\n*Сценарий* - Рон Осборн, Джефф Рино, Кевин Уэйд", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/41911-film-znakomtes-dzho-bljek-1998.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id,  "*Описание*\n        В жизни богатого и влиятельного газетного магната Уильяма Пэрриша появляется сама Смерть, принявшая обличье обворожительного молодого человека по имени Джо Блэк. \n        Смерть, уставшая от своих привычных обязанностей,предлагает Пэрришу необычное соглашение: магнат станет проводником Джо в мире живых, где тот планирует провести свой отпуск. По окончании каникул Смерть заберет Пэрриша с собой. С помощью Уильяма, загадочный и эксцентричный Джо начинает свое путешествие по бренной Земле. \n        Но происходит непредвиденное. Оказывается, что тело погибшего мужчины, которое Смерть выбрала для себя, принадлежало юноше, в которого была влюблена дочь Пэрриша.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Знакомьтесь, Джо Блэк*", parse_mode="Markdown")

# Загадочное - Дориан Грей
            if call.message:
                if call.data == '4.23':
                    img = open('dorian-grej.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2009\n*Страна* - Великобритания\n*Жанр* - фэнтези, триллер, драма\n*Слоган* - «Молодой навсегда. Проклятый навеки»\n*Режиссер* - Оливер Паркер\n*Сценарий* - Тоби Финлэй, Оскар Уайльд", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/33612-film-dorian-grej-2009.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Молодой и невероятно красивый Дориан Грей приезжает в Лондон и попадает под влияние искателя приключений лорда Уоттона. Он внушил юноше, что секрет успеха и счастья Дориана - в его красоте, ведь она поможет получить все удовольствия мира. Дориан заключает сделку с Дьяволом. Юноша заказывает свой портрет, и теперь вся грязь его жизни, полной распутства и преступных страстей, будет пачкать и портить полотно, его же собственное лицо останется вечно юным и прекрасным. \n        Проскитавшись по свету в поисках наслаждений 25 лет, Дориан возвращается на родину. Захваченный врасплох сильными чувствами, он впервые понял ценность взаимной любви. Но на пути к счастью железной преградой встало темное и загадочное прошлое Дориана...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*Дориан Грей*", parse_mode="Markdown")

# Загадочное - Тело

            if call.message:
                if call.data == '4.24':
                    img = open('telo.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2012\n*Страна* - Испания\n*Жанр* - триллер, детектив, криминал\n*Слоган* - «Смерть – не всегда конец»\n*Режиссер* - Ориол Паоло\n*Сценарий* - Ориол Паоло, Лара Сендим", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="https://w1.fullsee.site/movies/8815-telo/watch/ODgxNTo6MjY1NTA%3D/")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Автомобиль сбивает человека, в панике убегающего от кого-то или от чего-то. Прибывшие на место полицейские выясняют, что сбитый бедолага — ночной сторож из близлежащего морга. Так что так напугало несчастного? И куда делся из отсека №3 недавно привезенный в морг труп?", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*Тело*", parse_mode="Markdown")

# Загадочное - Сомния

            if call.message:
                if call.data == '4.25':
                    img = open('somnija.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2014\n*Страна* - США\n*Жанр* - ужасы, фэнтези, триллер, драма\n*Слоган* - «Кошмары станут реальностью»\n*Режиссер* - Майк Флэнеган\n*Сценарий* - Майк Флэнеган, Джефф Ховард", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="https://lf5.lordfilm.lu/10599-film-somnija-2016.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        У молодой пары, потерявшей маленького сына, появляется второй шанс на счастливую жизнь, когда они берут из приюта замечательного восьмилетнего Коди. По неизвестной им причине он очень боится засыпать по ночам, но вскоре оказывается, что дело в необычном даре Коди – пока он спит, его сны оживают. Каждую ночь новым родителям могут явиться либо прекрасные видения его воображения, либо леденящие душу порождения его кошмаров. ", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Сомния*", parse_mode="Markdown")

# Загадочное - Сонная лощина

            if call.message:
                if call.data == '4.26':
                    img = open('sonnaja-loschina.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1999\n*Страна* - США, Германия\n*Жанр* - триллер, фэнтези, ужасы, детектив\n*Слоган* - «Вы можете запереть двери. Вы можете закрыть окна. Но сможете ли вы пережить эту ночь?»\n*Режиссер* - Тим Бёртон\n*Сценарий* - Эндрю Кевин Уокер, Вашингтон Ирвинг, Кевин Ягер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="https://lf5.lordfilm.lu/3789-film-sonnaja-loschina-1999.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Нью-Йорк, 1799 год. Икабода Крэйна, молодого констебля, отправляют в местечко Сонная лощина для расследования загадочных убийств. Все жертвы, как сообщает местное население, погибают от меча всадника без головы. \n        Все они обезглавлены, а головы исчезли. Крэйну приходится убедиться, что это не легенда, а страшная правда. Становится очевидно, что убийца приходит с того света, что в преступлениях замешаны ведьмы и иная нечисть. Всадника нельзя убить пулей, всех смельчаков он побеждает в схватках. Но каковы мотивы злодеяний?..", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Сонная лощина*", parse_mode="Markdown")

# Загадочное - Ключ от всех дверей

            if call.message:
                if call.data == '4.27':
                    img = open('kljuch-ot-vseh-dverej.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2005\n*Страна* - США, Германия\n*Жанр* - ужасы, триллер, драма, детектив\n*Слоган* - «Fearing Is Believing»\n*Режиссер* - Иэн Софтли\n*Сценарий* - Эрен Крюгер", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/5656-film-kljuch-ot-vseh-dverej-2005.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        25-летняя Кэролайн Эллис устраивается работать сиделкой к пожилому инвалиду Бену Деверо, владельцу огромного особняка неподалеку от Луизианы. Его жена Вайолет вручает девушке универсальный ключ от всех дверей в доме. \n        Однажды Кэролайн обнаруживает на чердаке секретную комнату с массой мистических предметов. Хозяйка утверждает, что вещи принадлежат бывшим владельцам, которые занимались чёрной магией. Вскоре Кэролайн становится свидетельницей довольно странных и необъяснимых событий и решает во что бы то ни стало разгадать секрет таинственной комнаты.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Ключ от всех дверей*", parse_mode="Markdown")

# Загадочное - Знамение

            if call.message:
                if call.data == '4.28':
                    img = open('znamenie.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2009\n*Страна* - США, Великобритания, Австралия\n*Жанр* - фантастика, боевик\n*Слоган* - «Что будет, когда закончатся числа?»\n*Режиссер* - Алекс Пройас\n*Сценарий* - Райн Дуглас Пирсон, Джульетт Сноуден, Стайлз Уайт", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/6048-film-znamenie-2009.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        После вскрытия «временной капсулы», в которую в 1959 году группа школьников поместила рисунки со своим видением будущего, в руки к профессору Джону Кестлеру попадает загадочный лист, сверху до низу исписанный цифрами. В поисках расшифровки Кестлер устанавливает связь между цифрами и крупнейшими бедствиями, произошедшими на Земле за последние 50 лет. Если верить цифрам, трагедий не избежать и в будущем, только теперь Кестлер знает, когда их ожидать. ", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Знамение*", parse_mode="Markdown")

# Загадочное - Гоголь. Вий

            if call.message:
                if call.data == '4.29':
                    img = open('vie-gogol.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2018\n*Страна* - Россия\n*Жанр* - детектив, приключения, драма, ужасы, триллер\n*Слоган* - «Не выходи из круга»\n*Режиссер* - Егор Баранов\n*Сценарий* - Алексей Чупов, Наташа Меркулова, Николай Гоголь", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://vk.com/video?len=2&q=%D0%93%D0%BE%D0%B3%D0%BE%D0%BB%D1%8C.%20%D0%92%D0%B8%D0%B9&z=video-34462314_456239062%2Fpl_cat_trends")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Писарь из Санкт-Петербурга Николай Гоголь бросает вызов загадочному тёмному Всаднику, который жестоко расправляется с девушками в окрестностях села Диканька. Собрав команду из местного полицейского, пьяницы-доктора, суеверного кузнеца и странствующего философа-экзорциста, Гоголь пытается заманить злодея в ловушку, но на его пути встает самое жуткое порождение нечистой силы – Вий, один взгляд которого способен высосать душу смертного. Неожиданно для себя Гоголь выясняет, что с потусторонними силами его связывают не только таинственные видения.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Гоголь. Вий*", parse_mode="Markdown")

# Загадочное - Приют

            if call.message:
                if call.data == '4.30':
                    img = open('prijut.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2007\n*Страна* - Испания, Мексика\n*Жанр* - ужасы, триллер, драма, детектив\n*Слоган* - «Un cuento de amor. Una historia de terror»\n*Режиссер* - Хуан Антонио Байона\n*Сценарий* - Серхио Х. Санчес", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/35671-film-prijut-2007.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Самые счастливые годы Лаура провела в сиротском приюте на побережье. Любимые воспитатели заменили ей родителей, а друзья – братьев и сестер. Через тридцать лет Лаура возвращается в дом своего детства с мужем и семилетним сыном Симоном. Она мечтает восстановить его и открыть для новых маленьких посетителей. Однако в день открытия приюта обнаруживается, что Симон бесследно исчез. Лауре кажется, что дело в Томасе, вымышленном друге сына, с чьим призраком она столкнулась в день исчезновения.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Приют*", parse_mode="Markdown")
                



       
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------          


        
        
        
        
# Мотивирующее - Одержимость            
            if call.message:
                if call.data == '4.31':
                    img = open('oderzhimost.jpg', 'rb')
                    bot.send_message(call.message.chat.id,"*Год производства* - 2013\n*Страна* - США \n*Жанр* - драма, музыка\n*Слоган* - «The road to greatness can take you to the edge»\n*Режиссер* - Дэмьен Шазелл\n*Сценарий* - Дэмьен Шазелл", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://films-online-hd.xyzy.ru/38473-oderzhimost-2013.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Эндрю мечтает стать великим. Казалось бы, вот-вот его мечта осуществится. Юношу замечает настоящий гений, дирижер лучшего в стране оркестра. Желание Эндрю добиться успеха быстро становится одержимостью, а безжалостный наставник продолжает подталкивать его все дальше и дальше – за пределы человеческих возможностей. Кто выйдет победителем из этой схватки?", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Одержимость*", parse_mode="Markdown")

# Мотивирующее - Скрытые фигуры
            if call.message:
                if call.data == '4.32':
                    img = open('skrytye-figury.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2016\n*Страна* - США \n*Жанр* -  драма, биография, история\n*Слоган* - «У гениальности нет расы. У силы нет пола. У мужества нет границ»\n*Режиссер* - Тед Мелфи\n*Сценарий* - Эллисон Шредер, Тед Мелфи, Марго Ли Шеттерли", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="http://aj.lordfilms-s.tv/42824-film-skrytye-figury-2016.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id,  "*Описание*\n        Команда афроамериканок проводит для НАСА ряд математических вычислений, необходимых для запуска первой космической миссии.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Скрытые фигуры*", parse_mode="Markdown")

# Мотивирующее - Каждое воскресенье
            if call.message:
                if call.data == '4.33':
                    img = open('kazhdoe-voskresene.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 1999\n*Страна* - США\n*Жанр* - драма, спорт\n*Слоган* - «Play or be played»\n*Режиссер* - Оливер Стоун\n*Сценарий* - Оливер Стоун, Дэниэл Пайн, Джон Логан", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/40339-film-kazhdoe-voskresene-1999.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Сражения не кончаются на футбольном поле. Четыре года назад футбольная команда «Акулы Майами» находилась на гребне своего успеха. Но теперь их преследуют неудачи, и даже звезда «Акул» по прозвищу Кэп вынужден уйти. Главный тренер команды Тони Д`Амато - старый рыцарь спорта, переживающий вместе со своими ребятами все успехи и поражения, - сталкивается с новой проблемой.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*Каждое воскресенье*", parse_mode="Markdown")

# Мотивирующее - Не волнуйся, он далеко не уйдет

            if call.message:
                if call.data == '4.34':
                    img = open('ne-volnujsja-on-daleko-ne-ujdet.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2018\n*Страна* - Франция, США\n*Жанр* - драма, комедия, биография\n*Слоган* - «Don't just sit there. Do nothing»\n*Режиссер* - Гас Ван Сент\n*Сценарий* - Гас Ван Сент, Джек Гибсон, Уилльям Эндрю Итмэн", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/31096-film-ne-volnujsja-on-daleko-ne-ujdet-2018.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Джон не умел вовремя останавливаться, когда дело касалось быстрой езды, красивых женщин и опасных шуток. Прихватив случайного приятеля на вечеринке, он садится в машину и чудом остаётся в живых. С этого момента начинается горькая и вдохновляющая, правдивая и трогательная история человека, который потерял все, и вынужден двигаться дальше, чтобы обрести себя как одного из самых талантливых художников-карикатуристов Америки.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*Не волнуйся, он далеко не уйдет*", parse_mode="Markdown")

# Мотивирующее - В погоне за счастьем

            if call.message:
                if call.data == '4.35':
                    img = open('v-pogone-za-schastem.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2006\n*Страна* - США\n*Жанр* - драма, биография\n*Слоган* - «Никому не позволяй говорить, будто ты чего-то не можешь... У тебя есть мечта - защищай её»\n*Режиссер* - Габриэле Муччино\n*Сценарий* - Стивен Конрад", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/32486-film-v-pogone-za-schastem-2006.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Крис Гарднер – отец-одиночка. Воспитывая пятилетнего сына, Крис изо всех сил старается сделать так, чтобы ребенок рос счастливым. Работая продавцом, он не может оплатить квартиру, и их выселяют. \n        Оказавшись на улице, но не желая сдаваться, отец устраивается стажером в брокерскую компанию, рассчитывая получить должность специалиста. Только на протяжении стажировки он не будет получать никаких денег, а стажировка длится 6 месяцев...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*В погоне за счастьем*", parse_mode="Markdown")

# Мотивирующее - Человек, который изменил все

            if call.message:
                if call.data == '4.36':
                    img = open('chelovek-kotoryj-izmenil-vse.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2011\n*Страна* - США\n*Жанр* - биография, спорт, драма\n*Слоган* - «А что в жизни сделал ты?»\n*Режиссер* - Беннетт Миллер\n*Сценарий* - Стивен Зеллиан, Аарон Соркин, Стэн Червин", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="http://aj.lordfilms-s.tv/37371-film-chelovek-kotoryj-izmenil-vse-2011.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Фильм по книге Майкла M. Льюиса, изданной в 2003 году, об Оклендской бейсбольной команде и ее генеральном менеджере, Билли Бине. Его цель - создать конкурентоспособную бейсбольную команду, несмотря на финансовые трудности.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Человек, который изменил все*", parse_mode="Markdown")

# Мотивирующее - Я — Сэм

            if call.message:
                if call.data == '4.37':
                    img = open('ja-sjem.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2001\n*Страна* - США\n*Жанр* - драма\n*Слоган* - «Тебе нужна была любовь»\n*Режиссер* - Джесси Нельсон\n*Сценарий* - Кристин Джонсон, Джесси Нельсон", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://hd-23.lordfilm-s.me/16899-films-ja-sjem-2001.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Сэм Доусон, 40-летний мужчина с уровнем интеллекта 7-летнего ребёнка, работающий официантом. Ему трудно было бы выжить с такими данными, если бы не дочь, плод случайной связи. Люси выросла вполне нормальным человеком и могла бы заботиться о своём отце, но местная социальная служба забрала её у отца. Сэм хочет вернуть свою дочь. Для ведения этого дела он нанимает адвоката Риту Харрисон. По мере работы над этим делом Рита сама получает несколько уроков о том, что значит быть родителем...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Я — Сэм*", parse_mode="Markdown")

# Мотивирующее - 127 часов

            if call.message:
                if call.data == '4.38':
                    img = open('127-chasov.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2010\n*Страна* - Великобритания, США, Франция\n*Жанр* - триллер, биография, драма, приключения\n*Слоган* - «Важна каждая секунда»\n*Режиссер* - Дэнни Бойл\n*Сценарий* - Дэнни Бойл, Саймон Бофой, Арон Ральстон", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/8064-film-127-chasov-2010.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Неудержимый скалолаз и любитель спрятанных в каньонах пещер в очередной раз в одиночестве едет в горы и оказывается в смертельной ловушке. 127 часов без еды, без питья и практически без надежды выжить. Тут-то и проявляется сила характера…", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*127 часов*", parse_mode="Markdown")

# Мотивирующее - Серфер души

            if call.message:
                if call.data == '4.39':
                    img = open('serfer-dushi.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2011\n*Страна* - США\n*Жанр* - драма, спорт, биография, семейный\n*Слоган* - «When you come back from a loss, beat the odds, and never say never, you find a champion»\n*Режиссер* - Шон МакНамара\n*Сценарий* - Шон МакНамара, Дебора Шварц, Дуглас Шварц", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/8190-film-serfer-dushi-2011.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        С детства Бетани увлекалась серфингом, но в 13 лет у северного побережья Кауай на нее напала акула — девушка осталась без левой руки и чуть было не погибла. Но сила воли и настоящий характер сыграли свое дело — Бетани, несмотря ни на что, вновь встала на доску и начала принимать участие в соревнованиях на правах полностью здорового серфера.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Серфер души*", parse_mode="Markdown")

# Мотивирующее - Спасительный рассвет

            if call.message:
                if call.data == '4.40':
                    img = open('spasitelnyj-rassvet.webp', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2006\n*Страна* - США, Люксембург\n*Жанр* - биография, военный, драма, триллер\n*Слоган* - «Вырваться из ада!»\n*Режиссер* - Вернер Херцог\n*Сценарий* - Вернер Херцог", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/6074-film-spasitelnyj-rassvet-2006.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Немец Дитер Денглер, летчик ВМФ США во время войны во Вьетнаме, был сбит над Лаосом и попал в плен. Вместе с группой пленных Дитер организовывает побег.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Спасительный рассвет*", parse_mode="Markdown")
                



       
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------          


        
        
        
        
# Романтичное - 365 дней            
            if call.message:
                if call.data == '4.41':
                    img = open('365-dnej.webp', 'rb')
                    bot.send_message(call.message.chat.id,"*Год производства* - 2020\n*Страна* - Польша\n*Жанр* - мелодрама\n*Слоган* - —\n*Режиссер* - Барбара Бяловас, Томаш Мандес\n*Сценарий* - Blanka Lipinska, Tomasz Klimala, Томаш Мандес", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lf5.lordfilm.lu/2318-film-365-dnej-2020.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Массимо Торичелли - молодой красивый босс сицилийской мафиозной семьи. После убийства отца конкурентами он вынужден взять на себя его обязанности. Лаура Бель - директор по продажам в роскошном отеле. Она успешна в профессии, но в личной жизни ей не хватает страсти. Лаура делает последнюю попытку сохранить отношения. Вместе с женихом и друзьями она летит на Сицилию, где её похищает Массимо и даёт ей 365 дней, чтобы Лаура его полюбила.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*365 дней*", parse_mode="Markdown")

# Романтичное - После
            if call.message:
                if call.data == '4.42':
                    img = open('posle.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2019\n*Страна* - США \n*Жанр* - мелодрама\n*Слоган* - «Твоя жизнь не будет прежней»\n*Режиссер* - Дженни Гейдж\n*Сценарий* - Сьюзэн МакМартин, Tamara Chestna, Дженни Гейдж", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://y2.lordfilms.fund/filmy/83090-posle-2019.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id,  "*Описание*\n        Будущее. Деспотичное государство ежегодно устраивает показательные игры на выживание, за которыми в прямом эфире следит весь мир. Жребий участвовать в Играх выпадает юной Китнисс и тайно влюбленному в нее Питу. Они знакомы с детства, но теперь должны стать врагами. Ведь по нерушимому закону Голодных игр победить может только один из 24 участников. Судьям не важно кто выиграет, главное - зрелище. И на этот раз зрелище будет незабываемым.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*После*", parse_mode="Markdown")

# Романтичное - Секретарша
            if call.message:
                if call.data == '4.43':
                    img = open('sekretarsha.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2001\n*Страна* - США\n*Жанр* - драма, мелодрама, комедия\n*Слоган* - «Assume the position»\n*Режиссер* - Стивен Шейнберг\n*Сценарий* - Эрин Крессида Уилсон, Мэри Гейтскилл, Стивен Шейнберг", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="https://lo1.lordsfilm.win/3020-sekretarsha-film-2002.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Ли Холловэй возвращается в родной город. Она страдает небольшими отклонениями в поведении, однако это не мешает ей устроиться на работу секретарём к местному юристу мистеру Грэю. Поначалу работа кажется Ли вполне обычной, пока мистер Грэй не замечает у неё проблем с грамматикой и не решает исправить их своими особыми методами.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*Секретарша*", parse_mode="Markdown")

# Романтичное - Будка поцелуев

            if call.message:
                if call.data == '4.44':
                    img = open('budka-poceluev.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2018\n*Страна* - США, Великобритания\n*Жанр* - мелодрама, комедия\n*Слоган* - «She can tell her best friend anything. Except this one thing»\n*Режиссер* - Винс Марчелло\n*Сценарий* - Винс Марчелло, Бет Риклз", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="https://lo1.lordsfilm.win/23478-budka-poceluev-film-2018.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Старшеклассница Эль - общительная, милая, но еще не испытавшая прелести поцелуев девушка. Ной – старший брат ее лучшего друга - дерзкий и ветреный, разбивший не одно девичье сердце. Решив однажды поучаствовать в «Будке поцелуев» на осеннем карнавале, Эль даже представить не могла, что подарит свой первый поцелуй Ною, и её жизнь изменится до неузнаваемости.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text="*Будка поцелуев*", parse_mode="Markdown")

# Романтичное - Предложение

            if call.message:
                if call.data == '4.45':
                    img = open('predlozhenie.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2009\n*Страна* - США\n*Жанр* - мелодрама, комедия, драма\n*Слоган* - «Горько?.»\n*Режиссер* - Энн Флетчер\n*Сценарий* - Пит Чиарелли", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="https://lo1.lordsfilm.win/12031-predlozhenie-film-2009.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Главная героиня фильма – ответственная начальница, которой грозит высылка в Канаду. Ради того, чтобы избежать ссылки в край озер, героиня готова на все – даже фиктивно выскочить замуж за своего молодого ассистента...", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Предложение*", parse_mode="Markdown")

# Романтичное - Звезда родилась

            if call.message:
                if call.data == '4.46':
                    img = open('zvezda-rodilas.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2018\n*Страна* - США\n*Жанр* - мелодрама, музыка, драма\n*Слоган* - —\n*Режиссер* - Брэдли Купер\n*Сценарий* - Эрик Рот, Брэдли Купер, Уилл Феттерс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма",  url="https://lo1.lordsfilm.win/14026-zvezda-rodilas-film-2018.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Кантри-музыкант Джексон Мейн, чья карьера быстро катится под откос, однажды знакомится с никому не известной талантливой певицей Элли. Между героями вспыхивает страстный роман. Джек помогает Элли добиться успеха. Но чем стремительнее набирает обороты музыкальная карьера Элли, тем сложнее ему мириться со своей увядающей славой.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Звезда родилась*", parse_mode="Markdown")

# Романтичное - Тепло наших тел

            if call.message:
                if call.data == '4.47':
                    img = open('teplo-nashih-tel.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2013\n*Страна* - США, Канада\n*Жанр* - ужасы, мелодрама, комедия\n*Слоган* - «Он всё ещё мёртв, но сердце снова бьётся»\n*Режиссер* - Джонатан Левин\n*Сценарий* - Джонатан Левин, Айзек Марион", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lo1.lordsfilm.win/14440-teplo-nashih-tel-film-2013.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Мир поражен чумой и стоит на грани вымирания. Покойники ходят по земле и норовят употребить в пищу живых, которые, оставшись в катастрофическом меньшинстве, с трудом держат оборону. Перемены начинаются, когда один зомби, чье имя при жизни начиналось на «Р», спасает девушку вместо того, чтобы ее съесть. Дружба, завязавшаяся между представителями враждующих сторон, грозит обоим самыми нехорошими последствиями. Но Р и Джули, сами того не подозревая, держат в руках простой и единственный ключ к спасению гибнущего мира.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Тепло наших тел*", parse_mode="Markdown")

# Романтичное - Пятьдесят оттенков серого

            if call.message:
                if call.data == '4.48':
                    img = open('pjatdesjat-ottenkov-serogo.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2015\n*Страна* - США\n*Жанр* - мелодрама\n*Слоган* - «Мистер Грей ждет вас»\n*Режиссер* - Сэм Тейлор-Джонсон\n*Сценарий* - Келли Марсел, Э.Л. Джеймс", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lo1.lordsfilm.win/17134-pjatdesjat-ottenkov-serogo-film-2015.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Анастейша Стил — скромная студентка, живущая вместе с близкой подругой-сокурсницей Кейт. За неделю до выпускного в университете Анастейша, по просьбе заболевшей Кейт заменить её, берёт интервью у молодого красавца-миллиардера Кристиана Грея. Интервью складывается не очень удачно, и Анастейша не думает, что они когда-либо встретятся вновь. Неожиданно Грей появляется в хозяйственном магазине, где девушка работает продавцом. Их знакомство продолжается, и Анастейша постепенно узнаёт о тайных сексуальных увлечениях богача.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Пятьдесят оттенков серого*", parse_mode="Markdown")

# Романтичное - Золушка

            if call.message:
                if call.data == '4.49':
                    img = open('zolushka.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2015\n*Страна* - США, Великобритания\n*Жанр* - фэнтези, драма, мелодрама, приключения, семейный\n*Слоган* - «Midnight is just the beginning»\n*Режиссер* - Кеннет Брана\n*Сценарий* - Крис Вайц, Шарль Перро", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://lo1.lordsfilm.win/14822-zolushka-film-2015.html")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        Отец молодой девушки по имени Элла, овдовев, женится во второй раз, и вскоре Элла оказывается один на один с жадными и завистливыми новыми родственницами – мачехой Леди Тремэйн и ее дочерьми - Анастасией и Дризеллой. Из хозяйки дома она превращается в служанку, вечно испачканную золой, за что и получает от своих сварливых сводных сестриц прозвище – Золушка. \n        Несмотря на злоключения, выпавшие на ее долю, Золушка не отчаивается, ведь даже в самые тяжелые моменты находится что-то, что помогает ей думать о хорошем: например, случайная встреча на лесной тропинке с прекрасным юношей. Элла даже не предполагает, что встретилась с самим принцем и что вскоре Фея-крестная навсегда поменяет её жизнь к лучшему.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Золушка*", parse_mode="Markdown")

# Романтичное - Он - дракон

            if call.message:
                if call.data == '4.50':
                    img = open('on-drakon.jpg', 'rb')
                    bot.send_message(call.message.chat.id, "*Год производства* - 2015\n*Страна* - Россия\n*Жанр* - фэнтези\n*Слоган* - «Любить страшно»\n*Режиссер* - Индар Джендубаев\n*Сценарий* - Марина Дяченко, Сергей Дяченко, Индар Джендубаев", parse_mode="Markdown")
                    bot.send_photo(call.message.chat.id, img)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Перейти к просмотру фильма", url="https://www.lordfilm-smotret.one/47969-on-drakon-film-2015-09")
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, "*Описание*\n        В разгар свадьбы княжну Мирославу похищает дракон, унося в свой замок на острове. В прошлом остались родные, жених, теперь только каменный плен в компании прекрасного Армана. Но кто он, и как оказался на острове? Мира поймет это слишком поздно: любовь к нему, человеку-дракону, откроет ей горькую истину – любить страшно.", reply_markup=markup, parse_mode="Markdown")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Он - дракон*", parse_mode="Markdown")












        except Exception as e:
            print(repr(e))
