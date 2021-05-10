#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Integration tests for flask_sn_generator
----------------------------------

Tests for `flask_sn_generator` module.
"""
from flask import Flask
import pytest

from flask_sn_generator import SnGenerator


@pytest.fixture
def app():
    return Flask(__name__)


def test_constructor(app):
    """Test that a constructor with app instance will initialize the
    connection"""
    sn_generator = SnGenerator(app)
    assert sn_generator._sn_lua_script is not None
    assert hasattr(sn_generator._redis_client, "connection_pool")


def test_init_app(app):
    """Test that a constructor without app instance will not initialize the
    connection.
    After FlaskRedis.init_app(app) is called, the connection will be
    initialized."""
    sn_generator = SnGenerator()
    assert sn_generator._sn_lua_script is None
    sn_generator.init_app(app)
    assert sn_generator._sn_lua_script is not None
    assert hasattr(sn_generator._redis_client, "connection_pool")
    if hasattr(app, "extensions"):
        assert "redis" in app.extensions
        assert app.extensions["sn"] == sn_generator


# def test_custom_prefix(app):
#     """Test that config prefixes enable distinct connections"""
#     app.config["DBA_URL"] = "redis://localhost:6379/1"
#     app.config["DBB_URL"] = "redis://localhost:6379/2"
#     sn_generator = SnGenerator(app, config_prefix="DBA")
#     assert redis_a.connection_pool.connection_kwargs["db"] == 1

