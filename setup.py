from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in school_info/__init__.py
from school_info import __version__ as version

setup(
	name="school_info",
	version=version,
	description="it describes all the process takes place in a school",
	author="demo",
	author_email="123@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
