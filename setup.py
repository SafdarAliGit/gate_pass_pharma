from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gate_pass_pharma/__init__.py
from gate_pass_pharma import __version__ as version

setup(
	name="gate_pass_pharma",
	version=version,
	description="this gate pass app for pharma",
	author="Safar Ali",
	author_email="safdar211@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
