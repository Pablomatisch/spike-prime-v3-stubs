"""The ``orientation`` module contains the orientation constants to use
with the ``light_matrix`` module.

To use the orientation module add the following import statement to your
project:

::

    import orientation

The following constants are defined:

* ``UP`` = 0
* ``RIGHT`` = 1
* ``DOWN`` = 2
* ``LEFT`` = 3
"""

from typing import Final
import sys

#message when run on pc

sys.stderr.write(
    "❌ LEGO SPIKE runtime not detected.\n"
    "This code only works on the SPIKE hardware.\n"
)

sys.exit(1)

UP: Final[int] = 0
RIGHT: Final[int] = 1
DOWN: Final[int] = 2
LEFT: Final[int] = 3