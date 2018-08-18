from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
    body2 = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class UserMstr(models.Model):
    userid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    mail = models.CharField(max_length=40)
    update_time = models.DateTimeField()
    regist_time = models.DateTimeField()
    loginflg = models.CharField(max_length=1)
    delflg = models.CharField(max_length=1)



    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class Kakikomi(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
