# aioprint
`aioprint` provides an asynchronous interface for `print` by using `aiofiles` as a backend.

# Installation
### Using PyPI
`pip3 install -U aioprint`

### Using git with this GitHub repo
`pip3 install -U git+https://github.com/crrapi/aioprint`

# Usage
```python
import aioprint
import asyncio

async def main():
    await print("yes")
    await print(["sub", 2, "pew"], flush=True, end="")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

# Acknowledgements
Special thanks to [Gelbpunkt aka Adrian](https://github.com/Gelbpunkt) for reviving this and making it useful
