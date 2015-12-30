from django.db import models

# Create a book model in the database
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    isbn = models.CharField(primary_key=True, max_length=30)
    published_year = models.CharField(max_length=4, blank=True)
    quantity = models.IntegerField(default=0)
    image_name = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    language = models.CharField(max_length=30, default='English')
    genre = models.CharField(max_length=50, default='fantasy')

    def __str__(self):
        return self.title
