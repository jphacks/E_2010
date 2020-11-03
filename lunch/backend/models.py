from django.db import models


# Create your models here.
class Test(models.Model):
    hoge = models.CharField(max_length=100)

    # テーブル名を指定
    class Meta:
        db_table = 'tests'

    # 管理者画面での表示方法の変更
    def __repr__(self):
        return "{}: {}".format(self.pk, self.hoge)

    __str__ = __repr__


class User(models.Model):
  # id は自動作成される
  # id = models.CharField(max_length=100)
  email = models.EmailField()
  name = models.CharField(max_length=50) #Char は max_length 必須
  password = models.CharField(max_length=50)
  university = models.CharField(max_length=100)
  research = models.TextField(max_length=300)

  STATUS_GENDER = (
      ('male', '男'),
      ('female', '女'),
      ('other', 'その他'),
  )
  gender = models.CharField(choices=STATUS_GENDER, default='male', max_length=10)
  age = models.PositiveSmallIntegerField()
  position = models.CharField(max_length=100)
  self_introduction = models.TextField(max_length=300, null=True, blank=True)
  birthday = models.DateField(null=True, blank=True)

  # テーブル名を指定
  class Meta:
      db_table = 'users'

  # 管理者画面での表示方法の変更
  def __repr__(self):
        return "{}: {}".format(self.pk, self.name)

  __str__ = __repr__
