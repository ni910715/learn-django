from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

# 定義不同網址時所看到的畫面
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST) # response.POST會返回在form中的所有key value成一個字典

        if form.is_valid():
            n = form.cleaned_data["name"] # cleaned_data解密 並使用字典的方式取出name的value
            t = ToDoList(name = n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id) # 重新導向新的url
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})