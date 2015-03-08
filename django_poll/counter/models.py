from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=11)
    ethnicity = models.CharField(max_length=14)

    def __str__(self):
        return str(self.ethnicity + " " + self.gender)


class Segment(models.Model):
    ## producer = models.ForeignKey(Producer, default=)
    slug = models.CharField(max_length=100)
    pub_date = models.DateField('airdate')
    order_in_show = models.IntegerField(default=0)

    def __str__(self):
        return self.slug


class Guest(models.Model):
    WHITE = 'W'
    BLACK = 'B'
    LATINO = 'L'
    MIDDLE_EASTERN = 'M'
    ASIAN = 'A'
    OTHER_UNKNOWN = 'O'
    ETHNICITY_CHOICES = (
        (WHITE, 'White'),
        (BLACK, 'Black'),
        (LATINO, 'Latino'),
        (MIDDLE_EASTERN, 'Middle Eastern'),
        (ASIAN, 'Asian'),
        (OTHER_UNKNOWN, 'Other/Unknown'))

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))

    ethnicity = models.CharField(max_length=1, choices=ETHNICITY_CHOICES, default=WHITE)	
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    segment = models.ForeignKey(Segment)

    def __str__(self):
        return str(self.ethnicity + "," + self.gender)
