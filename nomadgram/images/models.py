from django.db import models
from nomadgram.users import models as user_models


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
    '''
    Image Model
    '''
    file = models.ImageField(("이미지"))
    location = models.CharField(("장소"), max_length=50)
    caption = models.TextField(("내용"))
    # 각 작성자는 여러개의 이미지를 작성할 수 있다.
    creator = models.ForeignKey(user_models.User, verbose_name=("image_작성자"), on_delete=models.CASCADE, null=True)


class Comment(TimeStampedModel):
    ''' 
    Comment Model 
    '''
    message = models.TextField(("Message"))
    # 작성자는 여러개의 comment를 쓸 수 있다.
    creator = models.ForeignKey(user_models.User, verbose_name=("comment_작성자"), on_delete=models.CASCADE, null=True)
    # 각 이미지는 여러개의 comment 를 가진다.
    image = models.ForeignKey(Image, verbose_name=("comment_이미지"), on_delete=models.CASCADE, null=True)


class Like(TimeStampedModel):
    '''
    Like Model
    '''
    # 각각 사람들은 여러개의 좋아요를 가진다.
    creator = models.ForeignKey(user_models.User, verbose_name=("like_작성자"), on_delete=models.CASCADE, null=True)
    # 각 이미지는 여러개의 Like를 가진다.
    image = models.ForeignKey(Image, verbose_name=("like_이미지"), on_delete=models.CASCADE, null=True)
