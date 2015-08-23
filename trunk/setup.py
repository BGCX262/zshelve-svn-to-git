from setuptools import setup, find_packages

import zshelve

setup(
    name = "zshelve",
    version = zshelve.__version__,
    #version = "0.0.1",
    author = "Huang Jihua",
    author_email = "jhuangjiahua@gmail.com",
    description = "compression shelve database",
    license = "MIT",
    url="http://code.google.com/p/zshelve/",
    keywords = "database persistence pickle ipc shelve",
    long_description = """\
Manage shelves of compression pickled objects.

A "shelf" is a persistent, dictionary-like object. The difference with dbm databases is that the values (not the keys!) in a shelf can be essentially arbitrary Python objects -- anything that the "pickle" module can handle. This includes most class instances, recursive data types, and objects containing lots of shared sub-objects. The keys are ordinary strings.
""",
    py_modules = ['zshelve'],
    scripts=['zshelve'],
)
