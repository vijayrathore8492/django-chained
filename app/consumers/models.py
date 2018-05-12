from django.db import models
from django.core.validators import RegexValidator

class Consumer(models.Model):

    name = models.CharField(
        max_length=300, 
        validators=[RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')], 
        help_text='Your Name'
        )
    email = models.EmailField(max_length=300, unique=True, help_text='Your Email')

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return "name = "+self.name + ";email = " + self.email