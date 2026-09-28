@pytest.mark.parametrize('data', [pd.date_range('2000', periods=4), pd.date_range('2000', periods=4, tz='US/Central'), pd.period_range('2000', periods=4), pd.timedelta_range(0, periods=4)])
def test_combine_datetlike_udf(self, data):
    df = pd.DataFrame({'A': data})
    other = df.copy()
    df.iloc[1, 0] = None

    def combiner(a, b):
        return b
    result = df.combine(other, combiner)
    tm.assert_frame_equal(result, other)