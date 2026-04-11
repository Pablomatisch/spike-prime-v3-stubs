"""The ``force_sensor`` module contains functions to interact with an attached
Force Sensor (e.g. LEGO part 45606) and enables you to write code that reacts
to touch events or force magnitude.

To use the ``force_sensor`` module, add the following import statement to
your project:

::

    import force_sensor

All functions in the module should be called inside the ``force_sensor``
module as a prefix like so:

::

    force_sensor.force(port.A)
"""

from hub.port import Port
import sys

#message when run on pc

sys.stderr.write(
    "❌ LEGO SPIKE runtime not detected.\n"
    "This code only works on the SPIKE hardware.\n"
)

sys.exit(1)

def force(port: Port) -> int:
    """Get the measured force in decinewtons. Values range from 0 to 100.

    ::

        from hub import port
        import force_sensor

        print(force_sensor.force(port.A))

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :rtype: int
    """


def pressed(port: Port) -> bool:
    """Test whether the button on the sensor is pressed. Returns true if the
    force sensor connected to port ``port`` is pressed.

    ::

        from hub import port
        import force_sensor

        print(force_sensor.pressed(port.A))

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :rtype: bool
    """


def raw(port: Port) -> int:
    """Get the raw, uncalibrated force value of the force sensor connected
    on port ``port``.

    ::

        from hub import port
        import force_sensor

        print(force_sensor.raw(port.A))

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :rtype: int
    """
