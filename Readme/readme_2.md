# Continue with django....

## 1.Create app inside project

```bash
python manage.py startapp <app_name>
```

## 2. Migrate command after creating app
```bash
python manage.py migrate
```

## 3. Create superuser to access admin panel
```bash
python manage.py createsuperuser
```

## 4. Run server
```bash
python manage.py runserver
```

## 5. Access admin panel by visiting
```bash
http://127.0.0.1:8000/admin/
```


## 6. In admin panel you can create users and groups and assign permissions


## 7. Configure model.py to add models
```python
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
```

## 8. Register models in admin.py to manage them via admin panel
```python
from django.contrib import admin
from .models import AboutUs

admin.site.register(AboutUs)
```

## 9. Add app to settings.py
```python
INSTALLED_APPS = [
    ...
    'about',
]
```
## 10. install pillow for image field
```bash
python -m pip install Pillow
```

## 11. Make migrations and migrate to create database tables
```bash
python manage.py makemigrations
python manage.py migrate
```

## 12. Configure media settings in settings.py
- it is for handling media files like images
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
## 13. Configure urls.py to serve media files during development
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


