from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_name_2 = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    course = models.CharField(max_length=50)
    tutor = models.BooleanField(default=False)
    modules = models.ManyToManyField(Module, related_name="teachers", blank=True)

    def __str__(self):
        return f"{self.name} {self.last_name} {self.last_name_2}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_name_2 = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    course = models.CharField(max_length=50)
    modules = models.ManyToManyField(Module, related_name="students", blank=True)

    def __str__(self):
        return f"{self.name} {self.last_name} {self.last_name_2}"