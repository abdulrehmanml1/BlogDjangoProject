from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.


posts=[

{
'author':'Abdul Rehman',
'title':'Blog Title 1',
'content': "First blog content",
'date_posted':'Aug 28, 2021',

},
{
'author':'Daniyal',
'title':'Blog Title 2',
'content': "Second blog content",
'date_posted':'Aug 29, 2021',

},
{
'author':'Ammar',
'title':'Blog Title 3',
'content': "Third blog content",
'date_posted':'Aug 30, 2021',

}


]



#Home Function


def home(request):
	# return HttpResponse('<h1>Blog Home<h1/>')

	context={
		'posts':posts,
		'title':'Some Title Comes Here',
	}

	return render(request,'blog/home.html',context)   #rendering a template



 
def about(request):
	return render(request,"blog/about.html",{})
	# return HttpResponse("<h1>Blog About</h1>")  







