# Import version information
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('python_metrics').version
except DistributionNotFound:
    __version__ = 'unknown'

# Import submodules for the package
