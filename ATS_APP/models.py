from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import logging

class userManager(BaseUserManager):
    use_in_migrations = True

    # python manage.py createsuperuser
    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email,
            is_superuser=True,
            **kwargs
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

# Create your models here.
class user(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=200)
    city=models.CharField(max_length=30,default='')
    phone=models.CharField(max_length=20,default='')
    country=models.CharField(max_length=200,default='')
    is_superuser=models.BooleanField(default='False')
    is_staff=models.BooleanField(default='False')
    is_active = models.BooleanField(default='True')

    objects = userManager()
    #objects = models.Manager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    # def is_staff(self, perm, obj=None):
    #     return self.is_staff
    #
    # def is_superuser(self, perm, obj=None):
    #     return self.is_superuser

    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_superuser


class User_Role(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(
        'Role',
         on_delete=models.CASCADE,
         )
    user = models.ForeignKey(
        'user',
         on_delete=models.CASCADE,
         )

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)

class Skill_Set(models.Model):
    skill_set_id = models.AutoField(primary_key=True)
    skill = models.CharField(max_length=1000)
    #skill_level = models.CharField(max_length=30)
    applicant = models.ForeignKey(
        'user',
         on_delete=models.CASCADE,
         )
 

class job_platforms(models.Model):
    job_platform_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description= models.CharField(max_length=1000,null=True)
    

class Company(models.Model):
    companey_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000,null=True)
  

   
class applicant_cv(models.Model):
    applicant_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(max_length=30)
    gender = models.CharField(max_length=30)
    summary = models.CharField(max_length=1000)
    last_updated = models.DateTimeField(max_length=30)
    zip_code=models.CharField(max_length=30,null=True)
    country=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    phone2=models.CharField(max_length=30,null=True)
    training_certification = models.CharField(max_length=100)
    applicant_cv = models.ForeignKey(
        'user',
         on_delete=models.CASCADE,
         )


class Experience(models.Model):
    experiance_id = models.AutoField(primary_key=True)
    organization = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    begin_date = models.DateTimeField(max_length=30)
    end_date = models.DateTimeField(max_length=30)
    applicant_cv = models.ForeignKey(
        'skill_set',
         on_delete=models.CASCADE,
         )

class Education(models.Model):
    education_id = models.AutoField(primary_key=True)
    institution_name = models.CharField(max_length=30)
    degree_obtained = models.CharField(max_length=30)
    date_attended_from= models.DateTimeField(max_length=30)
    date_attended_to = models.DateTimeField(max_length=30)
    applicant_cv = models.ForeignKey(
        'applicant_cv',
         on_delete=models.CASCADE,
         )

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    #name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000,null=True)
    date_published = models.DateTimeField()
    #job_start_date = models.DateTimeField(max_length=30,null=True)
    job_deadline = models.DateTimeField()
    number_of_vacancies = models.IntegerField()
    job_category = models.ForeignKey(
        'job_category',
         on_delete=models.CASCADE,
         )
    job_position = models.CharField(max_length=30)
    job_platform = models.ForeignKey(
        'job_platforms',
         on_delete=models.CASCADE,
         )
    organization_name = models.CharField(max_length=50,default='',null=True)
    file=models.FileField()
 
class job_category(models.Model):
    job_category_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000,null=True)

    
class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    date_of_application = models.DateTimeField(max_length=30,auto_now=True)
    job = models.ForeignKey(
        'job',
         on_delete=models.CASCADE,
         )
    user = models.ForeignKey(
        'user',
         on_delete=models.CASCADE,
         )
    application_status = models.CharField(max_length=30)



class Applicant_Document(models.Model):
    applicant_document_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    document= models.FileField()
    url = models.CharField(max_length=90,null=True)
    last_updated = models.DateTimeField(auto_now=True, max_length=30)
    user  = models.ForeignKey(
        'user',
         on_delete=models.CASCADE,
         )

class candidate_Evaluation(models.Model):
    candidate_evaluation_id = models.AutoField(primary_key=True)
    evaluation_notes = models.CharField(max_length=1000, null=True)
    job = models.ForeignKey(
        'job',
         on_delete=models.CASCADE,
         )
    applicant = models.ForeignKey(
        'user',
         on_delete=models.CASCADE,
         )
    evaluation_result = models.IntegerField()

 

class Job_Description_Document(models.Model):
    job_description_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    document= models.FileField(max_length=100)
    last_updated = models.DateTimeField(max_length=30)
    job  = models.ForeignKey(
        'job',
         on_delete=models.CASCADE,
         )
