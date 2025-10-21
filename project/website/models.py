from django.db import models

class SiteSettings(models.Model):
    """Основные настройки сайта"""
    company_name = models.CharField('Название компании', max_length=200, default='Хакасская газовая компания')
    phone = models.CharField('Телефон', max_length=20, default='+7 (913) 442-57-77')
    additional_telephone = models.CharField('Телефон', max_length=20, default='')
    email = models.EmailField('Email', default='manyakin1975@mail.ru')
    address = models.TextField('Адрес', default='г. Абакан, Ташебинский промышленный узел, промплощадка Абаканвагонмаш территория, 77')
    working_hours = models.CharField('Режим работы', max_length=100, default='Пн-Пт: 8:00-17:00, экстренно 24/7')
    hero_title = models.CharField('Заголовок главной секции', max_length=200, default='Надежная поставка газа в Хакасии')
    hero_subtitle = models.TextField('Подзаголовок главной секции', default='Официальный дилер газа с полным спектром услуг: от заправки газгольдеров до монтажа оборудования')
    
    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'
    
    def __str__(self):
        return 'Настройки сайта'


class Service(models.Model):
    """Услуги компании"""
    title = models.CharField('Название услуги', max_length=200)
    description = models.TextField('Описание')
    icon = models.CharField('Иконка (эмодзи)', max_length=10, default='🔧')
    order = models.PositiveIntegerField('Порядок отображения', default=0)
    is_active = models.BooleanField('Активна', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title


class Advantage(models.Model):
    """Преимущества компании"""
    title = models.CharField('Название преимущества', max_length=200)
    description = models.TextField('Описание')
    icon = models.CharField('Иконка (эмодзи)', max_length=10, default='⭐')
    badge_text = models.CharField('Текст бейджа', max_length=50, blank=True)
    order = models.PositiveIntegerField('Порядок отображения', default=0)
    is_active = models.BooleanField('Активно', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title


class CoverageStat(models.Model):
    """Статистика покрытия"""
    title = models.CharField('Название', max_length=200)
    number = models.CharField('Число', max_length=20)
    description = models.TextField('Описание')
    icon = models.CharField('Иконка (эмодзи)', max_length=10, default='📊')
    order = models.PositiveIntegerField('Порядок отображения', default=0)
    is_active = models.BooleanField('Активно', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Статистика покрытия'
        verbose_name_plural = 'Статистика покрытия'
        ordering = ['order', 'title']
    
    def __str__(self):
        return f"{self.number} - {self.title}"


class DeliveryPoint(models.Model):
    """Точки доставки"""
    name = models.CharField("Название точки", max_length=100)
    description = models.TextField("Описание", blank=True)
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")
    active = models.BooleanField("Активна", default=True)

    class Meta:
        verbose_name = "Точка доставки"
        verbose_name_plural = "Точки доставки"

    def __str__(self):
        return self.name