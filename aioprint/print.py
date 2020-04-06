import sys
from asyncio import get_event_loop

from aiofiles.threadpool.binary import AsyncBufferedIOBase

async_stdout_buffer = AsyncBufferedIOBase(
    sys.stdout, loop=get_event_loop(), executor=None
)

# Exact signature like the actual print() function
async def print(*objects, sep=" ", end="\n", flush=False):
    """Asynchronously prints things!"""
    objects = [str(i) for i in objects]
    printable_string = f"{sep.join(objects)}{end}"
    await async_stdout_buffer.write(printable_string)
    if flush:
        await async_stdout_buffer.flush()
