"""The ``device`` module contains functions to get general information about
any devices plugged into the hub (motors, sensors, displays, etc). 

To use the ``device`` module, add the following import statement to your
project:

::

    import device

All functions in the module should be called inside the ``device``
module as a prefix like so:

::

    device.id(port.A)
"""

from hub.port import Port
import sys

#message when run on pc

sys.stderr.write(
    "❌ LEGO SPIKE runtime not detected.\n"
    "This code only works on the SPIKE hardware.\n"
)

sys.exit(1)


def data(port: Port) -> tuple[int]:
    """Get the raw LPF-2 data from a device.

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :rtype: tuple
    """


def id(port: Port) -> int:
    """Get the device type ID of a device. Each device has an ID based on its
    type. IDs for commonly used Spike Prime inputs/outputs (from
    `<https://github.com/pybricks/technical-info/blob/master/assigned-numbers.md>`_
    include:

    * *48*: Spike Prime Medium Motor (45603)
    * *49*: Spike Prime Large Motor (45602)
    * *61*: Color Sensor (45605)
    * *62*: Distance Sensor (45604)
    * *63*: Force Sensor (45606)
    * *64*: Color Light Matrix (45608)
    * *65*: Small Motor (45607)

    See the link above for a more extensive list.

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :rtype: int
    """


def get_duty_cycle(port: Port) -> int:
    """Get the duty cycle for a device. Returned value is in range 0 to
    10000.

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :rtype: int
    """


def ready(port: Port) -> bool:
    """When a device is attached to the hub, it might take a short amount of
    time before it is ready to accept requests. Use ``ready`` to test for the
    readiness of the attached devices.

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :rtype: bool
    """


def set_duty_cycle(port: Port, duty_cycle: int) -> None:
    """Set the duty cycle on a device. Range 0 to 10000.

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :param duty_cycle: The PWM value (0–10000)
    :rtype: None
    """
