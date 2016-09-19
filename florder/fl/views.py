# -*- coding=utf-8 -*-
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Context
from django.core.exceptions import ObjectDoesNotExist
from fl.models import Seller, Dish, Table
from django.template.loader import render_to_string
import re
import time, datetime
import json
import MySQLdb
from django.core.paginator import Paginator
import unicodedata
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.hashers import make_password, check_password
from PIL import Image
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# Create your views here.
#用户
class UserForm(forms.Form):
    username = forms.CharField(label=u'用户名', max_length=30, error_messages={'required': u'请输入用户名'})
    password1 = forms.CharField(label=u'密码', widget=forms.PasswordInput(), error_messages={'required': u'请输入密码'})
    password2 = forms.CharField(label=u'确认密码', widget=forms.PasswordInput(), error_messages={'required': u'请重复密码'})
    email = forms.EmailField(label=u'邮箱', error_messages={'required': u'请输入邮箱'})
#登录
class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
#用户详细信息
class Modify(forms.Form):
    resname = forms.CharField()
    resaddress = forms.CharField()
    resphone = forms.CharField()
    #resphoto = forms.ImageField()
    resintroduce = forms.CharField(required=False)
    resopentime = forms.CharField()
    resnotice = forms.CharField(required=False)
    resother = forms.CharField(required=False)
class Userphoto(forms.Form):
    resphoto = forms.ImageField()
#pwd
class PwdForm(forms.Form):
    oldpwd = forms.CharField()
    newpwd = forms.CharField()
    newpwd1 = forms.CharField()
#菜品
class DishForm(forms.Form):
    dishname = forms.CharField()
    dishphoto = forms.ImageField(required=False)
    dishprice = forms.CharField()
    dishintroduce = forms.CharField(required=False)
    dishkind = forms.CharField(required=False)
#忘记密码
class ForgetpwdForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
#重置密码
class ResetpwdForm(forms.Form):
    password1 = forms.CharField()
    password2 = forms.CharField()
#餐桌
class TableForm(forms.Form):
    tablenum = forms.CharField()
    tableperson = forms.CharField()
#订单
#class OrderForm(forms.Form):
#    customer = forms.CharField()
#    time = forms.CharField()
def checkname(request, a):
    #print a
    if request.is_ajax():
        user = Seller.objects.filter(username=a)
        #print len(user)
        if len(user)>0:
            notice = "该用户名已注册！"
            r = HttpResponse(notice)
            return r
        elif not re.search(r'^([A-Za-z])(\w+)$', a):
            notice = "用户名不合规范！"
            r = HttpResponse(notice)
            return r
        else:
            notice = "输入正确"
            r = HttpResponse(notice)
            return r
    else:
        return HttpResponseRedirect('/fl/login')
def checkemail(request, a):
    if request.is_ajax():
        #print a
        email = Seller.objects.filter(email=a)
        if len(email)>0:
            notice = "邮箱已存在！"
            r = HttpResponse(notice)
            return r
        elif not re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b',a):
            notice = "请输入正确邮箱！"
            r = HttpResponse(notice)
            return r
        else:
            notice = "输入正确"
            r = HttpResponse(notice)
            return r
    else:
        return HttpResponseRedirect('/fl/login')
def checkdish(request, a):
    if request.is_ajax():
        #print a
        username = request.COOKIES['username']
        #print username
        dish = Dish.objects.filter(dishname=a,username=username)
        if len(dish)>0:
            notice = "菜品已存在！"
            r = HttpResponse(notice)
            return r
        else:
            notice = ""
            r = HttpResponse(notice)
            return r
    else:
        return HttpResponseRedirect('/fl/login')
