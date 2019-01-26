import os
import re

import setuptools


def get_version(package):
    with open(os.path.join(package, "__version__.py")) as f:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", f.read()).group(1)


def get_readme():
    with open("README.md", encoding="utf8") as f:
        return f.read()


setuptools.setup(
    name="graphene-prisma",
    version=get_version("graphene_prisma"),
    url="https://github.com/taoufik07/graphene-prisma",
    license="BSD",
    description="Brings prisma playground to Graphene and more",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    author="Taoufik Abbassid",
    author_email="abacidtaoufik@gmail.com",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    extras_require={"responder": ["responder"], "starlette": ["starlette"]},
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
