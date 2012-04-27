# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
HTML5Tidy
=========

Simple wrapper around html5lib & lxml.etree to "tidy" html in the wild to
well-formed xml/html


Usage
-----

    >>> from html5tidy import tidy
    >>> tidy('some text')
    '<html><head/><body>some text</body></html>'


Dependencies
------------

* [html5lib](http://code.google.com/p/html5lib/)
* [lxml](http://lxml.de/)


Copyright
---------

- 2011, 2012 [The active archives contributors](http://activearchives.org/)
- 2011, 2012 Michael Murtaugh

All rights reserved.

This software is released under the GPL3 license. See gpl-3.0.txt for details.
"""


import html5lib
import lxml.etree


parser = html5lib.HTMLParser(tree=html5lib.treebuilders.getTreeBuilder("lxml"), namespaceHTMLElements=False)


def tidy(src, fragment=False, container="div", encoding=None, parseMeta=True, useChardet=True, method="xml", pretty_print=False, xml_declaration=None, output_encoding="utf-8"):
    if fragment:
        parts = parser.parseFragment(src, container=container, encoding=encoding, parseMeta=parseMeta, useChardet=useChardet)
    else:
        parts = [parser.parse(src, encoding=encoding, parseMeta=parseMeta, useChardet=useChardet)]

    ret = ""
    for p in parts:
        t = type(p)
        if (t == str or t == unicode):
            ret += p
        else:
            ret += lxml.etree.tostring(p, method=method, pretty_print=pretty_print, xml_declaration=xml_declaration, encoding=output_encoding)

    return ret


if __name__ == "__main__":
    import doctest
    doctest.testmod()
