from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # gender를 CharField로 지정하였기 때문에, 어떤 문자열도 올 수 있다.
    # gender에 대해서 일정부분만 지정하기 위해선 다음과 같이 해주고,
    # choices 옵션을 추가한다.
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(_("Website"), max_length=200, null=True)
    bio = models.TextField(_("Bio"), null=True)
    phone = models.CharField(_("Phone Number"), max_length=140, null=True)
    gender = models.CharField(_("Gender"), max_length=80, choices=GENDER_CHOICES, null=True)

    # 팔로잉 팔오워 모두, 자기 자신에게 연결한다.
    followers = models.ManyToManyField("self", verbose_name=_("나를 팔로워 하고 있는 유저들"))
    following = models.ManyToManyField("self", verbose_name=("내가 팔로잉 하고 있는 유저들"))

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
