def test_enable_data_resource_formatter(self):
    formatters = self.display_formatter.formatters
    mimetype = 'application/vnd.dataresource+json'
    with pd.option_context('display.html.table_schema', True):
        assert 'application/vnd.dataresource+json' in formatters
        assert formatters[mimetype].enabled
    assert 'application/vnd.dataresource+json' in formatters
    assert not formatters[mimetype].enabled
    with pd.option_context('display.html.table_schema', True):
        assert 'application/vnd.dataresource+json' in formatters
        assert formatters[mimetype].enabled
        self.display_formatter.format(cf)