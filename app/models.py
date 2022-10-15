from django.db.models import *


class User(Model):
    name = CharField(max_length=40, null=False)
    age = IntegerField()


class UserData(Model):
    user_id = OneToOneField(User,on_delete=CASCADE)
    email = EmailField(max_length=50)
    experience = IntegerField()


class Locate(Model):
    title = CharField(max_length=40)


class Industrial(Model):
    title = CharField(max_length=40)
