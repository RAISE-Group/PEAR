def test_asof_datetime_partial(self):
    index = pd.date_range('2010-01-01', periods=2, freq='m')
    expected = Timestamp('2010-02-28')
    result = index.asof('2010-02')
    assert result == expected
    assert not isinstance(result, Index)