from django.db import models

'''
from users.models import User

{
    "userName": "Sourav Singh",
    "userNumber": "9876543211",
    "userEmail": "sourav@gmail.com",
    "userPass": "sourav22454"
}

// userEmail-password
// mobile-password
User.objects.create(userName= "Sourav Singh", userNumber= "9876543211", userEmail= "sourav@gmail.com", userPass= "sourav22454")
User.objects.create(userName= "Gaurav Singh", userNumber= "9876543222", userEmail= "gaurav@gmail.com", userPass= "gaurav22584")
User.objects.all().delete()
'''


class User(models.Model):
    userName = models.CharField(max_length=25) 
    userNumber = models.CharField(max_length=10)
    userEmail = models.EmailField(max_length=25, unique=True)
    userPass = models.CharField(max_length=25)

    def __str__(self):
        return self.userName
