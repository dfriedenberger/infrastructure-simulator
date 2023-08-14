from setuptools import setup
from infrastructure_simulator import __version__

setup(name='infrastructure_simulator',
      version=__version__,
      description='Simulator for (e.g. railway) infrastructure.',
      url='https://github.com/dfriedenberger/infrastructure-simulator.git',
      author='Dirk Friedenberger',
      author_email='projekte@frittenburger.de',
      license='GPLv3',
      packages=['infrastructure_simulator'],
      install_requires=["svgwrite"],
      zip_safe=False)
