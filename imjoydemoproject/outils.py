# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import numpy as np

# ---------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------

__version__ = '0.1.0'
__author__ = 'Florian MUELLER, Aubin SAMACOITS'
__email__ = 'muellerf.research@gmail.com'


# ---------------------------------------------------------------------------
# Modules
# ---------------------------------------------------------------------------

def calc_sine(n_points=10):
    """Calculates sine function for defined number of points.

    Extended description of function.

    Args:
        arn_points (int): Number of data points

    Returns:
        x (1D numpy arr): x coordinates
        y (1D numpy arr): y coordinates
    """
    x = np.around(np.arange(0.0, 5.0, 5.0/n_points),decimals=2)
    y = np.sin(2*np.pi*x)
    return x, y
