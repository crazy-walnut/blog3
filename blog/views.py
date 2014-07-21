from django.shortcuts import render_to_response
from django.http import HttpResponse
from blog.models import User
from django import forms
import datetime

# Create your views here.
class UserForm(forms.Form):
	username = forms.CharField(max_length = 30)
	headImg  = forms.FileField()

	
class UserForm1(forms.Form):
	username = forms.CharField(max_length = 30)
def search(request):
	if request.method == 'POST' :
		uf = UserForm1(request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			print username
			user = User()
			user.name  =username
			book_list=User.objects.filter(name__istartswith = user.name)
			return render_to_response('search_form.html',{'uf':uf,'book_list':book_list})	
	else:
		uf = UserForm1()
	return render_to_response('search_form.html',{'uf':uf})
	
def register(request):
	if request.method == "POST" :
		uf = UserForm(request.POST,request.FILES)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			headImg  = uf.cleaned_data['headImg']
			user = User()
			user.name    =username
			user.headImg =headImg
			user.save()
			print username,headImg
			ua = request.META.get('HTTP_USER_AGENT', 'unknown')
			return HttpResponse("Your browser is %s" % ua)
	else :
		uf = UserForm()
	return render_to_response('register.html',{'uf':uf,'title':'baba'})
	
def biaoqian(request):
	user={'name':'ysh','age':12}
	
	book_list=User.objects.order_by('name')
	return render_to_response('biaoqian.html',{'user':user,'book_list':book_list})


#quary databsae
class UserForm(forms.Form):
	username = forms.CharField()
	headImg  = forms.FileField()
	

	


		
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
	
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            print errors.append('Enter a subject.')

        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
			
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
			
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', '`noreply@example.com`_'),
                ['`siteowner@example.com`_'],
            )
            return HttpResponseRedirect('/contact_form/')
    return render_to_response('contact_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })
def bootstrap(request):
	return render_to_response('bootstrap.html','')
	
def blog(request):
	return render_to_response('blog.html')	

def login(request):
	return render_to_response('login.html','')	