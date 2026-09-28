def test_insert(self):
    expected = PeriodIndex(['2017Q1', pd.NaT, '2017Q2', '2017Q3', '2017Q4'], freq='Q')
    for na in (np.nan, pd.NaT, None):
        result = period_range('2017Q1', periods=4, freq='Q').insert(1, na)
        tm.assert_index_equal(result, expected)