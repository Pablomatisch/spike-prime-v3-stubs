"""The ``port`` module contains constants that enable easy addressing of the
lettered ports on the SPIKE Prime hub. Use the constants in all functions that
take a ``port`` parameter.

To use the ``port`` module add the following import statement to your
project:

::

    from hub import port

All constants in the module should be called inside the ``port`` module
as a prefix like so:

::

    port.A

The following constants are defined:

* ``A`` = 0
* ``B`` = 1
* ``C`` = 2
* ``D`` = 3
* ``E`` = 4
* ``F`` = 5
"""
from typing import Final
import sys

#message when run on pc

sys.stderr.write(
    "❌ LEGO SPIKE runtime not detected.\n"
    "This code only works on the SPIKE hardware.\n"
)

sys.exit(1)

A: Final[int] = 0
"""Port A"""
B: Final[int] = 1
"""Port B"""
C: Final[int] = 2
"""Port C"""
D: Final[int] = 3
"""Port D"""
E: Final[int] = 4
"""Port E"""
F: Final[int] = 5
"""Port F"""