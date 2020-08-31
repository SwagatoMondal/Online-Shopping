# Online-Shopping
This is a very basic demo for a Django based application

## Tutorials

### Creating DB models
Create all models under `<app-name>/models.py` file. After creating run the commands
mentioned under this [section](https://github.com/SwagatoMondal/Online-Shopping#making-changes-to-db) for DB changes.

For example, refer to [products/models.py](https://github.com/SwagatoMondal/Online-Shopping/blob/master/online_shop/products/models.py) file.

### Creating HTML Pages

#### Create & Place your HTML files
To create your website pages, create a directory (like [templates](https://github.com/SwagatoMondal/Online-Shopping/tree/master/online_shop/templates))
under root directory and place your HTML files there.

#### Register directory under templates
Next step is to register this directory under `TEMPLATES` object in `settings.py` file. The change would look like
as mentioned below -
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
    ...
```
For example, refer to [settings.py](https://github.com/SwagatoMondal/Online-Shopping/blob/master/online_shop/online_shop/settings.py) file of this project.

#### Update Views
Next step is to define your page(s) under `views.py` by declaring a method to return the page. Your code should look like this-
```
def first(request):
    return render(request, 'page1.html')
```
For example, refer to [views.py](https://github.com/SwagatoMondal/Online-Shopping/blob/master/online_shop/online_shop/settings.py) file.

#### Register this view in URL(s)
Add the path of the newly created view under `urlpatterns` in `urls.py` file. You need to add the following line-

`path('<page-name>/', views.<method-name>)`

For example, refer to [urls.py](https://github.com/SwagatoMondal/Online-Shopping/blob/master/online_shop/online_shop/urls.py) file.

#### Re-start server & Check Browser
Now you're all setup to test your page, so run the command as mentioned in this [section](https://github.com/SwagatoMondal/Online-Shopping#start-server) and open the `<IP-address>:<Port-number>/<page-name>` in your browser to test.

## Important commands

### Creating new Apps
```
python manage.py startapp <app-name>
```

### Start server
```
python manage.py runserver
```

### Making changes to DB
```
python manage.py makemigrations <app-name>
python manage.py migrate <app-name>
```

### Running Virtual Environment
```
 source /tutorial-env/bin/activate
```

### Exiting Virtual Environment
```
deactivate
```
