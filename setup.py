from marx import __appname__, __version__
from setuptools import setup


long_description = ""

setup(
    name=__appname__,
    version=__version__,
    scripts=[],
    packages=[
        'marx',
        'marx.docker',
    ],
    author="Paul Tagliamonte",
    author_email="tag@pault.ag",
    long_description=long_description,
    description='Control the means of production',
    license="Expat",
    url="http://deb.io/",
    platforms=['any'],
    entry_points={
        'console_scripts': [
        ],
    }
)
