@pytest.mark.parametrize('na_sentinel', [-1, -2])
def test_factorize(self, data_for_grouping, na_sentinel):
    codes, uniques = pd.factorize(data_for_grouping, na_sentinel=na_sentinel)
    expected_codes = np.array([0, 0, na_sentinel, na_sentinel, 1, 1, 0, 2], dtype=np.intp)
    expected_uniques = data_for_grouping.take([0, 4, 7])
    tm.assert_numpy_array_equal(codes, expected_codes)
    self.assert_extension_array_equal(uniques, expected_uniques)