#注册
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password1 = uf.cleaned_data['password1']
            password2 = uf.cleaned_data['password2']
            email = uf.cleaned_data['email']
            errors = []
            usernumber = Seller.objects.filter(username=username)
            emailnumber = Seller.objects.filter(email=email)
            if not re.search(r'^([A-Za-z])(\w+)$', username):
                errors.append('用户名不合规范！')
                #uf = UserForm()
                return render_to_response('register2.html',{'errors':errors[0]})
                #return render_to_response('register.html',{'uf':uf, 'errors1':username_errors[0]})
            elif len(usernumber)>0:
                errors.append('用户名已存在！')
                return render_to_response('register2.html',{'errors':errors[0]})
                #uf = UserForm()
                #return render_to_response('register.html',{'uf':uf, 'errors1':username_errors[0]})
            elif len(password1)<6:
                errors.append('密码至少为6位')
                return render_to_response('register2.html',{'errors':errors[0]})
            elif len(emailnumber)>0:
                errors.append('邮箱已存在！')
                return render_to_response('register2.html',{'errors':errors[0]})
                #uf = UserForm()
                #return render_to_response('register.html',{'uf':uf, 'errors2':email_errors[0]})
            elif password1 != password2:
                errors.append('两次密码不相同！')
                return render_to_response('register2.html',{'errors':errors[0]})
                #uf = UserForm()
                #return render_to_response('register.html',{'uf':uf, 'errors3':password_errors[0]})
            else:
                user = Seller()
                user.username = username
                user.password = password1
                user.email = email
                user.save()
                userinfo = Seller.objects.filter(username=username)
                userid = userinfo[0].id
                seller = userid + 10000
                userinfo.update(seller=seller)
                errors = []
                errors.append("注册成功，请重新登录！")
                return render_to_response('business/login.html', {'errors': errors[0]})
        else:
            errors = []
            errors.append("填写信息不完整！")
            return render_to_response('register2.html', {'errors': errors[0]})
    else:
        #return render_to_response('register1.html')
        return render_to_response('register2.html')
        #return render_to_response('register1.html', {'uf': uf}, context_instance=RequestContext(request))
#登录
def login(request):
    if request.method == "POST":
        af = Login(request.POST)
        if af.is_valid():
            username = af.cleaned_data['username']
            password = af.cleaned_data['password']
            errors = []
            #print username
            #print password
            user = Seller.objects.filter(username=username, password=password)
            if user:
                response = HttpResponseRedirect('/fl/index/')
                seller = user[0].seller
                response.set_cookie('username',username)
                response.set_cookie('seller',seller)
                #a = response.cookies["username"]
                #print a
                return response
            else:
                errors.append('您输入的密码有误！')
                #print email_errors
                return render_to_response('business/login.html', {'errors': errors[0]})
        else:
            errors = []
            errors.append("您输入的密码有误！")
            return render_to_response('business/login.html', {'errors': errors[0]})
    else:
        return render_to_response('login.html')

#忘记密码
def forgetpwd(request):
    return render_to_response('business/forgetpwd.html')

#发送修改密码邮件
def sendpwdemail(request):
    if request.method == "POST":
        bf = ForgetpwdForm(request.POST)
        if bf.is_valid():
            username = bf.cleaned_data['username']
            email = bf.cleaned_data['email']
            errors = []
            user = Seller.objects.filter(username=username, email=email)
            if user:
                datetime1 = datetime.datetime.now()
                datetime2 = make_password(datetime1, None, 'pbkdf2_sha256')
                subject, from_email = 'flavor-order||忘记密码', '18700195768@163.com'
                text_content = 'flavor-order账户'
                dic = {'home': username, 'body': email, 'md': datetime2}
                html_content = render_to_string('business/sendemail.html', dic)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                user.update(isfgpwd=True)
                return HttpResponseRedirect('/fl/login')
            else:
                errors.append("您输入的信息错误！")
                return render_to_response('business/forgetpwd.html', {'errors':errors[0]})
        else:
            errors = []
            errors.append("您输入的信息错误！")
            return render_to_response('business/forgetpwd.html', {'errors':errors[0]})
    return HttpResponseRedirect('/fl/login')

#忘记密码时重置密码
def fgpwdreset(request):
    if "home" and "body" in request.GET:
        username = request.GET["home"]
        email = request.GET["body"]
        if username and email:
            user = Seller.objects.filter(username=username, email=email)
            if user[0].isfgpwd == False:
                errors = []
                errors.append("您的链接已失效，请重新生成！")
                return render_to_response('business/login.html', {'errors':errors[0]})
            else:
                user.update(isfgpwd=False)
                response = HttpResponseRedirect('/fl/showresetpwd')
                response.set_cookie('username1',user[0].username)
                return response
        else:
            return HttpResponseRedirect('/fl/login')
    else:
        return HttpResponseRedirect('/fl/login')

#重置密码页
def showresetpwd(request):
    if "username1" in request.COOKIES:
        return render_to_response('business/resetpwd.html')
    else:
        return HttpResponseRedirect('/fl/login')

