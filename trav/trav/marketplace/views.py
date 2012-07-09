# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.shortcuts import get_object_or_404
from models import usr
from models import profile
from forms import LoginForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.views.generic import simple
from models import Product
def quiz_guess(request, user_id):   
  message = {"fname": "", "lname": ""}
  if request.is_ajax():
    user = get_object_or_404(usr, id=user_id)
    message['fname'] = user.firstname
    message['lname'] = user.lastname
  else:
    message = "You're the lying type, I can just tell."
  json = simplejson.dumps(message)
  return HttpResponse(json, mimetype='application/json')

def authenticate(request):
    csrf_exempt(authenticate)
    user=request.POST["username"]
    json=simplejson.dumps("")
    pwd=request.POST["password"]
    if(request.is_ajax()):
        u=usr.objects.get(username=user,password=pwd)
        if u is not None:
            request.session['userid'] = u.id
            message = {"uid": u.id, "uname": user,"status":"success"}
        else:
            message={"status": "fail"}
        json=simplejson.dumps(message)
    return HttpResponse(json,mimetype="application/json")

def signup(request):
    u=request.POST["username"]
    fname=request.POST["firstname"]
    lname=request.POST["lastname"]
    password=request.POST["password"]
    email=request.POST["email"]
    db=usr(username=u,firstname=fname,lastname=lname,password=password,email=email)
    db.save()
    request.session['userid'] = db.id
    msg="Sucess"
    return HttpResponse("")

def hello(request):
    csrf_exempt(hello)      
    form=LoginForm()
    return render_to_response('index.html',{'form':form}) 

def update(request):  
    return render_to_response('profile.html')

def updatepro(request):
    uid=request.session.get("userid")
    u=request.POST["plcvisited"]
    tv=request.POST["plctovisit"]
    fdb=request.POST["feedback"]
    p=profile(userid=uid,plcvisited=u,plctovisit=tv,user_feedback=fdb)
    p.save()
    return HttpResponseRedirect("/home")

def logout(request):
    del request.session['userid']
    html="<html><body>You are successfully logged out</body></html>"
    return HttpResponse(html)

def home(request):
    u=""
    if request.session.get("userid"):
        i=request.session.get("userid")
        u=usr.objects.get(id=i)
    return render_to_response('home.html',{'user':u})
    #html="<html><body>Hai ",u.username,"</body></html>"
    #return HttpResponse(html)
        
def show_object(request):
    return simple.direct_to_template(request, 'home.html', extra_context={'objects':Product.objects.all()})