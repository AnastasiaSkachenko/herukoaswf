from django.db import models

class Count(models.Model):
    integer_1 = models.IntegerField(null=True)
    numerator_1 = models.IntegerField()
    denominator_1 = models.IntegerField()

    operator = models.Field()

    integer_2 = models.IntegerField(null=True)
    numerator_2 = models.IntegerField()
    denominator_2 = models.IntegerField()
