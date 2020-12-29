from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField()
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=20)
    text1 = models.TextField()
    mail = models.EmailField()
    mobile=models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Cource(models.Model):
    name = models.CharField(max_length=20)
    image1 = models.TextField()
    image2 = models.TextField()
    image3 = models.TextField()
    image4 = models.TextField()
    image5 = models.TextField()
    text1 = models.TextField()


    def __str__(self):
        return self.name

class Python(models.Model):
    pname = models.CharField(max_length=20)
    text2=models.TextField()

    def __str__(self):
        return self.pname

class Django(models.Model):
    dname = models.CharField(max_length=20)
    text3=models.TextField()

    def __str__(self):
        return self.dname

class Datascience(models.Model):
    Dname = models.CharField(max_length=20)
    text4=models.TextField()

    def __str__(self):
        return self.Dname


class Bigdata(models.Model):
    Bname = models.CharField(max_length=20)
    text5=models.TextField()

    def __str__(self):
        return self.Bname

class Html_css(models.Model):
    Hname = models.CharField(max_length=20)
    text6=models.TextField()

    def __str__(self):
        return self.Hname