@pytest.mark.parametrize('data, dtype', [([1], pd.Int64Dtype()), ([1], pd.CategoricalDtype()), ([pd.Interval(left=0, right=5)], pd.IntervalDtype()), ([pd.Period('2000-03', freq='M')], pd.PeriodDtype('M')), ([1], pd.SparseDtype())])
def test_other_dtypes(self, data, dtype):
    df = pd.DataFrame(data, dtype=dtype)
    result = df.append(df.iloc[0]).iloc[-1]
    expected = pd.Series(data, name=0, dtype=dtype)
    tm.assert_series_equal(result, expected)