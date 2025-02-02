# -*- coding: utf-8 -*-

from setuptools import setup

# Six 1.10 is vendored in with Django 1.11 so we require at least that version
requires = ['Django >= 1.11', 'six>=1.10']
tests_require = requires

setup(
    name="dj-inmemorystorage",
    description="A non-persistent in-memory data storage backend for Django.",
    version="2.0.0",
    url="https://github.com/waveaccounting/dj-inmemorystorage",
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    author='Cody Soyland, Seán Hayes, Tore Birkeland, Nick Presta',
    author_email='opensource@waveapps.com',
    packages=[
        'inmemorystorage',
    ],
    zip_safe=True,
    install_requires=requires,
    tests_require=tests_require,
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
