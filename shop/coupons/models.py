from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Код Купона")
    valid_from = models.DateTimeField(verbose_name="Купон От")
    valid_to = models.DateTimeField(verbose_name="Купон Для")
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Скидка")
    active = models.BooleanField(verbose_name="Активна")

    class Meta:
        ordering = ('-valid_to',)
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return self.code
