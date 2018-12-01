import copy
import functools
import asyncio

_print_copy = copy.copy(print)
_loop = asyncio.get_event_loop()

async def print(*args, **kwargs):
    """Asynchronously prints things!"""
    _partial_print = functools.partial(_print_copy, *args, **kwargs)
    await _loop.run_in_executor(None, _partial_print)
