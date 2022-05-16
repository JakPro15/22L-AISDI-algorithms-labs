import n
import kr
import kmp


text_petrosian = """
Are you kidding ??? What the **** are you talking about man ?
You are a biggest looser i ever seen in my life ! You was doing PIPI
in your pampers when i was beating players much more stronger then you!
You are not proffesional, because proffesionals knew how to lose and
congratulate opponents, you are like a girl crying after i beat you!
Be brave, be honest to yourself and stop this trush talkings!!!
Everybody know that i am very good blitz player, i can win anyone
in the world in single game! And "w"esley "s"o is nobody for me,
just a player who are crying every single time when loosing,
( remember what you say about Firouzja ) !!! Stop playing with my name,
i deserve to have a good name during whole my chess carrier, I am
Officially inviting you to OTB blitz match with the Prize fund! Both
of us will invest 5000$ and winner takes it all!

I suggest all other people who's intrested in this situation, just
take a look at my results in 2016 and 2017 Blitz World championships,
and that should be enough... No need to listen for every crying babe,
Tigran Petrosyan is always play Fair ! And if someone will continue
Officially talk about me like that, we will meet in Court! God bless
with true! True will never die ! Liers will kicked off...
"""


text_cejrowski = """
Zima idzie a ja w starych adidasach już miałem dziurę taką, że można było 2 palce
wsadzić więc po miesiącu wyrzeczeń dzięki którym zaoszczędziłem pieniądze, poszedłem
wczoraj do galerii handlowej kupić sobie porządne buty na zimę. W sklepie CCC znalazłem
pic rel. Solidne wykonanie, przystępna cena, modny wygląd- nie zastanawiałem się długo.
Wróciłem z butami do domu, pochodziłem w nich po pokoju, poprzeglądałem się w lustrze
i czułem dobrze. Jeszcze je solidnie zaimpregnowałem, żeby nie przepuszczały wody i
się nie niszczyły. 

Dzisiaj poszedłem w swoich nowych butach na uniwersytet. Czułem się dzięki nim bardziej
pewny siebie, jak siedziałem na korytarzu to nogi wyciągałem daleko, żeby ludzie lepiej
widzieli jakie mam eleganckie buty. 
Po zajęciach czekam na przystanku na Krakowskim Przedmieściu na autobus a tu z kawiarni
wychodzi znany podróżnik katolicki Wojciech Cejrowski. Elegancko ubrany a nie w jakąś
tam koszulę hawajską, z egzotycznych motywów to miał tylko w ręce taki kubeczek na yerba mate. 
Popatrzył się na mnie, na moje buty i podchodzi i zagaduje, czy te buty to są te z CCC
za 139,00zł. 
Ja mu zadowolony mówię, że tak panie Wojtku, te same dokładnie, i że miło, że pan zauważył. 
Cejrowski na to powiedział tylko 
>Śmieć 
Mi szczęka opadła i nie wiem o co chodzi. Cejrowski pyta, którego wyrazu nie rozumiem
"śmieć" czy "śmieć". No to ja mówię, że obydwa rozumiem tylko nie wiem dlaczego tak mówi.
Cejrowski mówi, że dlatego, że tylko śmieć może nosić takie biedackie buty. Że
on do dzikich krajów jeździł i tam ONZ i Czerwony Krzyż takie buty przysyłał dla biednych
ludzi za darmo i nawet oni nie chcieli w nich chodzić tylko wyrzucali. I że nawet było
specjalne posiedzenie komisji UNICEF, że nie wolno głodnym dzieciom takich gównianych
butów dawać, więc tam przestali wysyłać tylko do sklepów do Polski. 
Ludzie na przystanku śmiechają pod nosami i się patrzą na moje buty, ja już gula w gardle
i staram się jakoś jeden za drugim schować ale to nic nie daje. Ale jednak pomyślałem,
że nie dam sobą pomiatać nawet znanemu człowiekowi i krzyczę na Wojciecha, że on sam
przecież boso przez świat chodzi więc nie ma prawa się do moich butów przyczepiać.   
Cejrowski w śmiech i mówi, że boso to on chodzi w eleganckich krajach zagranicznych a
nie w Polsce gdzie co 5 metrów można w psie gówno wejść albo jakąś strzykawkę z HIV,
i że po Polsce to on chodzi w porządnych butach i pokazuje mi swoje buty z jakimiś
frendzlami, paskami, dolce&gabana i że nawet taki guzik mają, że jak go lawina przysypie
w tych butach to on ten guzik naciska i go wtedy można znaleźć pod śniegiem. 
Ja nie daję za wygraną i krzyczę, że przecież on jest człowiekiem wierzącym gorliwie i
że Pan Jezus chodził boso albo w jakichś rozpadających się sandałach więc dlaczego on
mnie obraża. Cejrowski na to, że z tymi sandałami Jezusa to lewacka propaganda II Soboru
Watykańskiego i Jezus obuwie dobierał bardzo starannie, i jakby teraz zszedł na ziemię
znowu i mnie w takich butach zobaczył to by mi w mordę przywalił. 
Ja cały czerwony, nie wiem co powiedzieć, ludzie ryczą ze śmiechu a Wojtek Cejrowski
mówi, żebym się zachował jak biały człowiek honoru i te buty zdejmował i uciekał. No
to ściągam te buty, cały już zaryczany bo tak mi było ich szkoda i odkładam do kosza
na śmieci na przystanku delikatnie, bo je chciałem wyjąć jak Cejrowski pójdzie. 

Stoję na śniegu w samych skarpetkach, nogi aż pieką od zimna, autobus powoli nadjeżdża,
chciałem szybko buty złapać i wskoczyć do środka ale jak się rzuciłem do śmietnika to
Wojciech mi zagrodził drogę i powiedział, żebym miał trochę godności. Wsiadłem bosy
do autobusu, przejechałem jeden przystanek, wysiadłem i biegiem lecę spowrotem buty
zabrać. Grzebię w śmietniku, wszystkow wyrzucam z niego ale butów nie ma. Pytam ludzi
co stali na przystanku, czy butów ktoś ze śmietnika nie zabrał a oni mówią, że tak,
że znany podróżnik Wojciech Cejrowski tutaj był i wziął buty i powiedział, że jedzie
na ryzykowną wyprawę do Nepalu i w sam raz będzie miał buty eleganckie i niezawodne. 
A ja będę całą zimę zawalał w starych adidasach.
"""


