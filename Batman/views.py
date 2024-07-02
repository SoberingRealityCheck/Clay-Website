from django.http import HttpResponse
from django.template import loader
from .models import Comment

def Home(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def George(request):
  template = loader.get_template('georgepage.html')
  return HttpResponse(template.render())

def Interactive(request):
  firstname = request.GET.get('fname')
  lastname = request.GET.get('lname')
  text = request.GET.get('comment_text')
  if firstname and lastname and text:
    print(firstname,lastname,text)
    new_comment = Comment(firstname=firstname,lastname=lastname,text=text)
    new_comment.save()
  mycomments = Comment.objects.all().values()
  template = loader.get_template('interactive.html')
  context = {
    'mycomments': mycomments,
  }
  return HttpResponse(template.render(context,request))

