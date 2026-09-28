@pytest.mark.parametrize(('data', 'f'), (([1, 1, np.nan], pd.isna), ([1, 2, np.nan], pd.isna), ([1, 1, np.nan], {1: False}), ([1, 2, np.nan], {1: False, 2: False}), ([1, 1, np.nan], pd.Series([False, False])), ([1, 2, np.nan], pd.Series([False, False, False]))))
def test_map_with_nan(self, data, f):
    values = pd.Categorical(data)
    result = values.map(f)
    if data[1] == 1:
        expected = pd.Categorical([False, False, np.nan])
        tm.assert_categorical_equal(result, expected)
    else:
        expected = pd.Index([False, False, np.nan])
        tm.assert_index_equal(result, expected)