#重置密码
def resetpwd(request):
    if request.method == "POST":
        pwd = ResetpwdForm(request.POST)
        if pwd.is_valid():
            password1 = pwd.cleaned_data['password1']
            password2 = pwd.cleaned_data['password2']
            errors = []
            if password1 == password2:
                errors.append("密码重置成功，请重新登录！")
                a = request.COOKIES["username1"]
                user = Seller.objects.filter(username=a)
                user.update(password=password1)
                return render_to_response('business/login.html', {'errors':errors[0]})
            else:
                errors.append("两次密码不相同，请重新输入！")
                return render_to_response('business/resetpwd.html', {'errors':errors[0]})
        else:
            errors = []
            errors.append("信息输入不完整！")
            return render_to_response('business/resetpwd.html', {'errors':errors[0]})
    else:
        return HttpResponseRedirect('/fl/login')

#登陆成功
def index(request):
    username = request.COOKIES.get('username', '')
    if username:
        userinfo = Seller.objects.filter(username=username)
        userid = userinfo[0].seller
        photo = userinfo[0].resphoto.name
        userphoto = '/static/images/resphoto/thumbnail/' + photo
        return render_to_response('business/index.html', {'username':username,'userid':userid,'userphoto':userphoto})
    else:
        return HttpResponseRedirect('/fl/login')

#退出
def logout(request):
    response = HttpResponseRedirect('/fl/login')
    response.delete_cookie('username')
    response.delete_cookie('seller')
    return response
#查看个人信息
def show(request):
    if "username" in request.COOKIES:
        a = request.COOKIES["username"]
        userinfo = Seller.objects.filter(username=a)
        #cc = userinfo[0].username
        return render_to_response('business/modify.html', {'username':userinfo})
    else:
        return HttpResponseRedirect('/fl/login')
#查看密码
def showpwd(request):
    if "username" in request.COOKIES:
        a = request.COOKIES["username"]
        userinfo = Seller.objects.filter(username=a)
        return render_to_response('business/modifypwd.html', {'username':userinfo})
    else:
        return HttpResponseRedirect('/fl/login')
#修改密码
def modifypwd(request):
    if request.method == "POST":
        bf = PwdForm(request.POST)
        if bf.is_valid():
            oldpwd = bf.cleaned_data['oldpwd']
            newpwd = bf.cleaned_data['newpwd']
            newpwd1 = bf.cleaned_data['newpwd1']
            errors = []
            a = request.COOKIES["username"]
            user = Seller.objects.filter(username=a, password=oldpwd)
            userinfo = Seller.objects.filter(username=a)
            if user:
                if newpwd == newpwd1:
                    user.update(password=newpwd)
                    errors.append("密码已重置，请重新登录！")
                    return render_to_response('business/login.html', {'errors':errors[0]})
                else:
                    errors.append("新密码两次输入不一致！")
                    dic = {'errors':errors[0], 'username':userinfo}
                    return render_to_response('business/modifypwd.html', dic)
            else:
                errors.append("原密码输入错误！")

                dic = {'errors':errors[0], 'username':userinfo}
                return render_to_response('business/modifypwd.html', dic)
        else:
            errors = []
            a = request.COOKIES["username"]
            userinfo = Seller.objects.filter(username=a)
            errors.append("请输入完整信息！")
            dic = {'errors':errors[0], 'username':userinfo}
            return render_to_response('business/modifypwd.html', dic)
    else:
        return HttpResponseRedirect('/fl/login')


#修改个人信息
def modify(request):
    if request.method == "POST":
        bf = Modify(request.POST)
        if bf.is_valid():
            resname = bf.cleaned_data['resname']
            resaddress = bf.cleaned_data['resaddress']
            resphone = bf.cleaned_data['resphone']
            #resphoto = bf.cleaned_data['resphoto']
            resintroduce = bf.cleaned_data['resintroduce']
            resopentime = bf.cleaned_data['resopentime']
            resnotice = bf.cleaned_data['resnotice']
            resother = bf.cleaned_data['resother']
            #print resname
            #print resaddress
            b = request.COOKIES["username"]
            #print b
            Seller.objects.filter(username=b).update(resname=resname, resaddress=resaddress,
                                                   resphone=resphone, resintroduce=resintroduce,
                                                   resopentime=resopentime, resnotice=resnotice, resother=resother)
        else:
            resname = request.POST["resname"]
            resaddress = request.POST["resaddress"]
            resphone = request.POST["resphone"]
            resopentime = request.POST["resopentime"]
            errors = []
            a = request.COOKIES["username"]
            userinfo = Seller.objects.filter(username=a)
            if resname == '':
                errors.append("饭店名不能为空！")
            elif resaddress == '':
                errors.append("饭店地址不能为空！")
            elif resphone == '':
                errors.append("饭店电话不能为空！")
            elif resopentime == '':
                errors.append("营业时间不能为空！")
            dic = {'username':userinfo, 'errors':errors[0]}
            return render_to_response('business/modify.html', dic)
    return HttpResponseRedirect('/fl/index')
