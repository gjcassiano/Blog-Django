from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Comentario,Post
from django.contrib.auth import authenticate, login, logout

username = 'someone'
password = ''

def formulario_buscar(request):
	return render(request, 'formulario_buscar.html')	

def formulario_mostrar(request):
	latest_question_list = Comentario.objects.order_by('-nome')[:5]

	context = {'latest_question_list': latest_question_list}
	return render(request, 'formulario_mostrar.html', context)

def posts(request,num = -1):
	global username,password
	#try of login user
	user = None
	if  request.method == 'POST':
		logout(request)
		username = password = ''
		if request.POST:
		    username = request.POST['username']
		    password = request.POST['passwd']
		    print username,password

		    user = authenticate(username=username, password=password)
		    if user is not None:
		        if user.is_active:
		            login(request)
		            #login acepted

	if num <= 0:
		posts_list = Post.objects.order_by('-post_id')[:5]
		for post in posts_list:
			if len(post.texto) >120:
				post.texto = post.texto[:120] + "..."
	else:
		try:
			posts_list = Post.objects.filter(post_id=num)
		except:
			print "[except in posts views !]"
			posts_list = Post.objects.order_by('-post_id')[:5]
	
	context = {'posts_list':posts_list}
	if user!=None:
		context = {'posts_list':posts_list,'user':username}
	

	return render(request,'posts.html',context)

def login(request):
	return render(request,'login.html')


