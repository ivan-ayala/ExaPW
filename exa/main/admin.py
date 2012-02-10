from django.contrib import admin
from main.models import Models, Article,Comment, Tag

class ModelsAdmin(admin.ModelAdmin):
	search_fields=['author']
	list_display=['author', 'name','last_name','b_day']

class ArticleAdmin(admin.ModelAdmin):
	search_fields=['title']
	list_display=['title', 'author','body']

class CommentAdmin(admin.ModelAdmin):
	search_fields=['name']
	list_display=[ 'name','text']

class TagAdmin(admin.ModelAdmin):
	search_fields=['name']
	list_display=['name','deliver_mode']


admin.site.register(Models, ModelsAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)

#este archivo se debe de guardar en la carpeta main
