# By default, Django signals execute synchronously, meaning the signal handler is executed before
# the code continues execution after the signal is sent. 
# Below is a code snippet demonstrating this:

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received for:", instance.name)

# Creating an instance of MyModel
obj = MyModel.objects.create(name="Test")
print("Object created")  # This will be printed after the signal handler completes
