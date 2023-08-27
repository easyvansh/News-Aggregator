from django.db import models

# Create your models here.
class Headline(models.Model):
#   Database to store the title of the article
  title = models.CharField(max_length=200)
#   Database to store the image 
  image = models.URLField(null=True, blank=True)
#   Database to store the url 
  url = models.TextField()
  def __str__(self):
    return self.title
