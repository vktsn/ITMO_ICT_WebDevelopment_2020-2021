from django.db import models


class Guest(models.Model):
    passport_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    check_in_date = models.DateField(auto_now_add=True)
    room = models.OneToOneField('Room', on_delete=models.PROTECT, related_name='guest')


class Staff(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)


class Room(models.Model):
    ROOM_TYPE = (
        ('3', '3 beds'),
        ('2', '2 beds'),
        ('1', '1 bed'))

    type = models.CharField(max_length=1, choices=ROOM_TYPE)
    price = models.IntegerField()
    floor = models.IntegerField()
    cleaners = models.ManyToManyField('Staff', through='Cleaning')


class Cleaning(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='cleaning1')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='cleaning')
    date_time = models.DateTimeField()
