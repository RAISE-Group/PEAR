@pytest.mark.parametrize('categorical, numeric', [(pd.Categorical('A', categories=['A', 'B']), [1]), (pd.Categorical(('A',), categories=['A', 'B']), [1]), (pd.Categorical(('A', 'B'), categories=['A', 'B']), [1, 2])])
def test_replace_categorical(self, categorical, numeric):
    s = pd.Series(categorical)
    result = s.replace({'A': 1, 'B': 2})
    expected = pd.Series(numeric)
    tm.assert_series_equal(expected, result, check_dtype=False)