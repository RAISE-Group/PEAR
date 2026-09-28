def test_map_with_categorical_series(self):
    a = pd.Index([1, 2, 3, 4])
    b = pd.Series(['even', 'odd', 'even', 'odd'], dtype='category')
    c = pd.Series(['even', 'odd', 'even', 'odd'])
    exp = CategoricalIndex(['odd', 'even', 'odd', np.nan])
    tm.assert_index_equal(a.map(b), exp)
    exp = pd.Index(['odd', 'even', 'odd', np.nan])
    tm.assert_index_equal(a.map(c), exp)