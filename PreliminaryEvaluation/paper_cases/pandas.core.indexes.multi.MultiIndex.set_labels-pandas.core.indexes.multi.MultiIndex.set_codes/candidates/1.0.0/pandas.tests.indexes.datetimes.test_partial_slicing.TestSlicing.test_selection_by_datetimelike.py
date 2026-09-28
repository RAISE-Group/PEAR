@pytest.mark.parametrize('datetimelike', [Timestamp('20130101'), datetime(2013, 1, 1), np.datetime64('2013-01-01T00:00', 'ns')])
@pytest.mark.parametrize('op,expected', [(operator.lt, [True, False, False, False]), (operator.le, [True, True, False, False]), (operator.eq, [False, True, False, False]), (operator.gt, [False, False, False, True])])
def test_selection_by_datetimelike(self, datetimelike, op, expected):
    df = DataFrame({'A': [pd.Timestamp('20120101'), pd.Timestamp('20130101'), np.nan, pd.Timestamp('20130103')]})
    result = op(df.A, datetimelike)
    expected = Series(expected, name='A')
    tm.assert_series_equal(result, expected)