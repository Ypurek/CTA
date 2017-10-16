from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class CreditCard(models.Model):
    card_number = models.CharField(primary_key=True, max_length=19)
    amount = models.FloatField(default=1000)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )
    birth_day = models.DateField(null=True)
    image = models.ImageField(null=True)
    credit_card = models.ForeignKey(
        CreditCard,
        related_name='user',
        on_delete=models.SET_NULL,
        null=True,
        default=None,
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Performance(models.Model):
    date = models.DateField('date of performance')
    time = models.TimeField('time of performance')
    description = models.TextField(max_length=1000)


class Ticket(models.Model):
    status = models.CharField(max_length=16)
    price = models.FloatField('price')
    performance_id = models.ForeignKey(
        Performance,
        related_name='tickets',
        on_delete=models.CASCADE,
        null=False,
        blank=False
        )
    booked = models.DateTimeField(
        null=True,
        blank=True
    )
    bought = models.DateTimeField(
        null=True,
        blank=True
    )
    booked_by = models.ForeignKey(
        User,
        related_name='booked_tickets',
        on_delete=models.CASCADE,
        null=True,
        )
    bought_by = models.ForeignKey(
        User,
        related_name='bought_tickets',
        on_delete=models.CASCADE,
        null=True
        )


class Feature(models.Model):
    feature = models.CharField(max_length=16, primary_key=True)
    performance_id = models.ManyToManyField(Performance)


class Discount(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    percent = models.IntegerField('discount percentage')
    ticket_id = models.ForeignKey(
        Ticket,
        related_name='discount',
        on_delete=models.CASCADE,
        null=True
    )


class TicketHistory(models.Model):
    datetime = models.DateTimeField()
    message = models.CharField(max_length=30)
    ticket_id = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        null=False
        )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
        )


class UserFeature(models.Model):
    feature_name = models.CharField(max_length=16, primary_key=True)
    price = models.FloatField()
    incompatible_with = models.ForeignKey(
        Feature,
        related_name='user_feature',
        blank=True,
        null=True)


# TODO replace with config file?
class AppSettings(models.Model):
    property = models.CharField(max_length=64, primary_key=True)
    value = models.CharField(max_length=64)
