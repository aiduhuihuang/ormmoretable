from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

#测试首页
def index(request):
    return  HttpResponse("测试首页")

#一对多关系的增加
def oneaddmore(request):
    #第一种方法
    # Publish.objects.create(name="北京出版社",address="北京")
    # Publish.objects.create(name="深圳出版社",address="深圳")


    # Book.objects.create(name="HTML5网页技术",pub_id=2)

    #第二种方法
    #正向：从外建表到关联表
    # pub=Publish.objects.get(name="深圳出版社")
    # print(pub)
    # Book.objects.create(name="人工智能",pub=pub)
    # Book.objects.create(name="大数据分析",pub=pub)

    #反向：从关联表到外建表
    pub_obj=Publish.objects.filter(name="北京出版社").first()
    pub_obj.book_set.create(name="GO语言入门")

    return  HttpResponse("一对多关系增加")

#一对多关系的查询
def onegetmore(request):
    #正常查询 深圳出版社出了哪些书
    # pub_obj=Publish.objects.filter(name="深圳出版社").first()
    # book_obj=Book.objects.filter(pub_id=pub_obj.id).all()#有没有all一样的返回queryset
    # print(book_obj)
    #GO语言是哪个出版社
    # book_obj=Book.objects.filter(name="GO语言入门").first()
    # pub_obj=Publish.objects.filter(id=book_obj.pub_id).first()
    # print(pub_obj)
    # print(pub_obj.name)

    #正向 html5网页技术属于哪个出版社
    # book_obj=Book.objects.filter(name="HTML5网页技术").first()
    # pub_obj=book_obj.pub
    # print(pub_obj)
    # print(pub_obj.name)

    #反向 成都出版社出版了哪些书
    pub_obj=Publish.objects.filter(name="四川出版社").first()
    print(pub_obj)
    book_obj=pub_obj.book_set.filter(id=2).values()
    print(book_obj)

    return  HttpResponse("一对多关系查询")

#一对多的修改
def oneupdatemore(request):
    #正向 修改某本书的出版社
    # pub_obj=Publish.objects.filter(name="北京出版社").first()
    # book_obj=Book.objects.filter(name="C#经典案例").update(pub=pub_obj)
    # print(book_obj)

    #反向 set中必须是对象
    pub_obj=Publish.objects.filter(name="深圳出版社").first()
    book_obj=Book.objects.filter(name="音乐大全").first()
    # book_obj1=Book.objects.filter(name="python全栈").first()
    obj=pub_obj.book_set.set([book_obj])
    print(obj)
    return  HttpResponse("一对多关系修改数据")


#一对多的删除
def onedelete(request):
    # pub_obj=Publish.objects.filter(name="北京出版社").delete()
    # print(pub_obj)
    book_obj=Book.objects.filter(name="人工智能").first().delete()
    print(book_obj)
    return  HttpResponse("一对多关系删除数据")