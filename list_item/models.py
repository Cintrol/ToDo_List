from django.db import models
from main.models import PurposeModel


class TaskModel(models.Model):
    """
 Модель списка дел внутри задачи
 """
    name = models.CharField(max_length=130, verbose_name='Название задачи')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    purpose = models.ForeignKey('main.PurposeModel', on_delete=models.CASCADE,
                                verbose_name='Цель')
    is_done = models.BooleanField(default=False)
    expare_date = models.DateTimeField(blank=True, null=True)
    priority = models.SmallIntegerField(verbose_name='Приоритет', default=0)

    def save(self, *args, **kwargs):
        super(TaskModel, self).save(*args, **kwargs)

        purpose_edit = PurposeModel.objects.get(id=self.purpose_id)
        if TaskModel.objects.filter(purpose=self.purpose_id, is_done=False):
            purpose_edit.is_done = False
        else:
            purpose_edit.is_done = True
        purpose_edit.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Список задач'
        unique_together = ('name', 'purpose')
