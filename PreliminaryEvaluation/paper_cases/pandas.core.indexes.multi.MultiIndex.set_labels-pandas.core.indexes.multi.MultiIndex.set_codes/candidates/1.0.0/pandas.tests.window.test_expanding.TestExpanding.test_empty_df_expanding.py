@pytest.mark.parametrize('expander', [1, pytest.param('ls', marks=pytest.mark.xfail(reason='GH#16425 expanding with offset not supported'))])
def test_empty_df_expanding(self, expander):
    expected = DataFrame()
    result = DataFrame().expanding(expander).sum()
    tm.assert_frame_equal(result, expected)
    expected = DataFrame(index=pd.DatetimeIndex([]))
    result = DataFrame(index=pd.DatetimeIndex([])).expanding(expander).sum()
    tm.assert_frame_equal(result, expected)