@pytest.mark.parametrize('file', ['dta19_115', 'dta19_117'])
def test_categorical_order(self, file):
    expected = [(True, 'ordered', ['a', 'b', 'c', 'd', 'e'], np.arange(5)), (True, 'reverse', ['a', 'b', 'c', 'd', 'e'], np.arange(5)[::-1]), (True, 'noorder', ['a', 'b', 'c', 'd', 'e'], np.array([2, 1, 4, 0, 3])), (True, 'floating', ['a', 'b', 'c', 'd', 'e'], np.arange(0, 5)), (True, 'float_missing', ['a', 'd', 'e'], np.array([0, 1, 2, -1, -1])), (False, 'nolabel', [1.0, 2.0, 3.0, 4.0, 5.0], np.arange(5)), (True, 'int32_mixed', ['d', 2, 'e', 'b', 'a'], np.arange(5))]
    cols = []
    for is_cat, col, labels, codes in expected:
        if is_cat:
            cols.append((col, pd.Categorical.from_codes(codes, labels)))
        else:
            cols.append((col, pd.Series(labels, dtype=np.float32)))
    expected = DataFrame.from_dict(dict(cols))
    file = getattr(self, file)
    parsed = read_stata(file)
    tm.assert_frame_equal(expected, parsed, check_categorical=False)
    for col in expected:
        if is_categorical_dtype(expected[col]):
            tm.assert_series_equal(expected[col].cat.codes, parsed[col].cat.codes)
            tm.assert_index_equal(expected[col].cat.categories, parsed[col].cat.categories)