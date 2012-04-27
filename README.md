HTML5Tidy
=========

Simple wrapper around html5lib & lxml.etree to "tidy" html in the wild to
well-formed xml/html


Usage
-----

With the command-line:

    html5tidy [-h] [-f] [--inputencoding INPUTENCODING] [--inputnometa]
              [--inputnochardet] [-m METHOD] [--prettyprint]
              [--outputencoding OUTPUTENCODING] [--xmldeclaration]
              [source]

With the python module

    >>> from html5tidy import tidy
    >>> tidy('some text')
    '<html><head/><body>some text</body></html>'


Copyright
---------

- 2011, 2012 [The active archives contributors](http://activearchives.org/)
- 2011, 2012 Michael Murtaugh

All rights reserved.

This software is released under the GPL3 license. See gpl-3.0.txt for details.
