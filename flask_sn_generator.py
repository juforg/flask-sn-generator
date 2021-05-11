# -*- coding: utf-8 -*-
"""
    Flask Serial Number Generator
    ~~~~~~~~~~~~~
    Flask extension for generating serial number.
    :copyright: (c) 2021 by juforg.
    :license: MIT, see LICENSE for more details.
"""

__version__ = '0.1.1'

__all__ = []
lua_script_content = """
-- need redis 3.2+
redis.replicate_commands();

local prefix = '_sn:';
local step = 1;
local startStep = 0;
local tag = KEYS[1];
--local formatStr = "%Y%m%d"
--local now = redis.call('TIME');
local ymd = KEYS[2];
local separator = KEYS[3];
local seqLength = KEYS[4];

local snKey = prefix .. tag .. ':' .. ymd;

local seq = tonumber(redis.call('INCRBY', snKey, step));
redis.call('EXPIRE', snKey, 86400);


-- second, microSecond,  seq
return  tag .. separator .. ymd .. separator .. string.format("%0"..seqLength.."d", seq)

"""


class SnGenerator(object):
    """
    Doc string.
    Explain your extension in detail here.
    """

    def __init__(self, app=None, config_prefix="SN", redis_config_prefix="REDIS"):
        self.sn_seq_length = None
        self.separator = ''
        self.config_prefix = config_prefix
        self.redis_config_prefix = redis_config_prefix
        self._sn_lua_script = None
        self._redis_client = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initalizes the application with the extension.
        :param app: The Flask application object.
        """

        if app is not None and hasattr(app, "extensions") and not app.extensions[self.redis_config_prefix.lower()]:
            raise Exception('FlaskRedis not inited, Please init FlaskRedis first!')
        else:
            self._redis_client = app.extensions[self.redis_config_prefix.lower()]
        self._sn_lua_script = self._redis_client.register_script(lua_script_content)
        app.config.setdefault(f'{self.config_prefix}_SEQ_LENGTH', 4)
        app.config.setdefault(f'{self.config_prefix}_SEPARATOR', '')
        self.separator = app.config.get(f'{self.config_prefix}_SEPARATOR')
        self.sn_seq_length = int(app.config.get(f'{self.config_prefix}_SEQ_LENGTH')) % 10 or 4
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions[self.config_prefix.lower()] = self

    def next_sn(self, tag, ymd):
        return self._sn_lua_script(keys=[tag, ymd, self.separator, self.sn_seq_length]).decode('UTF-8')
