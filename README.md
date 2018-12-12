randnumgen
====

This is a djangae project for randnumgen.

Running local development server
----

>  ./manage.py collectstatic  
>  ./manage.py migrate  
>  ./manage.py runserver


Deployment
----

>  ./manage.py collectstatic  
>  gcloud app deploy app.yaml


Setting up djangae
----

Use of virtualenvwrapper is recommended.

* Install the Google Cloud SDK and install the app-engine-python-extras component
  * `gcloud component install app-engine-python-extras`
* Downgrade the SDK to the latest version supported by djangae (currently 170.0.0)
  * `gcloud components update --version 170.0.0`
* Use `mkvirtualenv -p$(which python2) ...` to set up a virtualenv
* Install `requirements/base.txt` into your virtualenv
  * `pip install -r requirements/base.txt`
* Install `requirements/vendor.txt` into a 'lib' folder in the project
  * `pip install -t lib -r requirements/vendor.txt`
* Add the SDK's `platform/google_appengine` dir to your virtualenv
  * `add2virtualenv /path/to/google-cloud-sdk/platform/google_appengine`
* Add the 'lib' dir to your virtualenv
  * `add2virtualenv lib`
