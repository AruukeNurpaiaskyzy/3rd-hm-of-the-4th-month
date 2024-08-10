from django.db import models
from apps.base.utits import ICON
# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='заголовок'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        verbose_name_plural = 'настройка баннера'

class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='заголовок'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    icon = models.CharField(
        choices=ICON,
        max_length=10,
        verbose_name='Иконка'
    )

    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        verbose_name_plural = 'о нас '
