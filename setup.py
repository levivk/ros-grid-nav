from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
print("In setup.py")
d = generate_distutils_setup(
    packages=['grid_nav'],
    package_dir={'': 'src'}
)
setup(**d)