
r"""

OSNAP: Open-Source Neighborhood Analysis Package.
================================================

Documentation
-------------
OSNAP documentation is available in two forms: python docstrings and an html\
        webpage at http://osnap.org/

Available sub-packages
----------------------

analyze
    analyze neighborhood dynamics
harmonize
    harmonize neighborhood boundaries into consistent demarcators
visualize
    plot and animate neighborhoods and their change
data
    ingest, store, and manipulate spatiotemporal neighborhood data

"""

__version__ = "0.0.0"

# __version__ has to be define in the first line



from . import analyze
from . import data
from . import util
from .data import metros
