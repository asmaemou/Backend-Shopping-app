from django.db import models

class User(models.Model):

    user_fname = models.CharField(max_length=20)
    user_lname = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_dob = models.CharField(max_length=20)
    user_picture = models.CharField(max_length=20)
    user_country = models.CharField(max_length=20)
    user_status = models.CharField(max_length=20)
    user_role = models.CharField(max_length=20)


    def __str__(self) :
        return self.user_fname + self.user_lname
