import builtins

from .print import print as new_print

# Keep a backup of the original function
# and overwrite the default print
builtins.old_print = print
builtins.print = new_print
