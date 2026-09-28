@pytest.mark.parametrize('fill_value, expected_output', [(Series(['a', 'b', 'c', 'd', 'e']), ['a', 'b', 'b', 'd', 'e']), (Series(['b', 'd', 'a', 'd', 'a']), ['a', 'd', 'b', 'd', 'a']), (Series(Categorical(['b', 'd', 'a', 'd', 'a'], categories=['b', 'c', 'd', 'e', 'a'])), ['a', 'd', 'b', 'd', 'a'])])
def test_fillna_categorical_with_new_categories(self, fill_value, expected_output):
    data = ['a', np.nan, 'b', np.nan, np.nan]
    s = Series(Categorical(data, categories=['a', 'b', 'c', 'd', 'e']))
    exp = Series(Categorical(expected_output, categories=['a', 'b', 'c', 'd', 'e']))
    tm.assert_series_equal(s.fillna(fill_value), exp)