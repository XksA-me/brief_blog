from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    # 用户手机号
    mobile = models.CharField(max_length=11, unique=True, blank=False)
    # 用户头像
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=False)
    # 用户简介
    user_desc = models.CharField(max_length=500, blank=False)

    class Meta:
        db_table = 'tb_users'  # 修改表名
        verbose_name = '用户管理'  # admin后台显示
        verbose_name_plural = verbose_name  # admin后台显示

    def __str__(self):
        return self.mobile


