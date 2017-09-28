from setuptools import setup, find_packages

setup(
    name="xml-default-dict",
    version="0.1",
    license="BSD2CLAUSE",
    packages=find_packages(),
    data_files=[('', ['LICENSE'])],
    package_data={'': ['LICENSE']},
    keywords="wmi impacket",
    url="https://github.com/kanazux/xml-default-dict",
    author='Silvio AS a.k.a kanazuchi',
    author_email='contato@kanazuchi.com',
    scripts=['scripts/xml-default-parse],
    description="A simple way to convert xml elemnts into a default dict from lib collections.",
)
