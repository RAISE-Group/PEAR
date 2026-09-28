def test_dictwrapper_getattr(self):
    options = self.cf.options
    with pytest.raises(OptionError, match='No such option'):
        options.bananas
    assert not hasattr(options, 'bananas')