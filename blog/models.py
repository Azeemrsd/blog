from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.EmailField()
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.firstName + " " + self.lastName

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})
    
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})
    
class Post(models.Model):
    title = models.CharField(max_length=150,null=False)
    excerpt = models.CharField(max_length=200,null=False)
    imageName = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True,related_name="posts")
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})


