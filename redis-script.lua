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
if separator == nil then
    separator = '';
end

local snKey = prefix .. tag .. ':' .. ymd;

local seq = tonumber(redis.call('INCRBY', snKey, step));
redis.call('EXPIRE', snKey, 86400);


-- second, microSecond,  seq
return  tag .. separator .. ymd .. separator .. string.format("%04d", seq)
