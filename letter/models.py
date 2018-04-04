# -*- conding:utf-8 -*-
from django.db import models
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible
class Letter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject[:20]

