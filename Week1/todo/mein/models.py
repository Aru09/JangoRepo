from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    website = models.URLField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
    	return "#{}: {}".format(self.id, self.name)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
