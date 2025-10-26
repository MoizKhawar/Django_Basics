# Continue Developing Using Django

## 1.Step

- Move previously made static folder into your Django project folder (the same level as manage.py).
- inside static folder create two folders: images and CSS
- And Now inside CSS folder create a new file styles.css



## 2. Link bootstrap using CDN for responsive design
- CDN helps to load the bootstrap files from external server instead of hosting them locally.
- To connect by CDN Add the following lines to the head section of your index/home.html file:

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
``` 


## 3. Link your CSS file to your HTML file
#### First of all add `{% load static %}` at the top of your HTML file to enable the use of static files in Django templates.
- To link your CSS file to your HTML file, add the following line inside the head section of your index/home.html file:

```html
 <link rel="stylesheet" href="{% static 'CSS/styles.css' %}">  <!--{% static %} is a Django template tag used to generate the correct URL for static files. -->
```

## 4. Now you can add your custom styles in styles.css file
```css
body {
    background-color: #f0f8ff; /* Light blue background */
    font-family: Arial, sans-serif; /* Change font */
    color: #333; /* Dark text color */
    margin: 20px; /* Add some margin */
}
```

## 5. use div inside body section with class container to wrap your content for better styling and responsiveness
```html
<div class="container">
    <h1>Welcome to the Klazoo Home Page!</h1>
    <p>This is the main landing page of the Klazoo Website.</p>
</div>
```

## 6. CSS Not Applying to HTML Page

- After adding you notice that style not take effect on your html page
- To fix this you need to make some changes in settings.py file
    1. Open settings.py file
    2. Scroll down to find `STATIC_URL = 'static/'`
    3. Below this add the following
    ```python
    STATIC_ROOT = BASE_DIR / 'static'
    STATICFILES_DIRS = [
        "klazoo/static"
        ]
    ```
    4. Save the settings.py file

## 7. Add Image to your HTML Page
- First place image inside static/images folder
- Add image inside the div container in your HTML file using the following code:
```html
<img src="{% static 'images/klazoo.JPG' %}" alt="Klazoo Logo" class="img-fluid">
<!-- class="img-fluid" is a Bootstrap class that makes the image responsive -->
```

## NOW CHECK EVERYTHING IS WORKING FINE BY RUNNING THE SERVER