text_numbers = ""
for i in range(1000):
    text_numbers += str(i)


def test_petrosian_n():
    text = text_petrosian

    string = "***"
    pos = n.find(string, text)
    assert pos == [30, 31]

    string = "looser"
    pos = n.find(string, text)
    assert pos == [81]

    string = "ff"
    pos = n.find(string, text)
    assert pos == [219, 241, 737, 1131, 1251]


def test_petrosian_kr():
    text = text_petrosian

    string = "***"
    pos = kr.find(string, text)
    assert pos == [30, 31]

    string = "looser"
    pos = kr.find(string, text)
    assert pos == [81]

    string = "ff"
    pos = kr.find(string, text)
    assert pos == [219, 241, 737, 1131, 1251]


def test_petrosian_kmp():
    text = text_petrosian

    string = "***"
    pos = kmp.find(string, text)
    assert pos == [30, 31]

    string = "looser"
    pos = kmp.find(string, text)
    assert pos == [81]

    string = "ff"
    pos = kmp.find(string, text)
    assert pos == [219, 241, 737, 1131, 1251]


def test_cejrowski_n():
    text = text_cejrowski

    string = "boso"
    pos = n.find(string, text)
    assert pos == [2112, 2219, 2718]

    string = "Cejrowski"
    pos = n.find(string, text)
    assert pos == [880, 1212, 1296, 1430, 2189, 2796, 3101, 3342, 3903]

    string = "Nepal"
    pos = n.find(string, text)
    assert pos == [3984]


def test_cejrowski_kr():
    text = text_cejrowski

    string = "boso"
    pos = kr.find(string, text)
    assert pos == [2112, 2219, 2718]

    string = "Cejrowski"
    pos = kr.find(string, text)
    assert pos == [880, 1212, 1296, 1430, 2189, 2796, 3101, 3342, 3903]

    string = "Nepal"
    pos = kr.find(string, text)
    assert pos == [3984]


def test_cejrowski_kmp():
    text = text_cejrowski

    string = "boso"
    pos = kmp.find(string, text)
    assert pos == [2112, 2219, 2718]

    string = "Cejrowski"
    pos = kmp.find(string, text)
    assert pos == [880, 1212, 1296, 1430, 2189, 2796, 3101, 3342, 3903]

    string = "Nepal"
    pos = kmp.find(string, text)
    assert pos == [3984]


def test_numbers_n():
    text = text_numbers

    string = "998"
    pos = n.find(string, text)
    assert pos == [2288, 2829, 2884]

    string = "676869"
    pos = n.find(string, text)
    assert pos == [124]

    string = "Nepal"
    pos = n.find(string, text)
    assert pos == []


def test_numbers_kr():
    text = text_numbers

    string = "998"
    pos = kr.find(string, text)
    assert pos == [2288, 2829, 2884]

    string = "676869"
    pos = kr.find(string, text)
    assert pos == [124]

    string = "Nepal"
    pos = kr.find(string, text)
    assert pos == []


def test_numbers_kmp():
    text = text_numbers

    string = "998"
    pos = kmp.find(string, text)
    assert pos == [2288, 2829, 2884]

    string = "676869"
    pos = kmp.find(string, text)
    assert pos == [124]

    string = "Nepal"
    pos = kmp.find(string, text)
    assert pos == []


from random import randint


def test_random_comparison_n_kr():
    text = ""
    for _ in range(1000):
        text += str(randint(0, 1000))
    for i in range(1000):
        string = str(i)
        pos_n = n.find(string, text)
        pos_kr = kr.find(string, text)
        assert pos_n == pos_kr


def test_random_comparison_n_kmp():
    text = ""
    for _ in range(1000):
        text += str(randint(0, 1000))
    for i in range(1000):
        string = str(i)
        pos_n = n.find(string, text)
        pos_kmp = kmp.find(string, text)
        assert pos_n == pos_kmp


def test_random_comparison_kr_kmp():
    text = ""
    for _ in range(1000):
        text += str(randint(0, 1000))
    for i in range(1000):
        string = str(i)
        pos_kr = kr.find(string, text)
        pos_kmp = kmp.find(string, text)
        assert pos_kr == pos_kmp
