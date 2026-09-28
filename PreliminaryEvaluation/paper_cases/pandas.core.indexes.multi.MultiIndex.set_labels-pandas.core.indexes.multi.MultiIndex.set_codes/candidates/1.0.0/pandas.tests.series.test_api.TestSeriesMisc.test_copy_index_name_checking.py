def test_copy_index_name_checking(self, datetime_series):
    datetime_series.index.name = None
    assert datetime_series.index.name is None
    assert datetime_series is datetime_series
    cp = datetime_series.copy()
    cp.index.name = 'foo'
    printing.pprint_thing(datetime_series.index.name)
    assert datetime_series.index.name is None