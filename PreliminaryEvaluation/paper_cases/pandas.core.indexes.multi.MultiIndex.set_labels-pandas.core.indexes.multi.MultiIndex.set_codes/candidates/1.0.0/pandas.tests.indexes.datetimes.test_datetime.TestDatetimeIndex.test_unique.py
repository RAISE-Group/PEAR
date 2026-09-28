@pytest.mark.parametrize('arr, expected', [(pd.DatetimeIndex(['2017', '2017']), pd.DatetimeIndex(['2017'])), (pd.DatetimeIndex(['2017', '2017'], tz='US/Eastern'), pd.DatetimeIndex(['2017'], tz='US/Eastern'))])
def test_unique(self, arr, expected):
    result = arr.unique()
    tm.assert_index_equal(result, expected)
    assert result[0] == expected[0]