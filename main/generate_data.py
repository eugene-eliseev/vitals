from .models import Race, Seller, Buyer, Vital, Sex


def generate_data():
    race1, _ = Race.objects.get_or_create(name="Test race 1")
    race2, _ = Race.objects.get_or_create(name="Test race 2")
    seller, _ = Seller.objects.get_or_create(name="Джанго Освобождённый", phone=911)
    buyer, _ = Buyer.objects.get_or_create(name="Сатана", phone=666)
    vital, _ = Vital.objects.get_or_create(name="Мозг")
    sex1, _ = Sex.objects.get_or_create(name="М")
    sex2, _ = Sex.objects.get_or_create(name="Ж")