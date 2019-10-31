from setuptools import setup, find_packages
from spacedoc import __version__

setup(
    name='spacedoc',
    version=__version__,

    url='http://host/',
    author='dk766',
    author_email='vchifu@gmail.com',

    packages=find_packages(),
    include_package_data=True,
    scripts=['scripts/manage.py'],

    install_requires=(
        'django<2.1',
    )
)
