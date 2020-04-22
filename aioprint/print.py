import sys
from asyncio import get_event_loop
from io import StringIO, TextIOWrapper

import aiofiles
from aiofiles.threadpool.binary import AsyncBufferedIOBase

_loop = get_event_loop()

async_stdout_buffer = AsyncBufferedIOBase(sys.stdout, loop=_loop, executor=None)
async_stderr_buffer = AsyncBufferedIOBase(sys.stderr, loop=_loop, executor=None)

# Exact signature like the actual print() function
async def print(*objects, sep=" ", end="\n", flush=False, file=sys.stdout):
    """
    Asynchronously prints things!
    Parameters to be printed will be converted to strings in the following order:
        - If it has a coroutine function called "__aiostr__", that will be used. It should return a string
        - Else, it will use the builtin str() (and therefore "__str__" or "__repr__")
    """
    # check if it's a buffer we know
    if file == sys.stdout:
        buffer = async_stdout_buffer
        close = False
    elif file == sys.stderr:
        buffer = async_stderr_buffer
        close = False
    elif isinstance(file, StringIO):
        # it is a buffer, convert it
        buffer = AsyncBufferedIOBase(file, loop=_loop, executor=None)
        close = True
    elif isinstance(file, TextIOWrapper):
        # it is an open file, BAD! open async again
        name = file.name
        buffer = await aiofiles.open(name, "w")
        close = True
    else:
        # we assume a filename
        buffer = await aiofiles.open(file, "w")
        close = True
    objects = [
        str(i) if not hasattr(i, "__aiostr__") else await i.__aiostr__()
        for i in objects
    ]
    printable_string = f"{sep.join(objects)}{end}"
    await buffer.write(printable_string)
    if flush:
        await buffer.flush()
    if close:
        await buffer.close()
