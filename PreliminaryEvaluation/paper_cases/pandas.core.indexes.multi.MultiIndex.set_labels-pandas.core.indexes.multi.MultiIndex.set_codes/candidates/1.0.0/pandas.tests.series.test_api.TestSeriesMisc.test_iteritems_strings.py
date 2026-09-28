def test_iteritems_strings(self, string_series):
    for idx, val in string_series.iteritems():
        assert val == string_series[idx]
    assert not hasattr(string_series.iteritems(), 'reverse')