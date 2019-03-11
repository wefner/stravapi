============
Installation
============

Make sure you have xcode installed (MacOS only)

First off, it's recommended to create a virtualenv. If you don't know how, you,
can follow these instructions_:

Once your virtualenv is activated, install the required packages::

    $ pip install stravapi
    $ pip install uwsgi

If you run into ``openssl`` problems on MacOS, you may need to run the following::

    $ brew install openssl

Now you are going to need to configure ``pystrava`` which it will handle the
authentication to Strava API. You can configure it by following this link_.

Basically you will need to export the following environment variables as this
API does not support other methods at the moment::

    $ export CLIENT_ID=
    $ export SECRET=
    $ export CALLBACK_URL=
    $ export SCOPE=
    $ export EMAIL=
    $ export PASSWORD=

Clone this repository as follows::

    $ git clone https://github.com/wefner/stravapi.git

and then you should be able to run::

    $ cd stravapi/
    $ hug -f stravapi/stravapi.py


Or if you prefer to run it with ``uwsgi``::

    $ uwsgi --http 0.0.0.0:8000 \
        --wsgi-file $HOME/.pyenv/versions/<your_version>/envs/uwsgi/lib/python<your_version>/site-packages/stravapi/stravapi.py \
        --callable \
        __hug_wsgi__

Both commands will expose a RestAPI on port ``8000``. You can open a browser
and try different activities with the given URLs::

- http://localhost:8000/activities?activity_type=swim&number=4
- http://localhost:8000/activities?activity_type=ride&number=1
- http://localhost:8000/activities?activity_type=run&number=10

.. _instructions: https://github.com/pyenv/pyenv-virtualenv
.. _link: https://pystrava.readthedocs.io/en/latest/usage.html
