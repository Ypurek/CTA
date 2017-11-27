from core import processing
import datetime, random
from django.contrib.auth.models import User
from core.models import UserFeature, Feature

descriptions = ('Увидеть живого белого слона и всемирно известный аттракцион иллюзий, который объездил почти весь мир. '
                'Насладиться полетами призеров Международного фестиваля воздушных гимнастов. Стать свидетелями '
                'сенсационного представления от лучшего жонглера мира, а также вас ждут выступления фокусников, '
                'клоунов, глотателей огня... и буря незабываемых эмоций!',

                'Бурые медведи на велосипедах, прыгающие сквозь огонь собаки, трюки без страховки прямо под куполом '
                'цирка от призеров крупнейших фестивалей цирка, захватывающие дух акробатические номера и чудесные '
                'перевоплощения, выступление талантливого итальянского укротителя Эммануэля Фарины с львами и тиграми…',

                'Аргонавты - яркое и красочное театрально-цирковое шоу по мотивам знаменитой древнегреческой легенды о '
                'путешествии мореплавателей корабля Арго за золотым руном. Предводимые мужественным Ясоном, '
                'аргонавты должны возвратить в Грецию священную реликвию. На пути героям встречаются прекрасные '
                'женщины, мудрые кентавры, огненные быки и полчища врагов. В программе шоу: воздушные гимнасты, '
                'вравщающиеся на огненных кубах, акробаты, выполняющие трюки на высоте 15 метров, хореографические '
                'сцены с участием профессиональных танцоров знаменитых школ Тодес и Дункан.',

                'Сегодня и только сегодня можно увидеть танцующего слона под самым куполом цирка. Насладиться fireshow '
                'от лучших мировых артистов. Также в программе смертельнве трюки гимнастов на ремнях, где нельзя '
                'ошибится. И конечно же весёлый клоун, который не оставит равнодушным ни единого ребёнка и взрослого! '
                )
features = ('cat', 'mouse', 'parrot', 'clown')


# test data for debug for 1 week
def add_tickets():
    for i in range(7):
        date = datetime.date.today() + datetime.timedelta(days=1 + i)
        for i in range(12):
            time = datetime.time(hour=10 + i)
            description = random.choice(descriptions)
            feature = random.choices(features, k=random.randint(0,2))
            perf = processing.add_performance(date, time, 100, 'new perf', description, feature)
            processing.add_tickets(perf, random.randint(100,300), number=random.randint(10,30))


def set_settings():
    processing.set_app_property('max_book_ticket', '10')
    #processing.set_app_property('max_buy_ticket', '10')
    processing.set_app_property('user_buy_counter', '1')
    processing.set_app_property('user_buy_counter_limit', '10')
    processing.set_app_property('user_buy_counter_discount', '1')
    processing.set_app_property('user_logged_in_discount', '3')
    processing.set_app_property('snack_price', '50')
    processing.set_app_property('booking_timeout', '15')


def add_user_features():
    f1 = processing.add_feature('dog')[0]
    f2 = processing.add_feature('elephant')[0]
    f3 = processing.add_feature('clown')[0]
    UserFeature.objects.create(name='cat', price='50', incompatible_with=f1)
    UserFeature.objects.create(name='mouse', price='50', incompatible_with=f2)
    UserFeature.objects.create(name='parrot', price='50')


def add_anonymous():
    User.objects.create_user(username='anonymous',password='606ff68fcdadc34eba6f27fd25424934')
