from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in honda_api/__init__.py
from honda_api import __version__ as version

setup(
	name="honda_api",
	version=version,
	description="Honda API",
	author="daviljutt",
	author_email="itsgoraya@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
