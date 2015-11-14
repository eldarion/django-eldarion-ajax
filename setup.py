import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Patrick Altman",
    author_email="paltman@eldarion.com",
    description="a companion app to eldarion-ajax providing base views and mixins to make hooking up views in your project even easier",
    name="django-eldarion-ajax",
    long_description=read("README.rst"),
    version="0.1",
    url="http://github.com/eldarion/django-eldarion-ajax/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "eldarion.ajax": []
    },
    test_suite="runtests.runtests",
    tests_require=[
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
