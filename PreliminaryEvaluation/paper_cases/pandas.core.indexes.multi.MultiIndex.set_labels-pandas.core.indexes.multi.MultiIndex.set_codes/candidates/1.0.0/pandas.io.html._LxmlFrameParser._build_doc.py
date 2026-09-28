def _build_doc(self):
    """
        Raises
        ------
        ValueError
            * If a URL that lxml cannot parse is passed.

        Exception
            * Any other ``Exception`` thrown. For example, trying to parse a
              URL that is syntactically correct on a machine with no internet
              connection will fail.

        See Also
        --------
        pandas.io.html._HtmlFrameParser._build_doc
        """
    from lxml.html import parse, fromstring, HTMLParser
    from lxml.etree import XMLSyntaxError
    parser = HTMLParser(recover=True, encoding=self.encoding)
    try:
        if is_url(self.io):
            with urlopen(self.io) as f:
                r = parse(f, parser=parser)
        else:
            r = parse(self.io, parser=parser)
        try:
            r = r.getroot()
        except AttributeError:
            pass
    except (UnicodeDecodeError, IOError) as e:
        if not is_url(self.io):
            r = fromstring(self.io, parser=parser)
            try:
                r = r.getroot()
            except AttributeError:
                pass
        else:
            raise e
    else:
        if not hasattr(r, 'text_content'):
            raise XMLSyntaxError('no text parsed from document', 0, 0, 0)
    return r