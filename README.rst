NicEdit widget for Django
=========================

NicEdit widget for django with image upload feature.

NicEdit home: `http://nicedit.com/ <http://nicedit.com/>`__

Blog post: `NicEdit widget for Django <http://nanvel.name/2013/08/django-nicedit>`__

Versions
--------

0.23 - use with Django<1.6

0.24 - use with Django==1.6

1.1 - use with Django==1.7

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install django-nicedit

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://github.com/nanvel/django-nicedit.git#egg=nicedit

Add ``nicedit`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'nicedit',
    )

Add the ``nicedit`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^nicedit/', include('nicedit.urls')),
    )

Don't forget to migrate your database

.. code-block:: bash

    python manage.py migrate nicedit

MEDIA_ROOT should be specified, example:

.. code-block:: python

    MEDIA_ROOT = os.path.join(os.path.dirname('__file__'), '../media')
    MEDIA_URL = '/media/'

Add to urls configuration:

.. code-block:: python

    from django.conf.urls.static import static
    from django.conf import settings

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Usage
-----

forms.py:

.. code-block:: python

    from django import forms

    from nicedit.widgets import NicEditWidget


    class MessageForm(forms.Form):
        message = forms.CharField(
            widget=NicEditWidget(attrs={'style': 'width: 800px;'})
        )

views.py:

.. code-block:: python

    from django.shortcuts import render

    from .forms import MessageForm


    def home(request):
        form = MessageForm()
        return render(request, 'home.html', {'form': form})

template:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>NicEdit widget</title>
        {{ form.media }}
      </head>
      <body>
        <form action='.' method='post'>
          {% csrf_token %}
          {{ form.message }}
          <button type="submit">Submit</button>
        </form>
      </body>
    </html>


See `testproject <https://github.com/nanvel/django-nicedit/tree/master/testproject>`__ for example.

Usage in admin:

.. code-block:: python

    # -*- coding: utf-8 -*-
    from django import forms
    from django.contrib import admin

    from nicedit.widgets import NicEditAdminWidget

    from .models import Item


    class ItemAdminForm(forms.ModelForm):

        class Meta:
            model = Item
            widgets = {
                'text': NicEditAdminWidget(
                    attrs={'style': 'width: 610px;'},
                    js_options={"buttonList": [
                        'save', 'bold', 'italic', 'underline', 'left', 'center',
                        'right', 'justify', 'ol', 'ul', 'fontSize',  # 'fontFamily',
                        'fontFormat', 'indent', 'outdent', 'image', 'upload', 'link',
                        'unlink', 'forecolor', 'bgcolor', 'xhtml']
                    }
                )
            }


    class ItemAdmin(admin.ModelAdmin):

        form = ItemAdminForm


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ virtualenv .env --no-site-packages
    $ source .env/bin/activate
    $ python setup.py install
    $ pip install -r test_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
