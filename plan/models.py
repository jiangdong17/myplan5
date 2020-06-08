from django.db import models

# Create your models here.
#class Schools(models.Model)
    #sid = models.IntegerField()
    #sdate = models.DateField()
   #sname = models.CharField()
    #scity = models.CharField()
    #isDelete = models.BooleanField(default=False)

#class Grades(models.Model):
    #gid = models.IntegerField()
   # gnum = models.CharField()
    #ggirlnum = models.IntegerField()
    #gboynum = models.IntegerField()
    #isDelete = models.BooleanField(default=False)
    #gschool = models.ForeignKey("Schools")
#class Clas(models.Model):
    #cid = models.IntegerField()
    #cnum = models.CharField()
    #ggirlnum = models.IntegerField()
    #gboynum = models.IntegerField()
    #isDelete = models.BooleanField(default=False)
    #gschool = models.ForeignKey("Schools")
class Students(models.Model):
    xid = models.IntegerField()
    xschool = models.CharField(max_length=20)
    xgrade = models.CharField(max_length=20)
    xclass = models.CharField(max_length=20)
    xname = models.CharField(max_length=20)
    xage = models.IntegerField()
    xgender = models.BooleanField(default=False)
    #xgrade = models.ForeignKey("Grades")
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.xname

class Plans(models.Model):
    pname =models.CharField(max_length=20)
    #pname =models.CharField()
    pp_start_time = models.DateField()
    pp_start_time = models.DateField()
    pp_long = models.IntegerField()
    pstart_time = models.DateField()
    pover_time = models.DateField()
    plong = models.IntegerField()
    pscore = models.IntegerField()
    #isDelete = models.BooleanField(default=False)
    pstudent = models.ForeignKey("Students",on_delete=models.CASCADE)

    def __str__(self):
        return self.pname