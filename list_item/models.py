from django.db import models


class ListItemModel(models.Model):
 """
 Модель списка дел внутри задачи
 """
 name = models.CharField(max_length=130, verbose_name='Название дела')
 created = models.DateTimeField(auto_now_add=True)
 modified = models.DateTimeField(auto_now=True)
 list = models.ForeignKey('main.ListModel', on_delete=models.CASCADE)
 is_done = models.BooleanField(default=False)
 expare_date = models.DateTimeField(auto_now=True)


 def __str__(self):
  return self.name

 class Meta:
  verbose_name = 'Список задач'

