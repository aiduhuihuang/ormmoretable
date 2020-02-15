from django.db import models

# Create your models here.
class Publish(models.Model):
    name=models.CharField(max_length=32,verbose_name="出版社名称")
    address=models.CharField(max_length=50,verbose_name="出版社地址")

    class Meta:
        db_table="publish"
        verbose_name_plural="出版社"

class Book(models.Model):
    name=models.CharField(max_length=32,verbose_name="书籍名字")
    pub=models.ForeignKey(to=Publish,on_delete=models.CASCADE)

    class Meta:
        db_table="book"
        verbose_name_plural="书籍"