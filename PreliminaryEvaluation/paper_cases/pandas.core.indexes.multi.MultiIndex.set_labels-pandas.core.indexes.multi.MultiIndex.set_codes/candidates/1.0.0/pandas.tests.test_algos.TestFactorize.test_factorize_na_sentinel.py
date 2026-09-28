@pytest.mark.parametrize('sort', [True, False])
@pytest.mark.parametrize('na_sentinel', [-1, -10, 100])
@pytest.mark.parametrize('data, uniques', [(np.array(['b', 'a', None, 'b'], dtype=object), np.array(['b', 'a'], dtype=object)), (pd.array([2, 1, np.nan, 2], dtype='Int64'), pd.array([2, 1], dtype='Int64'))], ids=['numpy_array', 'extension_array'])
def test_factorize_na_sentinel(self, sort, na_sentinel, data, uniques):
    codes, uniques = algos.factorize(data, sort=sort, na_sentinel=na_sentinel)
    if sort:
        expected_codes = np.array([1, 0, na_sentinel, 1], dtype=np.intp)
        expected_uniques = algos.safe_sort(uniques)
    else:
        expected_codes = np.array([0, 1, na_sentinel, 0], dtype=np.intp)
        expected_uniques = uniques
    tm.assert_numpy_array_equal(codes, expected_codes)
    if isinstance(data, np.ndarray):
        tm.assert_numpy_array_equal(uniques, expected_uniques)
    else:
        tm.assert_extension_array_equal(uniques, expected_uniques)