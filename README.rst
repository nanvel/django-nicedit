Nicedit widget for Django
============

Nicedit widget for django with image upload feature.

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
        ...,
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

    ./manage.py migrate nicedit

Usage
-----

from nicedit.widgets import NicEditWidget


class MyForm(forms.Form):
    content = forms.TextField(widget=NicEditWidget())


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-nicedit
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