#展示头像
def showuserphoto(request):
    if "username" and "seller" in request.COOKIES:
        a = request.COOKIES["username"]
        userinfo = Seller.objects.filter(username=a)
        photo = userinfo[0].resphoto
        #print photo
        photourl = '/static/images/resphoto/thumbnail/' + photo.name
        #print photourl
        return render_to_response('business/showuserphoto.html', {'resphoto':photourl, 'username':userinfo})
    else:
        return HttpResponseRedirect('/fl/index')
#更换商户图标
def resetuserphoto(request):
    if "username" and "seller" in request.COOKIES:
        if "resphoto" in request.FILES:
            if request.method == "POST":
                photo = Userphoto(request.POST, request.FILES)
                if photo.is_valid():
                    username = request.COOKIES["username"]
                    resphoto = request.FILES["resphoto"]
                    Seller.objects.filter(username=username).update(resphoto=resphoto)
                    img = Image.open(resphoto)
                    img = img.convert('RGB')
                    img1 = img.resize((100, 100), Image.ANTIALIAS)
                    url = 'resphoto/thumbnail/' + resphoto.name
                    name = 'E:/florder/media/images/' + url
                    img1.save(name, "jpeg")
                    url1 = 'resphoto/original/' + resphoto.name
                    name1 = 'E:/florder/media/images/' + url1
                    img.save(name1, "jpeg")
                    return HttpResponseRedirect('/fl/index')
                    #return render_to_response('business/index.html', {'username':username})
                else:
                    username = request.COOKIES["username"]
                    return render_to_response('business/index.html', {'username':username})
        else:
            return HttpResponseRedirect('/fl/index')
    else:
        return HttpResponseRedirect('/fl/login')
def showadddish(request):
    if "username" and "seller" in request.COOKIES:
        return render_to_response('business/adddish.html')
    else:
        return HttpResponseRedirect('/fl/index')


#添加菜品
def adddish(request):
    if "username" and "seller" in request.COOKIES:
        if request.method == "POST":
            dish1 = DishForm(request.POST, request.FILES)
            if dish1.is_valid():
                dishname = dish1.cleaned_data['dishname']
                seller = request.COOKIES["seller"]
                dishexist = Dish.objects.filter(dishname=dishname,seller=seller)
                if dishexist:
                    errors = []
                    errors.append("菜品已存在！")
                    return render_to_response('adddish.html', {'errors':errors[0]})
                else:
                    dishprice = dish1.cleaned_data['dishprice']
                    dishintroduce = dish1.cleaned_data['dishintroduce']
                    dishkind = dish1.cleaned_data['dishkind']
                    dishphoto = request.FILES["dishphoto"]
                    username = request.COOKIES["username"]
                    #seller = request.COOKIES["seller"]
                    img = Image.open(dishphoto)
                    img = img.convert('RGB')
                    img1 = img.resize((40, 40), Image.ANTIALIAS)
                    url = 'dishphoto/thumbnail/' + dishphoto.name
                    name = 'E:/florder/media/images/' + url
                    img1.save(name, "jpeg")
                    url1 = 'dishphoto/original/' + dishphoto.name
                    name1 = 'E:/florder/media/images/' + url1
                    img.save(name1, "jpeg")
                    img2 = img.resize((150, 150), Image.ANTIALIAS)
                    url2 = 'dishphoto/medium/' + dishphoto.name
                    name2 = 'E:/florder/media/images/' + url2
                    img2.save(name2, "jpeg")
                    #print dishphoto.name
                    Dish.objects.create(seller=seller, username=username, dishname=dishname, dishprice=dishprice,
                                        dishintroduce=dishintroduce, dishkind=dishkind, dishphoto=dishphoto.name)

                    return HttpResponseRedirect('/fl/showdish')
            else:
                dishname = request.POST["dishname"]
                dishprice = request.POST["dishprice"]
                errors = []
                if dishname == '':
                    errors.append("菜品名称不能为空！")
                elif dishprice == '':
                    errors.append("菜品价格不能为空！")
                return render_to_response('adddish.html', {'errors':errors[0]})
        else:
            return HttpResponseRedirect('/fl/index')
    else:
        return HttpResponseRedirect('/fl/login')
        #return render_to_response('business/adddish.html')
