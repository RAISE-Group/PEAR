def _build_doc(self):
    from bs4 import BeautifulSoup
    bdoc = self._setup_build_doc()
    if isinstance(bdoc, bytes) and self.encoding is not None:
        udoc = bdoc.decode(self.encoding)
        from_encoding = None
    else:
        udoc = bdoc
        from_encoding = self.encoding
    return BeautifulSoup(udoc, features='html5lib', from_encoding=from_encoding)