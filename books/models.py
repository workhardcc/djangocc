from django.db import models,connection

class book_sql(models.Manager):
    def first_names(self):
	cursor = connection.cursor()
	cursor.execute("""
		select * from books_book""")
	return [row[0] for row in cursor.fetchone()]
class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()
    #def filter_xx(self,keyword):
	#return self.filter(title__icontains=keyword).title()
class Title_Manager(models.Manager):
    def get_query_set(self):
        return super(Title_Manager, self).get_query_set().filter(title='a')


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __unicode__(self):
	return self.name
    class Meta:
	ordering=['address']

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    marriage = models.CharField(max_length=10)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
   # original=models.Manager()
    objects = book_sql()
    
   # xx=Title_Manager()
    def __unicode__(self):
	return self.title
