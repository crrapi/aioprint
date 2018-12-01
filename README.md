# aioprint
An inherently useless Python library so you can log things without blocking your async program at all.
# Installation
`pip3 install -U aioprint`
# Usage
```python
from aioprint import print

# in a coroutine function
await print("Non-blocking! Wew!")
```