def test_parse_failure_rewinds(self):

    class MockFile:

        def __init__(self, data):
            self.data = data
            self.at_end = False

        def read(self, size=None):
            data = '' if self.at_end else self.data
            self.at_end = True
            return data

        def seek(self, offset):
            self.at_end = False

        def seekable(self):
            return True
    good = MockFile('<table><tr><td>spam<br />eggs</td></tr></table>')
    bad = MockFile('<table><tr><td>spam<foobr />eggs</td></tr></table>')
    assert self.read_html(good)
    assert self.read_html(bad)