def test_date_format_series_raises(self):
    ts = Series(Timestamp('20130101 20:43:42.123'), index=self.ts.index)
    msg = "Invalid value 'foo' for option 'date_unit'"
    with pytest.raises(ValueError, match=msg):
        ts.to_json(date_format='iso', date_unit='foo')