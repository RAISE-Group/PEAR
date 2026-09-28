@pytest.mark.parametrize('fill_value, expected_output', [('a', ['a', 'a', 'b', 'a', 'a']), ({1: 'a', 3: 'b', 4: 'b'}, ['a', 'a', 'b', 'b', 'b']), ({1: 'a'}, ['a', 'a', 'b', np.nan, np.nan]), ({1: 'a', 3: 'b'}, ['a', 'a', 'b', 'b', np.nan]), (Series('a'), ['a', np.nan, 'b', np.nan, np.nan]), (Series('a', index=[1]), ['a', 'a', 'b', np.nan, np.nan]), (Series({1: 'a', 3: 'b'}), ['a', 'a', 'b', 'b', np.nan]), (Series(['a', 'b'], index=[3, 4]), ['a', np.nan, 'b', 'a', 'b'])])
def test_fillna_categorical(self, fill_value, expected_output):
    data = ['a', np.nan, 'b', np.nan, np.nan]
    s = Series(Categorical(data, categories=['a', 'b']))
    exp = Series(Categorical(expected_output, categories=['a', 'b']))
    tm.assert_series_equal(s.fillna(fill_value), exp)