from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    ROASTING_CHOICES = (
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
    )
    SOUR_CHOICES = (
        ('low', 'Низкая'), ('medium', 'Средняя'), ('high', 'Высокая')
    )
    VIEW_COFFEE_CHOICES = (
        ('arabica', 'Арабика'), ('robusta', 'Робуста'), ('arabica_blend', 'Смесь арабик'),
        ('arabica_robusta', 'Смесь арабика/робуста')
    )
    VIEW_COFFEE_CHOICES = (
        ('popular', 'Популярное'), ('new_crop', 'Новый урожай'), ('your_choice', 'Ваш выбор'),
        ('micro_lot', 'Микролот'), ('sort_week', 'Сорт недели'), ('discounts', 'Скидки'), ('new', 'Новинка')
    )
    PROCESSING_METHOD_CHOICES = (
        ('dry', 'Сухая'), ('washed', 'Мытая'), ('other', 'Прочие')
    )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    title = models.CharField(max_length=200, default='some_product')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    roasting = models.PositiveIntegerField(default=0, blank=True, choices=ROASTING_CHOICES)
    sour = models.CharField(max_length=30, blank=True, choices=SOUR_CHOICES)
    view = models.CharField(max_length=30, blank=True, choices=VIEW_COFFEE_CHOICES)
    special = models.CharField(max_length=30, blank=True, choices=VIEW_COFFEE_CHOICES)
    processing_method = models.CharField(max_length=30, blank=True, choices=VIEW_COFFEE_CHOICES)
    geography = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=0, blank=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
