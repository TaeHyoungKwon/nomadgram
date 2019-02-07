## 1. How does a backend Work?



![image-20190208013301952](/Users/thkwon/Library/Application Support/typora-user-images/image-20190208013301952.png)



* 백엔드가 동작하는 과정
  1. 브라우져에서 서버로 프로필을 요청한다.
  2. 서버는 해당 요청을 받고, 데이터베이스로 부터, 해당하는 정보를 받는다.
  3. 이때 받는 정보는 쿼리셋의 형태로 전달되고, 브라우져가 알아들을 수 있도록하기 위해서, Serialize 한다.
  4. 여기서 Serialize는 데이터베이스로 부터 받은 QuerySet을 JSON으로 바꾸는 것이다.
  5. 요청한 프로필에 대해서 JSON Object로 응답 값을 받는다.



## 2. Intro duction to Django

* Django is a framework
* 생산성이 좋다.



## 3. What is an virtual environment

* pipenv
*  프로젝트에 대한 개발환경을 독립적으로 유지하기 위해서 사용한다.



## 4. Creating a VirtualEnvironment

```shell
#pipenv 설치
brew install pipenv

#새로운 버블 pipenv 3 생성
pipenv --three

#pipenv에 라이브러리 추가
pipenv install requests

#pipenv 실행
pipenv shell
```





## 5. Parts of Django-Settings, Urls, Apps

* Settings
  * 장고의 행동방식을 커스터마이징 할 수 있다.
  * 타임존, 언어 설정 등등
* URLS
  * 외부에서 장고 서버에 요청을 보낼 때, url을 기준으로 보내게 되고, 해당 url이 호출되면, 매치되는 view function이 호출된다.
* Apps
  * 앱은 최대한 작게





## 6. Creating our Django Project

 ```shell
#쿠키커터 설치
pip3 install cookiecutter

#쿠키커터 실행 및 프로젝트 세팅
cookiecutter https://github.com/pydanny/cookiecutter-django
 ```





## 7. Creating the GitHub Repository

```shell
git remote add origin {Github repo}

git pull origin master
```





## 8. Installing the requirements

```shell
pipenv --three
pipenv install -r local.txt
pipenv shell
```





## 9. Production settings and local settings

* local setting and production setting
  * Base + local
  * base + production
  * 글로벌한 설정은 base에 들어간다.



## 10. Databases and Django

> 장고에서는 여러가지 디비를 사용할 수 있다. 원하는거 사용하자.



## 11. Creating the Databases

* pgadmin을 설치한다.
  * https://postgresapp.com/

![image-20190208034855726](assets/image-20190208034855726.png)

* 이걸 클릭하고, 쉘이 뜨면,

  ```shell
  CREATE DATABASE nomadgram;
  ```

  * 을 적어준다.

  ```python
  DATABASES = {
      'default': env.db('DATABASE_URL', default='postgres:///nomadgram'),
  }
  ```

  * setting 상의 db설정이 위와같이 되어있고, nomadgram db를 생성하면, 여기에 적힌대로 매칭이 되고, 서버를 실행할 수 있게된다.

  ![image-20190208035002577](assets/image-20190208035002577.png)





## 12. Creating the Apps



```shell
cd nomadgram
django-admin startapp images
```

* images 앱을 생성 한 후, base.py에 등록해준다.



```python
#images/apps.py
from django.apps import AppConfig

class ImagesConfig(AppConfig):
    name = 'nomadgram.images'
```



```python
#base.py

LOCAL_APPS = [
    'nomadgram.users.apps.UsersAppConfig',
    'nomadgram.images.apps.ImagesConfig'
]
```

* 위와 같이 앱을 등록한다.









