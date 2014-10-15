from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=64)
    access_id = models.CharField(max_length=64)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.name

class Schedule(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.name

