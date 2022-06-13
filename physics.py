import numpy as np

G = 6.67E-11  # G in SI units


def freefall_time(h, r, m):
    """
    Formula for time taken to hit the surface of a planet/moon from a certain height
    Retrieved from http://cosinekitty.com/pebble/
    :param float h:  Distance (metres) from the centre of planet/moon object is dropped
    :param float r:  Radius (metres) of the planet/moon
    :param float m:  Mass (kg) of planet/moon
    :return: (float) Time taken, in seconds, to fall
    """
    t = np.sqrt(h/(2*m*G))*(0.5*h*np.arccos((2*r-h)/h) + np.sqrt(r*(h-r)))
    return t


def speed(h, x, m):
    """
    Calculate the instantaneous speed of a particle that starts falling
    from distance H at the moment it passes through distance x.
    This formula derives directly from conserving kinetic energy + potential energy,
    with v=0 when x=H.
    :param float h: Distance (metres) from the centre of planet/moon object is dropped
    :param float x: Distance (metres) from the centre of planet/moon object is dropped
    :param float m: Mass (kg) of planet/moon
    :return: (float) Final speed in m/s
    """
    return np.sqrt(2*m*G * (1/x - 1/h))