#查看菜品
def showdish(request):
    if "username" and "seller" in request.COOKIES:

        username = request.COOKIES["username"]
        dishlist = Dish.objects.filter(username=username)
        objects, page_range = my_pagination(request, dishlist,6)
    #print dishlist[0].dishphoto
    #t = loader.get_template("showdish.html")
    #c = Context(locals())
    #return HttpResponse(t.render(c))
        return render_to_response('showdish.html', {'objects':objects,'page_range':page_range},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/fl/login')

#删除菜品
def deletedish(request):
    if "id" in request.GET:
        dishid = request.GET["id"]
        #print dishid
        Dish.objects.filter(id=dishid).delete()
        return HttpResponseRedirect('/fl/showdish')
    else:
        return HttpResponseRedirect('/fl/login')

#展示要修改的菜品
def showmodifydish(request):
    if "id" in request.GET:
        dishid = request.GET["id"]
        dishinfo = Dish.objects.filter(id=dishid)
        dishkind1 = dishinfo[0].dishkind
        #print dishkind1
        dishkind = [dishkind1]
        photo = dishinfo[0].dishphoto
        photourl = '/static/images/dishphoto/medium/' + photo.name
        return render_to_response('business/showmodifydish.html', {'dish':dishinfo, 'dishkind': json.dumps(dishkind), 'dishphoto': photourl})
    else:
        return HttpResponseRedirect('/fl/login')
#修改菜品
def modifydish(request):
    if "username" and "seller" in request.COOKIES:
        if request.method == "POST":
            bf = DishForm(request.POST, request.FILES)
            if bf.is_valid():
                #print '123'
                try:
                    dishname = bf.cleaned_data['dishname']
                    dishprice = bf.cleaned_data['dishprice']
                    dishintroduce = bf.cleaned_data['dishintroduce']
                    dishphoto = request.FILES["dishphoto"]
                    dishkind = bf.cleaned_data['dishkind']
                    img = Image.open(dishphoto)
                    img = img.convert('RGB')
                    img1 = img.resize((40, 40), Image.ANTIALIAS)
                    url = 'dishphoto/thumbnail/' + dishphoto.name
                    name = 'E:/florder/media/images/' + url
                    img1.save(name, "jpeg")
                    url1 = 'dishphoto/original/' + dishphoto.name
                    name1 = 'E:/florder/media/images/' + url1
                    img.save(name1, "jpeg")
                    img2 = img.resize((150, 150), Image.ANTIALIAS)
                    url2 = 'dishphoto/medium/' + dishphoto.name
                    name2 = 'E:/florder/media/images/' + url2
                    img2.save(name2, "jpeg")
                    dishid = request.GET["id"]
                    Dish.objects.filter(id=dishid).update(dishname=dishname, dishprice=dishprice,
                                                          dishintroduce=dishintroduce, dishkind=dishkind, dishphoto=dishphoto.name)
                    return HttpResponseRedirect('/fl/showdish')
                except KeyError:

                    dishname = bf.cleaned_data['dishname']
                    dishprice = bf.cleaned_data['dishprice']
                    dishintroduce = bf.cleaned_data['dishintroduce']
                    #dishphoto = request.FILES["dishphoto"]
                    dishkind = bf.cleaned_data['dishkind']
                    #img = Image.open(dishphoto)
                    #img1 = img.resize((40, 40), Image.ANTIALIAS)
                    #url = 'dishphoto/thumbnail/' + dishphoto.name
                    #name = 'E:/order/media/images/' + url
                    #img1.save(name, "jpeg")
                    #url1 = 'dishphoto/original/' + dishphoto.name
                    #name1 = 'E:/order/media/images/' + url1
                    #img.save(name1, "jpeg")
                    #print dishname
                    #print dishprice
                    dishid = request.GET["id"]
                    #print dishid
                    Dish.objects.filter(id=dishid).update(dishname=dishname, dishprice=dishprice,
                                                          dishintroduce=dishintroduce, dishkind=dishkind)
                    return HttpResponseRedirect('/fl/showdish')
            else:
                return HttpResponseRedirect('/fl/showdish')
        else:
            return HttpResponseRedirect('/fl/login')
    else:
        return HttpResponseRedirect('/fl/login')

def showaddtable(request):
    if "username" and "seller" in request.COOKIES:
        return render_to_response('business/addtable.html')
    else:
        return HttpResponseRedirect('/fl/login')

#添加餐桌
def addtable(request):
    if "username" and "seller" in request.COOKIES:
        if request.method == "POST":
            table1 = TableForm(request.POST)
            if table1.is_valid():
                tablenum = table1.cleaned_data['tablenum']
                tableperson = table1.cleaned_data['tableperson']
                username = request.COOKIES["username"]
                seller = request.COOKIES["seller"]
                tableexist = Table.objects.filter(tablenum=tablenum,seller=seller)
                if tableexist:
                    errors = []
                    errors.append("桌号已存在！")
                    return render_to_response('business/addtable.html', {'errors':errors[0]})
                else:
                    if tablenum != '' and tableperson != '':
                        #print username, dishname, dishprice, dishintroduce, dishkind
                        Table.objects.create(seller=seller, username=username, tablenum=tablenum, tableperson=tableperson)
                        return HttpResponseRedirect('/fl/showtable')
            else:
                tablenum = request.POST["tablenum"]
                tableperson = request.POST['tableperson']
                errors = []
                if tablenum == '':
                    errors.append("桌号不能为空")
                elif tableperson == '':
                    errors.append("人数不能为空")
                return render_to_response('business/addtable.html', {'errors':errors[0]})
        else:
            return HttpResponseRedirect('/fl/index')
    else:
        return HttpResponseRedirect('/fl/index')
#查看餐桌
def showtable(request):
    if "username" and "seller" in request.COOKIES:
        username = request.COOKIES["username"]
        tablelist = Table.objects.filter(username=username)
        objects, page_range = my_pagination(request, tablelist,6)
        #t = loader.get_template("showdish.html")
        #c = Context(locals())
        #return HttpResponse(t.render(c))
        return render_to_response('showtable.html', {'objects':objects,'page_range':page_range},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/fl/index')
#删除餐桌
def deletetable(request):
    if "id" in request.GET:
        tableid = request.GET["id"]
        #print dishid
        Table.objects.filter(id=tableid).delete()
        return HttpResponseRedirect('/fl/showtable')
    else:
        return HttpResponseRedirect('/fl/index')

#到店订单
def online(request):
    if "username" and "seller" in request.COOKIES:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='florder')
        cursor = conn.cursor()
        seller = '111'
        #sql = "select seller from fl_order where seller= %s",(seller)
        cursor.execute("SELECT * FROM fl_order WHERE seller= %s AND subscribe=%s AND status=%s",(seller,0,0))
        data = cursor.fetchall()

        multilist = [[0 for col in range(5)] for row in range(len(data))]

        m=[]
        for i in range(len(data)):
            multilist[i][0] = data[i][0]
            #print data[i][0]
            multilist[i][1] = data[i][2]
            timearray = time.localtime(data[i][7])
            otherstytime = time.strftime("%Y-%m-%d %H:%M:%S", timearray)
            #print otherstytime
            multilist[i][2] = otherstytime
            multilist[i][4] = data[i][10]
            m.append(data[i][3])

        for k in range(len(data)):
            a = m[k].split(",")
            dishinfo = ""
            for j in range(len(a)):
                b = a[j].split("-")
                dish = Dish.objects.filter(id=b[0])
                dishinfo += dish[0].dishname
                dishinfo += b[1]
                dishinfo += u"份"
                dishinfo += "\n"
            multilist[k][3] = dishinfo.encode("utf-8")
        cursor.close()
        conn.close()
        objects, page_range = my_pagination(request, multilist,8)
        return render_to_response('onlineorder.html',{'objects':objects,'page_range':page_range},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/fl/login')
#完成订单任务
def finishorder(request):
    if "id" in request.GET:
        idstr = request.GET["id"]
        detial = idstr[1:-1]
        tuple1 = detial.split(",")
        fromid = str(tuple1[0])
        changeid = fromid[:-1]
        orderid = int(changeid)
        #print orderid
        table_id = tuple1[1]
        #print table_id
        conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='florder')
        cursor = conn.cursor()
        seller = '111'
        updatetime = int(time.time())
        cursor.execute("UPDATE fl_order SET status= %s,finish_time= %s WHERE seller= %s AND table_id=%s AND subscribe=%s AND id=%s",(1,updatetime,seller,table_id,0,orderid))
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponseRedirect('/fl/online')
    else:
        return HttpResponseRedirect('/fl/login')
def print_order(request):
    if "id" in request.GET:
        idstr = request.GET["id"]
        detial = idstr[1:-1]
        tuple1 = detial.split(",")
        #print tuple1
        fromid = str(tuple1[0])
        changeid = fromid[:-1]
        orderid = int(changeid)
        tableid = tuple1[1]
        #oriordertime = str(tuple1[2])
        #ordertime = oriordertime[2:-1]
        #print ordertime
        conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='florder')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM fl_order WHERE id= %s",(orderid))
        data = cursor.fetchall()
        data1= data[0][3]
        oriorder = data1.split(",")
        #print len(oriorder)
        #dishinfo = []
        #dishnum = []
        multilist = [[0 for col in range(2)] for row in range(len(oriorder))]
        for i in range(len(oriorder)):
            changeorder = oriorder[i].split("-")
            #print changeorder
            dish = Dish.objects.get(id=changeorder[0])
            multilist[i][0]=dish.dishname.decode("utf-8")
            multilist[i][1]=changeorder[1].decode("utf-8")
            #dishinfo.append(dish.dishname)
            #dishinfo.append(changeorder[1])
        #print dishinfo
        #print multilist
        #return HttpResponse(dishnum)
        return render_to_response("print_order.html",{'multilist':multilist,'tableid':tableid},context_instance=RequestContext(request))


