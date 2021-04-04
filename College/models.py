from django.db import models


#forgot password
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


class TeacherModel(models.Model):
    faculty_name = models.CharField(max_length=50,unique=True)
    subject = models.CharField(max_length=30)


class StudentModel(models.Model):
    roll_no = models.BigIntegerField(primary_key=True, unique=True)
    student_name = models.CharField(max_length=50)
    course = models.CharField(max_length=30)
    CHOICES=(
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others")
    )
    gender = models.CharField(max_length=10, choices=CHOICES)



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )