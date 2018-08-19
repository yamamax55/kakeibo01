# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


@python_2_unicode_compatible
class AuthUserManager(BaseUserManager):
    def create_user(self, username, email, password, last_name, first_name):
        """
        ユーザ作成

        :param username: ユーザID
        :param email: メールアドレス
        :param password: パスワード
        :param last_name: 苗字
        :param first_name: 名前
        :return: AuthUserオブジェクト
        """
        if not email:
            raise ValueError('Users must have an email')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(username=username,
                          email=email,
                          password=password,
                          last_name=last_name,
                          first_name=first_name)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, last_name, first_name):
        """
        スーパーユーザ作成

        :param username: ユーザID
        :param email: メールアドレス
        :param password: パスワード
        :param last_name: 苗字
        :param first_name: 名前
        :return: AuthUserオブジェクト
        """
        user = self.create_user(username=username,
                                email=email,
                                password=password,
                                last_name=last_name,
                                first_name=first_name)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


@python_2_unicode_compatible
class AuthUser(AbstractBaseUser, PermissionsMixin):
    """
    ユーザ情報を管理する
    """
    class Meta:
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'

    def get_short_name(self):
        """
        ユーザの苗字を取得する

        :return: 苗字
        """
        return self.last_name

    def get_full_name(self):
        """
        ユーザのフルネームを取得する

        :return: 苗字 + 名前
        """
        return self.last_name + self.first_name

    username = models.CharField(verbose_name='ユーザID',
                                unique=True,
                                max_length=30)
    last_name = models.CharField(verbose_name='苗字',
                                 max_length=30,
                                 default=None)
    first_name = models.CharField(verbose_name='名前',
                                  max_length=30,
                                  default=None)
    email = models.EmailField(verbose_name='メールアドレス',
                              null=True,
                              default=None)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(verbose_name='有効フラグ',
                                    default=True)
    is_staff = models.BooleanField(verbose_name='管理サイトアクセス権限',
                                   default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'last_name', 'first_name']
    objects = AuthUserManager()

    def __str__(self):
        return self.last_name + ' ' + self.first_name
