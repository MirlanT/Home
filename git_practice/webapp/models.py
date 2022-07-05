from django.db import models

other = 'other'
phone_choices = [
    (other, 'Other'),
    ('iphone', 'iphone'),
    ('samsung', 'samsung'),
    ('mi', 'mi')
]


class Product(models.Model):
    phone = models.CharField(max_length=100, verbose_name='phone')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    category = models.CharField(max_length=30, choices=phone_choices, default=other, verbose_name='Category')
    count = models.IntegerField(default=0, verbose_name='Count')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return f'{self.phone} - {self.category} - {self.price}'

    class Meta:
        verbose_name = 'Telephone'
        verbose_name_plural = 'Telephone'
