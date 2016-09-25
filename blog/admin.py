from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-
from blog.models import Comentario,Post
from django.contrib import admin

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('nome','email')


class PostAdmin(admin.ModelAdmin):
	list_display = ('post_id','title','date')

admin.site.register(Comentario,ComentarioAdmin)
admin.site.register(Post,PostAdmin)
