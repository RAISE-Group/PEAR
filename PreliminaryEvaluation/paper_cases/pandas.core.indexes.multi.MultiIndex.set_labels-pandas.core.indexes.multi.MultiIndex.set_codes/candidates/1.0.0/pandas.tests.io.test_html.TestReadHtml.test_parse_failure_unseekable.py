def test_parse_failure_unseekable(self):
    if self.read_html.keywords.get('flavor') == 'lxml':
        pytest.skip('Not applicable for lxml')

    class UnseekableStringIO(StringIO):

        def seekable(self):
            return False
    bad = UnseekableStringIO('\n            <table><tr><td>spam<foobr />eggs</td></tr></table>')
    assert self.read_html(bad)
    with pytest.raises(ValueError, match='passed a non-rewindable file object'):
        self.read_html(bad)