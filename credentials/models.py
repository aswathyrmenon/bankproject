from django.db import models


class District(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name



class Place(models.Model):
    name = models.CharField(max_length=100,unique=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class Detail(models.Model):
    name = models.CharField(max_length=100,unique=True)
    dob = models.DateField(default=None)
    age = models.IntegerField()
    GENDER = (
        ('', ''),
        ('female', 'FEMALE'),
        ('male', 'MALE'),

    )
    gender = models.CharField(max_length=6, choices=GENDER, default='')
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(max_length=500)
    district = models.ForeignKey(District,on_delete=models.CASCADE,null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE,null=True)
    account_type = models.CharField(max_length=8)
    materials_required = models.CharField(max_length=20)

    def __str__(self):
        return self.name























