from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About pages"

    def __str__(self):
        return self.title