#预约订单
def subscribe(request):
    if "username" and "seller" in request.COOKIES:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='florder')
        cursor = conn.cursor()
        seller = '111'
        cursor.execute("SELECT * FROM fl_order WHERE seller= %s AND subscribe=%s AND status=%s",(seller,1,0))
        data = cursor.fetchall()
        #print data[0][0]
        multilist = [[0 for col in range(8)] for row in range(len(data))]
        m=[]
        for i in range(len(data)):
            #multilist[i][0] = data[i][0] + 10000
            multilist[i][0] = data[i][0]
            multilist[i][1] = data[i][2]
            customernum = data[i][4]
            #cursor1 = conn.cursor()
            cursor.execute("SELECT * FROM fl_customer WHERE id=%s",(customernum))
            customerdata = cursor.fetchall()
            #print customerdata[0][1]
            multilist[i][2] = customerdata[0][1]
            multilist[i][3] = customerdata[0][2]
            timearray = time.localtime(data[i][7])
            otherstytime = time.strftime("%Y-%m-%d %H:%M", timearray)
            multilist[i][4] = otherstytime
            timearray1 = time.localtime(data[i][6])
            otherstytime1 = time.strftime("%Y-%m-%d %H:%M", timearray1)
            multilist[i][5] = otherstytime1
            multilist[i][7] = data[i][10]
            m.append(data[i][3])
        for k in range(len(data)):
            a = m[k].split(",")
            dishinfo = ""
            for j in range(len(a)):
                b = a[j].split("-")
                dish = Dish.objects.filter(id=b[0])
                dishinfo += dish[0].dishname
                dishinfo += b[1]
                dishinfo += u"份"
                dishinfo += "\n"
            multilist[k][6] = dishinfo.encode("utf-8")
        cursor.close()
        conn.close()
        objects, page_range = my_pagination(request, multilist,8)
        return render_to_response('subscribe.html',{'objects':objects,'page_range':page_range},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/fl/login')

def finishsubscribeorder(request):
    if "id" in request.GET:
        idstr = request.GET["id"]
        detial = idstr[1:-1]
        tuple1 = detial.split(",")
        fromid = str(tuple1[0])
        changeid = fromid[:-1]
        #orderid = int(changeid)-10000
        orderid = int(changeid)
        #print orderid
        table_id = tuple1[1]
        #print table_id
        conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='florder')
        cursor = conn.cursor()
        seller = '111'
        updatetime = int(time.time())
        cursor.execute("UPDATE fl_order SET status= %s,finish_time= %s WHERE seller= %s AND table_id=%s AND subscribe=%s AND id=%s",(1,updatetime,seller,table_id,1,orderid))
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponseRedirect('/fl/subscribe')
    else:
        return HttpResponseRedirect('/fl/login')

