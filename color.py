"""The ``color`` module contains the color constants to use with the
``color_matrix``, ``color_sensor`` and ``light`` modules.

To use the ``color`` module, add the following import statement to your
project:

::

    import color

The following constants are defined:

* ``BLACK`` = 0
* ``MAGENTA`` = 1
* ``PURPLE`` = 2
* ``BLUE`` = 3
* ``AZURE`` = 4
* ``TURQUOISE`` = 5
* ``GREEN`` = 6
* ``YELLOW`` = 7
* ``ORANGE`` = 8
* ``RED`` = 9
* ``WHITE`` = 10
* ``UNKNOWN`` = -1
"""

from typing import Final
import sys

#message when run on pc

sys.stderr.write(
    "❌ LEGO SPIKE runtime not detected.\n"
    "This code only works on the SPIKE hardware.\n"
)

sys.exit(1)

BLACK: Final[int] = 0
MAGENTA: Final[int] = 1
PURPLE: Final[int] = 2
BLUE: Final[int] = 3
AZURE: Final[int] = 4
TURQUOISE: Final[int] = 5
GREEN: Final[int] = 6
YELLOW: Final[int] = 7
ORANGE: Final[int] = 8
RED: Final[int] = 9
WHITE: Final[int] = 10
UNKNOWN: Final[int] = -1
