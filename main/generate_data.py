from .models import Race, Seller, Buyer, Vital, Sex, People, PeopleVital
import random


def generate_data():
    races = [
        "Европеоидная раса",
        "Негроидная раса",
        "Восточноафриканская (эфиопская) раса",
        "Монголоидная раса",
        "Американоидная раса",
        "Веддо-австралоидная раса"
    ]
    reasons = [
        "Погряз в долгах",
        "Неизлечимая болезнь",
        "Перешёл дорогу не тому человеку"
    ]
    races_o = []
    for race in races:
        try:
            o = Race.objects.get(name=race)
            return
        except Exception as e:
            pass
        races_o.append(Race.objects.get_or_create(name=race)[0])
    sellers = []
    buyers = []
    with open("main/sellers.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            sellers.append(Seller.objects.get_or_create(name=line, phone=random.randint(1000000, 9999999))[0])
    with open("main/buyers.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            buyers.append(Buyer.objects.get_or_create(name=line, phone=random.randint(1000000, 9999999))[0])
    sex_m, _ = Sex.objects.get_or_create(name="М")
    sex_w, _ = Sex.objects.get_or_create(name="Ж")
    peoples = []
    with open("main/people.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            first_name = line.split(' ')[0]
            second_name = line.split(' ')[1]
            peoples.append(People.objects.get_or_create(
                first_name=first_name,
                second_name=second_name,
                reason=reasons[random.randint(0, len(reasons)-1)],
                sex=sex_m,
                is_alive=random.randint(0, 1),
                birthday="{}-{}-{}".format(random.randint(1900, 2000), random.randint(1, 12), random.randint(1, 12)),
                first_payment=random.randint(0, 1000000),
                buy_price=random.randint(100, 1000000),
                sell_price=random.randint(100, 1000000),
                sell_date="{}-{}-{}".format(random.randint(2010, 2019), random.randint(1, 12), random.randint(1, 12)),
                race=races_o[random.randint(0, len(races_o)-1)],
                seller=sellers[random.randint(0, len(sellers)-1)],
                buyer=buyers[random.randint(0, len(buyers)-1)]
            )[0])
    vitals = [
        "Мозг",
        "Печень",
        "Сердце",
        "Правое лёгкое",
        "Левое лёгкое",
        "Левая почка",
        "Правая почка",
        "Мочевой пузырь",
        "Селёзенка",
        "Желудок",
        "Левый глаз",
        "Правый глаз",
    ]
    vitals_o = []
    for vital in vitals:
        vitals_o.append(Vital.objects.get_or_create(name=vital)[0])

    variants = []
    for vital in vitals_o:
        for people in peoples:
            variants.append((people, vital))
    for _ in range(len(variants) // 5):
        number = random.randint(0, len(variants)-1)
        PeopleVital.objects.get_or_create(
            vital=variants[number][1],
            people=variants[number][0],
            price=random.randint(100, 100000),
            condition=random.randint(0, 100),
            buyer=buyers[random.randint(0, len(buyers)-1)]
        )
        del variants[number]
