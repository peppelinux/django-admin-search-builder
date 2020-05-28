# django-admin-search-builder
Django app that makes you able to build advanced queries via admin filters UI

This Application aims to give you the faster and easier way to do advanced query via Django Admin ModelAdmin UI, using the Django's ORM.
See example projects and gallery.

### Setup

````
pip install django-admin-search-builder
````

in `settings.INSTALLED_APPS` add
````
    'admin_adv_search_builder',
````

in your ModelAdmin, use it following this example
````
from admin_adv_search_builder.filters import AdvancedSearchBuilder
from django.contrib import admin

from . models import Identity


@admin.register(Identity)
class IdentityAdmin(admin.ModelAdmin):
    list_filter   = (AdvancedSearchBuilder,)
````

#### Example

````
pip install -r requirements.xt

cd example
./manage.py migrate
./manage.py createsuperuser
./manage.py loaddata identity_dumps.json
./manage.py runserver
````

#### Gallery
![Alt text](images/1.png)


#### Authors

Giuseppe De Marco
