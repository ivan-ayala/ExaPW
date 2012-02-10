from django.db import models

class Models(models.Model):
	author = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	b_day = models.DateTimeField()
        
        def __unicode__(self):
		return ' %s' % ( self.author)
        
	
class Article(models.Model):
	title = models.CharField(max_length=50)
        author = models.ForeignKey('Models')
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add =True)
        tag = models.ManyToManyField('Tag')

class Comment(models.Model):
	name = models.CharField(max_length=50)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add =True)
	

class Tag(models.Model):
	name = models.CharField(max_length=50)
	deliver_mode= models.CharField(max_length=50)

        def __unicode__(self):
		return '%s' % ( self.name)
        
