from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AdCategory(models.TextChoices):
    SERVICES = 'services', 'Услуги мастера'
    AUTO = 'auto', 'Авто и запчасти'
    FOOD = 'food', 'Домашняя выпечка и еда'
    EDUCATION = 'education', 'Обучение и репетиторы'
    ELECTRONICS = 'electronics', 'Электроника'
    REAL_ESTATE = 'real-estate', 'Недвижимость'
    JOBS = 'jobs', 'Работа'


class Ad(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=100, db_index=True)
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='RUB')
    category = models.CharField(
        max_length=32,
        choices=AdCategory.choices,
        default=AdCategory.SERVICES,
        db_index=True,
    )
    is_urgent = models.BooleanField(default=False, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    favorites = models.ManyToManyField(User, related_name='favorite_ads', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.city})"


class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='ads_images/')

    def __str__(self):
        return f"Фото для {self.ad.title}"
