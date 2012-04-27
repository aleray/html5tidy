#! /usr/bin/env python


from setuptools import setup


setup(
    name='html5tidy',
    version='1.0',
    author='Michael Murtaugh',
    author_email='mm@automatist.org',
    description='Simple wrapper around html5lib & lxml.etree to "tidy" html in the wild to well-formed xml/html',
    url='http://automatist.org/',
    py_modules=['html5tidy'],
    scripts=['html5tidy'],
    install_requires=['html5lib', 'lxml'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Environment :: Other Environment',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
    ],
)
