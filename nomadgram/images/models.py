from django.db import models


class TimeStampedModel(models.Model):
    '''
    모든 모델에 공통적으로 사용되는
    created_at, updated_at 부분을 따로 추상화 시켜서 추상 클래스화 한다.
    '''
    created_at = models.DateTimeField(("Created Date"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated Date"), auto_now=True)

    # 추상 클래스로 지정
    class Meta:
        abstract = True


class Image(TimeStampedModel):
    file = models.ImageField(("Image"), upload_to=None, height_field=None, width_field=None, max_length=None)
    location = models.CharField(("Location"), max_length=50)
    caption = models.TextField(("Caption"))


class Comment(TimeStampedModel):
    message = models.TextField(("Message"))
