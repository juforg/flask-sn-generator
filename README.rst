=============================
Flask Serial Number Generator
=============================

.. image:: https://readthedocs.org/projects/flask-sn-generator/badge/?version=latest
   :target: https://flask-sn-generator.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://github.com/juforg/flask-sn-generator/actions/workflows/publish-to-test-pypi.yml/badge.svg
   :target: https://github.com/juforg/flask-sn-generator/actions/workflows/publish-to-test-pypi.yml
   :alt: Publish Python 🐍 distributions 📦 to PyPI and TestPyPI

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
flask-redis 0.4.0 or higher)::

    pip install flask-sn-generator



Then:
    from flask import Flask
    from flask_redis import FlaskRedis
    from flask_sn_generator import SnGenerator

    app = Flask(__name__)


    redis_client = FlaskRedis()
    redis_client.init_app(app=app)
    sn_generator = SnGenerator()
    sn_generator.init_app(app)
    @app.route("/")
    def index():
        sn = sn_generator.next_sn('SN', '20210511')

example result:
 SN202105110001

Links
-----

-   Documentation: https://flask-sn-generator.readthedocs.io/en/latest/index.html
-   Changes: https://flask-sn-generator.readthedocs.io/en/latest/history.html
-   PyPI Releases: https://pypi.org/project/flask-sn-generator/
-   Source Code: https://github.com/juforg/flask-sn-generator/
-   Issue Tracker: https://github.com/juforg/flask-sn-generator/issues/

