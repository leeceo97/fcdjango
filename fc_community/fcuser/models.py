from django.db import models

# Create your models here.

class Fcuser(models.Model):
    # Class 'Fcuser' has no 'objects' member; maybe 'object'?pylint(no-member)-->오류방지를 위한 코드
    objects=models.Manager()
    #verbose_name:username,password등이 아니라 뒤에적은 이름이 출력됨(편리성)
    username=models.CharField(max_length=64,verbose_name='사용자명')
    useremail=models.EmailField(max_length=128,verbose_name='사용자이메일')
    password=models.CharField(max_length=64,verbose_name='비밀번호')
    # auto_now_add:현재시간을 자동으로 추가해주는것 
    registered_dttm=models.DateTimeField(auto_now_add=True,verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table='fastcampus_fcuser'
        #fcuser가 아닌 패스트캠퍼스 사용자로 출력하기 위한것
        verbose_name="패스트캠퍼스 사용자"
        #plural은 뒤에 복수형으로 나오는걸 방지하기위한것
        verbose_name_plural='패스트캠퍼스 사용자'