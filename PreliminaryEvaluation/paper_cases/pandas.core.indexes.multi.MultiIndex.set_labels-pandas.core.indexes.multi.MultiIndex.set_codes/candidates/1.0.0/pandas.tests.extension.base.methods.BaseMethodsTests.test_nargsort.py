@pytest.mark.parametrize('na_position, expected', [('last', np.array([2, 0, 1], dtype=np.dtype('intp'))), ('first', np.array([1, 2, 0], dtype=np.dtype('intp')))])
def test_nargsort(self, data_missing_for_sorting, na_position, expected):
    result = nargsort(data_missing_for_sorting, na_position=na_position)
    tm.assert_numpy_array_equal(result, expected)