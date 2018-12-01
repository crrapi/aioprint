# aioprint
An inherently useless Python library so you can log things without blocking your async program at all.
# Installation
`pip3 install -U git+https://github.com/crrapi/aioprint`
# Disclaimer
#### The practical use of this is trivial. You're better off using print, this is for the memes :^)
# Usage
```python
from aioprint import print

# in a coroutine function
await print("Non-blocking! Wew!")
```