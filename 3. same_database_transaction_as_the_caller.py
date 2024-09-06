# Yes, Django signals run in the same database transaction as the caller by default. 
# The following code illustrates this:

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    instance.name = "Modified"
    instance.save()

obj = MyModel.objects.create(name="Original")
print("Name before save:", obj.name)

with transaction.atomic():
    obj.name = "Updated"
    obj.save()
    print("Name after save:", obj.name)