#历史所有订单
def history(request):
    if "username" and "seller" in request.COOKIES:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='florder')
        cursor = conn.cursor()
        seller = '111'
        cursor.execute("SELECT * FROM fl_order WHERE seller= %s AND status=%s",(seller,1))
        data = cursor.fetchall()
        multilist = [[0 for col in range(3)] for row in range(len(data))]
        m=[]
        for i in range(len(data)):
            multilist[i][2] = data[i][10]
            timearray = time.localtime(data[i][9])
            otherstytime = time.strftime("%Y-%m-%d", timearray)
            multilist[i][0] = otherstytime
            m.append(data[i][3])
        for k in range(len(data)):
            a = m[k].split(",")
            dishinfo = ""
            for j in range(len(a)):
                b = a[j].split("-")
                dish = Dish.objects.filter(id=b[0])
                dishinfo += dish[0].dishname
                dishinfo += b[1]
                dishinfo += u"份"
                dishinfo += "\n"
            multilist[k][1] = dishinfo.encode("utf-8")
        cursor.close()
        conn.close()
        objects, page_range = my_pagination(request, multilist,10)
        #p = Paginator(multilist,2)
        #print p.page(1).object_list
        #print p.num_pages
        #print p.page(8)
        return render_to_response('history.html',{'objects':objects,'page_range':page_range},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/fl/index')
#查询订单样式
def showfindorder(request):
    if "username" and "seller" in request.COOKIES:
        a = request.COOKIES["username"]
        userinfo = Seller.objects.filter(username=a)
        return render_to_response('business/showfindorder.html', {'username':userinfo})
    else:
        return HttpResponseRedirect('/fl/index')

def findorder(request):
    if "username" and "seller" in request.COOKIES:
        if "reservation" in request.POST:
            time1 = request.POST["reservation"]
            response = HttpResponseRedirect('/fl/findorder/')
            response.set_cookie('time1',time1)
            return response
        else:
            time1 = request.COOKIES["time1"]
        #if "time1" in request.COOKIES:
        #    time1 = request.COOKIES["time1"]
        #else:
        #    time1 = request.POST["reservation"]
        #    response = HttpResponseRedirect('/fl/findorder/')
        #    response.set_cookie('time1',time1)
        #    return response
        #print time1
        timebegin = time1[0:10]
        timeend = time1[13:]
        unixtimebegin = int(time.mktime(time.strptime(timebegin, '%Y-%m-%d')))
        unixtimeend = int(time.mktime(time.strptime(timeend, '%Y-%m-%d'))+86400)
        #print unixtimebegin
        #print unixtimeend
        conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='florder')
        cursor = conn.cursor()
        seller = '111'
        cursor.execute("SELECT * FROM fl_order WHERE seller= %s AND status=%s AND finish_time BETWEEN %s AND %s",(seller,1,unixtimebegin,unixtimeend))
        data = cursor.fetchall()
        multilist = [[0 for col in range(3)] for row in range(len(data))]
        m=[]
        for i in range(len(data)):
            multilist[i][2] = data[i][10]
            timearray = time.localtime(data[i][9])
            otherstytime = time.strftime("%Y-%m-%d", timearray)
            multilist[i][0] = otherstytime
            m.append(data[i][3])
        for k in range(len(data)):
            a = m[k].split(",")
            dishinfo = ""
            for j in range(len(a)):
                b = a[j].split("-")
                dish = Dish.objects.filter(id=b[0])
                dishinfo += dish[0].dishname
                dishinfo += b[1]
                dishinfo += u"份"
                dishinfo += "\n"
            multilist[k][1] = dishinfo.encode("utf-8")
        cursor.close()
        conn.close()
        objects, page_range = my_pagination(request, multilist,10)
        return render_to_response('select_history.html',{'objects':objects,'page_range':page_range},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/fl/login')

def my_pagination(request, queryset, display_amount, after_range_num=3, bevor_range_num=2):
    paginator = Paginator(queryset,display_amount)
    try:
        page = int(request.GET["page"])
    except:
        page = 1
    try:
        object = paginator.page(page)
    except EmptyPage:
        object = paginator.page(paginator.num_pages)
    except:
        object = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]
    else:
        page_range = paginator.page_range[0:page+bevor_range_num]
    return object,page_range

def testname(request, gradename):
    name = gradename
    if name == "111":
        r = 1
        return r

