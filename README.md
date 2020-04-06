# aioprint
`aioprint` provides an asynchronous interface for `print` by using `aiofiles` as a backend.

# Installation
### Using PyPI
`pip3 install -U aioprint`

### Using git with this GitHub repo
`pip3 install -U git+https://github.com/crrapi/aioprint`

# Usage
```python
import asyncio
import sys

import aioprint


class A:

    async def __aiostr__(self):
        # The __aiostr__ magic method is preferred
        # over the __str__ method to provide
        # a coroutine interface
        return "pony trick yasuo"

async def main():
    await print(["sub", 2, "pew"], "he is great", end="", sep="LOL")
    a = A()
    await print("error", file=sys.stderr)
    await print(a, file="out.txt")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

# Acknowledgements
Special thanks to [Gelbpunkt aka Adrian](https://github.com/Gelbpunkt) for reviving this and making it useful
