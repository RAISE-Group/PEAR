@pytest.mark.parametrize('series', [['1-1', '1-1', np.NaN], ['1-1', '1-2', np.NaN]])
def test_apply_categorical_with_nan_values(self, series):
    s = pd.Series(series, dtype='category')
    result = s.apply(lambda x: x.split('-')[0])
    result = result.astype(object)
    expected = pd.Series(['1', '1', np.NaN], dtype='category')
    expected = expected.astype(object)
    tm.assert_series_equal(result, expected)