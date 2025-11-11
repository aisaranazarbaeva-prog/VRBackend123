from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    years_experience = models.PositiveIntegerField(verbose_name="Опыт (лет)", default=0)
    percent_satisfaction = models.PositiveIntegerField(verbose_name="Процент удовлетворения клиентов", default=0)
    free_support_months = models.PositiveIntegerField(verbose_name="Бесплатная поддержка (мес.)", default=0)
    image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self):
        return self.title