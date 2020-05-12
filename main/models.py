from django.db import models


class PurposeModel(models.Model):
    """
    Описание таблицы БД по хранению целей
    """
    name = models.CharField(max_length=120, verbose_name='Название цели')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Список целей"
        unique_together = ('name', 'user')


#        indexes =