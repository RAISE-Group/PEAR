@pytest.mark.parametrize('case', [lambda s: s, lambda s: s.loc])
def test_duplicate_int_indexing(self, case):
    s = pd.Series(range(3), index=[1, 1, 3])
    expected = s[1]
    result = case(s)[[1]]
    tm.assert_series_equal(result, expected)