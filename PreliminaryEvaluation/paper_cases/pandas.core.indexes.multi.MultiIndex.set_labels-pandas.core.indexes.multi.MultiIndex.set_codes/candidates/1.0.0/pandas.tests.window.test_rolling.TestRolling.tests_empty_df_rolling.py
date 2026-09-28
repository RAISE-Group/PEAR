@pytest.mark.parametrize('roller', ['1s', 1])
def tests_empty_df_rolling(self, roller):
    expected = DataFrame()
    result = DataFrame().rolling(roller).sum()
    tm.assert_frame_equal(result, expected)
    expected = DataFrame(index=pd.DatetimeIndex([]))
    result = DataFrame(index=pd.DatetimeIndex([])).rolling(roller).sum()
    tm.assert_frame_equal(result, expected)