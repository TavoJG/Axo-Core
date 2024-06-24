from django.contrib.auth import get_user_model
from django.db import models

from common.models import AbstractBaseModel

User = get_user_model()


class Variable(AbstractBaseModel):
    name = models.CharField(max_length=50, unique=True)
    units = models.CharField(max_length=50)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Record(AbstractBaseModel):
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return f"{self.variable.name}: {self.value} {self.variable.units}"
