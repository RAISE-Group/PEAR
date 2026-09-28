def test_rename_inplace(self, datetime_series):
    renamer = lambda x: x.strftime('%Y%m%d')
    expected = renamer(datetime_series.index[0])
    datetime_series.rename(renamer, inplace=True)
    assert datetime_series.index[0] == expected