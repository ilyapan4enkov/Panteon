import telebot
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot('6228753482:AAGwMoZ0g6NPjbiRjFbjM_G-Xgi0ptYvLpo')

smile=u'U+1F603'

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    start_image = open('/home/user/Рабочий стол/panteon/2023-03-27_10-56_1.png', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_kurs = types.KeyboardButton("Найти курс")
    markup.add(btn_kurs)
    bot.send_sticker(message.chat.id, start_image)
    bot.send_message(message.chat.id, text="Приветствуем в Пантеоне!😉\nЭто бот, который поможет тебе быстро выбрать курс, исходя из твоих требований.\nДля этого тебе нужно пройти небольшое анкетирование👇",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    age_image = open('/home/user/Рабочий стол/panteon/2023-03-26_20-18.png', 'rb')
    # Получение сообщений от юзера
    if message.text == "Найти курс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_klass9 = types.KeyboardButton("5-9 классы")
        btn_klass4 = types.KeyboardButton("1-4 классы")
        btn_klass11 = types.KeyboardButton("10-11 классы")
        markup.add(btn_klass4, btn_klass9, btn_klass11)
        bot.send_sticker(message.chat.id, age_image)
        bot.send_message(message.from_user.id, text="Выберите интересующую возрастную группу👨‍👩‍👧‍👦", reply_markup=markup)
    if (message.text == "1-4 классы") or (message.text == "5-9 классы") or (message.text == "10-11 классы"):
        global klass4
        global klass9
        global klass11
        klass4 = 0
        klass9 = 0
        klass11 = 0
        if message.text == "1-4 классы":
            klass4 = 1
        if message.text == "5-9 классы":
            klass9 = 1
        if message.text == "10-11 классы":
            klass11 = 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_predmet_fin = types.KeyboardButton("Финансы")
        btn_predmet_prog = types.KeyboardButton("Программирование")
        btn_predmet_angl = types.KeyboardButton("Английский язык")
        if klass4 == 0:
            btn_predmet_egeoge = types.KeyboardButton("Подготовка к ОГЭ или ЕГЭ")
        btn_predmet_dis = types.KeyboardButton("Дизайн")
        if klass4 == 0:
            markup.add(btn_predmet_prog, btn_predmet_angl, btn_predmet_fin, btn_predmet_egeoge, btn_predmet_dis)
        else:
            markup.add(btn_predmet_prog, btn_predmet_angl, btn_predmet_fin, btn_predmet_dis)
        napr_image = open('/home/user/Рабочий стол/panteon/2023-03-26_20-16_1.png', 'rb')
        bot.send_sticker(message.chat.id, napr_image)
        bot.send_message(message.from_user.id, text="Какое направление вас интересует?↕↔", reply_markup=markup)
    if message.text == "Финансы" or message.text == "Программирование" or message.text == "Английский язык" or message.text == "Подготовка к ОГЭ или ЕГЭ" or message.text == "Дизайн":
        if message.text == "Программирование":
            if klass4 == 1:
                url_kurs = 'https://ru.kodland.org/courses/scratch?utm_medium=cpa&utm_source=affise&utm_campaign=Sravni&utm_content=7&utm_term=%7Bclick_id%7D'
                url_kurs2 = 'https://ru.kodland.org/courses/roblox?utm_medium=cpa&utm_source=affise&utm_campaign=Sravni&utm_content=7&utm_term=%7Bclick_id%7D'
                text_kurs = 'Программирование в скретч и базовые алгоритмы создания игр и мультфильмов. Среда Scratch идеально подходит детям в возрасте 8+ лет, чтобы начать изучение IT мира с нуля. Рейтинг 4/5:'
                text_kurs2 = 'Изучение LUA в среде разработки Roblox Studio. Это программа для детей 10+ лет, которые никогда не создавали игры, но хотели бы научиться это делать. Рейтинг 3/5:'
            elif klass9 == 1:
                url_kurs = 'https://productstar.ru/dev-course-java?utm_source=rating&utm_medium=cpa&utm_campaign=dev-prof-java-landing&utm_term=sravni&utm_content=01-2023&click_id=102d7690c74414d691a3180f36e3d6'
                url_kurs2 = 'https://sky.pro/courses/programming/python-web-course?utm_source=advcake&utm_medium=cpa&utm_campaign=n'
                text_kurs = 'Вы научитесь программировать с нуля на самом популярном языке программирования Java, добавите сильные проекты к себе в портфолио и станете востребованным специалистом для любой Digital-компании(Выгодно!). Рейтинг 5/5:'
                text_kurs2 = 'Python —разработчик. Рейтинг 3.5/5: '
            else:
                url_kurs = 'https://skillbox.ru/course/profession-testing-automation-engineer/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=e180b2d0&utm_term=dd8cfc73fbbc9e27924fab6ef5cd7879&advcake_params=dd8cfc73fbbc9e27924fab6ef5cd7879&sub1=ga_183640537.1679829519'
                url_kurs2 = 'https://skillfactory.ru/devops-engineer?utm_source=infopartners&utm_medium=cpa&utm_campaign=sravni&utm_content=devops&utm_term=1025823eb5c4b57ce33259de3b06db'
                text_kurs = 'Вы с нуля освоите Java, JavaScript или Python и научитесь создавать автотесты на одном из этих языков. Познакомитесь с Selenium, повысите эффективность работы с помощью CI/CD и вырастете как QA-инженер. Рейтинг 4/5:'
                text_kurs2 = 'Обучение DevOps(Выгодно!). Рейтинг 5/5:'
        if message.text == "Английский язык":
            if klass4 == 1:
                url_kurs = 'https://skyeng.ru/besplatnye-kursy-anglijskogo-yazyka?utm_source=advcake&utm_medium=web_site&utm_campaign=e180b2d0&utm_content=affiliate&advcake_params=285d7ca5a850eb338a1d10ce4f171592&source_type=cpa_network&utm_term=285d7ca5a850eb338a1d10ce4f171592&workflow=adults&sub1=ga_183640537.1679829519%7Cym_1679829519990870879&sub2=%2Fkursy%2Finostrannye-yazyki%2F&sub4=Skyeng%7C%D0%91%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D1%8B%D0%B5%20%D0%BA%D1%83%D1%80%D1%81%D1%8B%20%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE&sub5=%D0%9A%D1%83%D1%80%D1%81%D1%8B&keyword=search%7Cposition_5'
                url_kurs2 = 'https://eng.skillbox.ru/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=e180b2d0&advcake_params=5f367dc6d012bd792cf4aac4522b39b7&utm_term=5f367dc6d012bd792cf4aac4522b39b7&sub1=ga_183640537.1679829519'
                text_kurs = 'Бесплатные курсы по английскому языку.\nДля начинающих и не только. Рейтинг 3.5/5:'
                text_kurs2 = 'Повышение уровня английского языка (до уровня А1). Выгодно! Рейтинг 5/5:'
            elif klass9 == 1:
                url_kurs = 'https://skyeng.ru/besplatnye-kursy-anglijskogo-yazyka?utm_source=advcake&utm_medium=web_site&utm_campaign=e180b2d0&utm_content=affiliate&advcake_params=285d7ca5a850eb338a1d10ce4f171592&source_type=cpa_network&utm_term=285d7ca5a850eb338a1d10ce4f171592&workflow=adults&sub1=ga_183640537.1679829519%7Cym_1679829519990870879&sub2=%2Fkursy%2Finostrannye-yazyki%2F&sub4=Skyeng%7C%D0%91%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D1%8B%D0%B5%20%D0%BA%D1%83%D1%80%D1%81%D1%8B%20%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE&sub5=%D0%9A%D1%83%D1%80%D1%81%D1%8B&keyword=search%7Cposition_5'
                url_kurs2 = 'https://eng.skillbox.ru/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=e180b2d0&advcake_params=5f367dc6d012bd792cf4aac4522b39b7&utm_term=5f367dc6d012bd792cf4aac4522b39b7&sub1=ga_183640537.1679829519'
                text_kurs = 'Бесплатные курсы по английскому языку.\nДля начинающих и не только. Рейтинг 3.5/5:'
                text_kurs2 = 'Повышение уровня английского языка (до уровня А1). Выгодно! Рейтинг 5/5:'
            else:
                url_kurs = 'https://practicum.yandex.ru/english/landing/english_for_career/?utm_source=partners&utm_medium=sravni&utm_campaign=partners_sravni_english_for_career'
                url_kurs2 = 'https://skyeng.ru/programs/razgovornyj-anglijskij?utm_source=advcake&utm_medium=web_site&utm_campaign=e180b2d0&utm_content=affiliate&advcake_params=a0eb6632c566a06db766ad43d04da31a&source_type=cpa_network&utm_term=a0eb6632c566a06db766ad43d04da31a&workflow=adults&sub1=ga_183640537.1679829519%7Cym_1679829519990870879&sub2=%2Fkursy%2Finostrannye-yazyki%2F&sub4=Skyeng%7C%D0%A0%D0%B0%D0%B7%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D0%BD%D1%8B%D0%B9%20%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9%20(%D0%9F%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC)&sub5=%D0%9A%D1%83%D1%80%D1%81%D1%8B&keyword=search%7Cposition_5'
                text_kurs = 'Курс для тех,кто хочет работать в международной Компании. Рейтинг 4/5:'
                text_kurs2 = 'Курс «JustSpeak» — разговорный английский язык. Рейтинг 5/5: :'
        if message.text == "Финансы":
            if klass4 == 1:
                url_kurs = 'https://coddyschool.com/courses/finansovaya_gramotnost/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=e180b2d0&utm_partner=adv.cake&advcake_params=b355d718ecb5389e50969b60068283da&utm_term=b355d718ecb5389e50969b60068283da&sub1=ga_183640537.1679829519'
                url_kurs2 = 'https://coddyschool.com/courses/finansovaya_gramotnost/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=e180b2d0&utm_partner=adv.cake&advcake_params=b355d718ecb5389e50969b60068283da&utm_term=b355d718ecb5389e50969b60068283da&sub1=ga_183640537.1679829519'
                text_kurs = 'Финансовая грамотность для детей. Рейтинг 4/5:'
                text_kurs2 = 'Как обращаться с деньгами школьникам начальных классов. Рейтинг 5/5:'
            elif klass9 == 1:
                url_kurs = 'https://eduson.academy/fin-analyst?utm_source=cpa&utm_medium=sravni_ru&utm_campaign=cpa&click_id=102e0695909320882f5d98da927de0'
                url_kurs2 = 'https://skillbox.ru/course/profession-accountant-basic/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=e180b2d0&utm_term=0e7399fc6c4e4e75bdf8c145df0782dc&advcake_params=0e7399fc6c4e4e75bdf8c145df0782dc&sub1=ga_183640537.1679829519'
                text_kurs = 'Практический онлайн-курс, где вы за 2-3 месяца с нуля научитесь анализировать финансовую отчетность, оценивать финансовое состояние компании, составлять прогнозы,строить финансовые модели. Сможете быстро найти перспективную работу в финансах или претендовать на повышение. Рейтинг 3.5/5:'
                text_kurs2 = 'Вы с нуля научитесь вести бухучёт по российским стандартам и работать в 1С,готовить налоговую отчётность и рассчитывать зарплату. Сможете начать карьеру бухгалтера в России или получить повышение. Рейтинг 4.5/5:'
            else:
                url_kurs = 'https://skillbox.ru/course/profession-accountant-basic/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=e180b2d0&utm_term=0e7399fc6c4e4e75bdf8c145df0782dc&advcake_params=0e7399fc6c4e4e75bdf8c145df0782dc&sub1=ga_183640537.1679829519'
                url_kurs2 = 'https://skillbox.ru/course/trading-customtariffs/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=e180b2d0&utm_term=150a3309c8b112e5dfd19da7f4b9d2d2&advcake_params=150a3309c8b112e5dfd19da7f4b9d2d2&sub1=ga_183640537.1679829519'
                text_kurs = 'Профессия в сфере финансов с серьезными перспективами трудоустройства. Рейтинг 4/5:'
                text_kurs2 = 'Вы научитесь торговать на финансовых рынках и контролировать риски. Создадите собственную стратегию торговли и сможете совершать обдуманные сделки. Рейтинг 5/5:'
        if message.text == "Подготовка к ОГЭ или ЕГЭ":
            if klass9 == 1:
                url_kurs = 'https://umschool.net/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=e180b2d0&advcake_params=cdc37c359eced57eada22da2e757986b&utm_term=cdc37c359eced57eada22da2e757986b&sub1=ga_183640537.1679829519'
                url_kurs2 = 'https://foxford.ru/courses/8316/landing?utm_source=admitad&utm_medium=cpa&utm_campaign=gen_all_all_common-regular&placement=1718520&admitad_uid=a7750d314a9cc9f2074160238c6d12cd'
                text_kurs = 'Подготовка к ОГЭ. Рейтинг 4/5:'
                text_kurs2 = 'Подготовка к итоговому собеседованию 2023 по русскому языку. Рейтинг 5/5:'
            else:
                url_kurs = 'https://tetrika-school.ru/menu-ege?utm_source=affiliate&utm_medium=cpa&utm_campaign=sravni&utm_content=id'
                url_kurs2 = 'https://umschool.net/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=e180b2d0&advcake_params=cdc37c359eced57eada22da2e757986b&utm_term=cdc37c359eced57eada22da2e757986b&sub1=ga_183640537.1679829519'
                text_kurs = 'Подготовка к ЕГЭ. Рейтинг 4.5/5:'
                text_kurs2 = 'Подготовка к ЕГЭ. Рейтинг 4/5:'
        if message.text == "Дизайн":
            if klass4 == 1:
                url_kurs = 'https://gb.ru/courses/geek-school/web-design?utm_source=aff&utm_medium=cpa&utm_campaign=aff_cpa_affiliate&utm_content=e180b2d0&utm_term=132082df558c0e1cd876dd3bfe746a8d&sub1=ga_183640537.1679829519'
                url_kurs2 = 'https://gb.ru/courses/geek-school/3d?utm_source=aff&utm_medium=cpa&utm_campaign=aff_cpa_affiliate&utm_content=e180b2d0&utm_term=39a832df41c668f59a4183ada0ddd895&sub1=ga_183640537.1679829519'
                text_kurs = 'Веб дизайн для детей. Рейтинг 3.5/5:'
                text_kurs2 = '3D-моделирование для детей. Рейтинг 4.5/5:'
            elif klass9 == 1:
                url_kurs = 'https://eduson.academy/web-designer?utm_source=cpa&utm_medium=sravni_ru&utm_campaign=cpa&click_id=102e0695909320882f5d98da927de0'
                url_kurs2 = 'https://productstar.ru/product-mini-course-figma?source_type=partners&utm_source=rating&utm_medium=cpa&utm_campaign=product-mini&utm_term=sravni&utm_content=july&click_id=102d7690c74414d691a3180f36e3d6'
                text_kurs = 'Веб-дизайн старт карьеры на удаленке. Рейтинг 5/5:'
                text_kurs2 = 'Основы продуктового дизайна с помощью FIGMA. Рейтинг 3.5/5:'
            else:
                url_kurs = 'https://contented.ru/edu/interactive-media-design?utm_source=infopartners&utm_medium=cpa&utm_campaign=sravni&utm_content=media&utm_term=%7Btransaction_id%7D'
                url_kurs2 = 'https://skillbox.ru/course/render/?utm_source=advcake&utm_medium=cpa&utm_campaign=affiliate&utm_content=e180b2d0&utm_term=067f853df10ac48f2314d05db06ba8fa&advcake_params=067f853df10ac48f2314d05db06ba8fa&sub1=ga_183640537.1679829519'
                text_kurs = 'Дизайнер интерактивных медиа. Рейтинг 4/5:'
                text_kurs2 = 'Рендер с нуля. Рейтинг 4.5/5:'
        markup = types.InlineKeyboardMarkup()
        markup2 = types.InlineKeyboardMarkup()
        end_image = open('/home/user/Рабочий стол/panteon/2023-03-26_20-28.png', 'rb')
        bot.send_sticker(message.chat.id, end_image)
        btn_kurs = types.InlineKeyboardButton("Ссылка на 1 курс👇", url=url_kurs)
        btn_kurs2 = types.InlineKeyboardButton("Ссылка на 2 курс👇", url=url_kurs2)
        markup.add(btn_kurs)
        markup2.add(btn_kurs2)
        a = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_start = types.KeyboardButton("/start")
        a.add(btn_start)
        bot.send_message(message.from_user.id, 'Мы подобрали для вас курсы:', reply_markup=a)
        bot.send_message(message.from_user.id, text=text_kurs, reply_markup=markup)
        bot.send_message(message.from_user.id, text=text_kurs2, reply_markup=markup2)


# Запускаем бота
bot.polling(none_stop=True, interval=0)