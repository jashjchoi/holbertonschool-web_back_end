#!/usr/bin/env python3
"""Redis main file
"""
import uuid
import redis
from typing import Union, Callable, Any, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count number of calls to method
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, args):
        """Wrapper function"""
        res = method(self, args)
        self._redis.incr(key)
        return res
    return wrapper


def call_history(method: Callable) -> Callable:
    """store Call History of inputs and outputs
    """
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        """list keys of Wrapper function
        """
        self._redis.rpush(input_key, str(args))
        res = method(self, *args)
        self._redis.rpush(output_key, str(res))
        return res
    return wrapper


def replay(method: Callable):
    """Replay log of functions
    """
    c = redis.Redis()
    storage = method.__qualname__
    aux = c.get(storage).decode('utf-8')
    inputs = c.lrange(storage + ':inputs', 0, -1)
    outputs = c.lrange(storage + ':outputs', 0, -1)
    print("{} was called {} times:".format(storage, aux))
    for i, o in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(storage, i.decode("utf-8"),
                                     o.decode("utf-8")))


class Cache:
    """Redis cache class
    """
    def __init__(self):
        """initiate Redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes argument and store in Redis
        and returns a string
        """
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """take a key in db and convert string argument
        """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, data: str) -> str:
        """Converts bytes to str value
        """
        return self._redis.get(data).decode('utf-8')

    def get_int(self, data: str) -> int:
        """Converts bytes to int value
        """
        return int(self._redis.get(data))
