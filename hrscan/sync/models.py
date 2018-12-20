# -*- coding: utf-8 -*
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.template.defaultfilters import slugify

class Degree(models.Model):
    none = models.IntegerField(default=-1000)
    name = models.CharField(blank=True, null=True, max_length=122100)
    rating = models.CharField(blank=True, null=True, max_length=122100)

    def save(self, *args, **kwargs):
        names=str(self.name)
        super(Degree, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Institute(models.Model):
    none = models.IntegerField(default=-1000)
    name = models.CharField(blank=True, null=True, max_length=122100)
    rating = models.CharField(blank=True, null=True, max_length=122100)

    def save(self, *args, **kwargs):
        names=str(self.name)
        super(Institute, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Course(models.Model):
    degree = models.ForeignKey(Degree, on_delete = models.CASCADE,  blank=True,related_name="courses")
    institute = models.ForeignKey(Institute, on_delete = models.CASCADE,  blank=True,related_name="courses")
    year = models.CharField(blank=True, null=True, max_length=122100)
    rating = models.CharField(blank=True, null=True, max_length=122100)

    def save(self, *args, **kwargs):
        names=str(self.name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Company(models.Model):
    none = models.IntegerField(default=-1000)
    name = models.CharField(blank=True, null=True, max_length=122100)
    rating = models.CharField(blank=True, null=True, max_length=122100)

    def save(self, *args, **kwargs):
        names=str(self.name)
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Exp(models.Model):
    year = models.CharField(blank=True, null=True, max_length=122100)
    rating = models.CharField(blank=True, null=True, max_length=122100)
    company = models.ForeignKey(Company, on_delete = models.CASCADE,  blank=True,related_name="artists")

    def save(self, *args, **kwargs):
        names=str(self.name)
        super(Exp, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Quality(models.Model):
    none = models.IntegerField(default=-1000)
    name = models.CharField(blank=True, null=True, max_length=122100)
    rating = models.CharField(blank=True, null=True, max_length=122100)

    def save(self, *args, **kwargs):
        names=str(self.name)
        super(Quality, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Artist(models.Model):
    none = models.IntegerField(default=-1000)
    name = models.CharField(blank=True, null=True, max_length=122100)
    qualities = models.ManyToManyField(Quality, blank=True, related_name="artists")
    exps = models.ManyToManyField(Exp, blank=True, related_name="artists")
    courses = models.ManyToManyField(Course, blank=True, related_name="artists")
    rating = models.CharField(blank=True, null=True, max_length=122100)
    gape = models.CharField(blank=True, null=True, max_length=122100)
    edu_dob = models.CharField(blank=True, null=True, max_length=122100)
    exp_dob = models.CharField(blank=True, null=True, max_length=122100)
    user = models.ForeignKey(User, on_delete = models.CASCADE,  blank=True,related_name="artists")

    def save(self, *args, **kwargs):
        names=str(self.name)
        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Cv(models.Model):
    none = models.IntegerField(default=-1000)
    name = models.CharField(blank=True, null=True, max_length=122100)
    rating = models.CharField(blank=True, null=True, max_length=122100)
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE,  blank=True,related_name="cvs")

    def save(self, *args, **kwargs):
        names=str(self.name)
        super(Cv, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Requirement(models.Model):
    company = models.ForeignKey(Company, on_delete = models.CASCADE,  blank=True,related_name="requirements")
    none = models.IntegerField(default=-1000)
    name = models.CharField(blank=True, null=True, max_length=122100)
    rating = models.CharField(blank=True, null=True, max_length=122100)
    qualities = models.ManyToManyField(Quality, blank=True, related_name="requirements")
    exps = models.ManyToManyField(Exp, blank=True, related_name="requirements")
    courses = models.ManyToManyField(Course, blank=True, related_name="requirements")
    gape = models.CharField(blank=True, null=True, max_length=122100)
    edu_dob = models.CharField(blank=True, null=True, max_length=122100)
    exp_dob = models.CharField(blank=True, null=True, max_length=122100)

    def save(self, *args, **kwargs):
        names=str(self.name)
        super(Requirement, self).save(*args, **kwargs)

    def __str__(self):
        return self.name