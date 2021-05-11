=====
Usage
=====

To use Flask SN Generator in a project::

    import flask_sn_generator

------------------------------
Configuring flask-sn-generator
------------------------------
**flask-sn-generator** is configured through the standard Flask config API. These are the available
options (each is explained later in the documentation):

* **SN_SEQ_LENGTH** : default **4**

* **SN_SEPARATOR** : default **''**


In addition the standard Flask ``TESTING`` configuration option is used by **flask-sn-generator**
in unit tests (see below).

sn generator is managed through a ``SnGenerator`` instance::

    from flask import Flask
    from flask_sn_generator import SnGenerator

    app = Flask(__name__)
    sn_generator = SnGenerator(app)

In this case all sn generator using the configuration values of the application that
was passed to the ``SnGenerator`` class constructor.

Alternatively you can set up your ``SnGenerator`` instance later at configuration time, using the
**init_app** method::

    sn_generator = SnGenerator()

    app = Flask(__name__)
    sn_generator.init_app(app)

In this case sn_generator will use the configuration values from Flask's ``current_app``
context global. This is useful if you have multiple applications running in the same
process but with different configuration options.


::::::::::::::::::::::
Generate Serial Number
::::::::::::::::::::::

To generate a serial number first create a ``SnGenerator`` instance::

    from flask_redis import FlaskRedis
    from flask_sn_generator import SnGenerator
    redis_client = FlaskRedis()
    sn_generator = SnGenerator()
    @app.route("/")
    def index():

        sn = sn_generator.next_sn('SN', '20210511')
