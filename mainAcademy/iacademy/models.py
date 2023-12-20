from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    USER = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENTS'),
    )
    
    user_type = models.CharField(choices=USER, max_length=30, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

#========== Course Model =============
class Course (models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


#========== Session Model=============
class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.session_start + " - " + self.session_end


#========== Student Model =============
class Student (models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year, on_delete= models.DO_NOTHING)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.admin.first_name + " " + self.admin.last_name


#========== Staff Model =============


class Staff(models.Model):

    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name


# ========== Subject Model =============
class Subject(models.Model):
    name = models.CharField(max_length=100)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True , null = True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return  self.name


# ========== Staff Notification Model =============

class Staff_notification (models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.IntegerField(null = True, default = 0)

    def __str__(self):
        return self.staff_id.admin.first_name


# ========== Staff Leave Model =============
    
class Staff_leave(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default = 0)

    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name


# ========== Staff Feedback Model =============
    
class Staff_Feedback(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name





