@pytest.mark.parametrize('na_sentinel', [-1, -2])
def test_factorize_equivalence(self, data_for_grouping, na_sentinel):
    codes_1, uniques_1 = pd.factorize(data_for_grouping, na_sentinel=na_sentinel)
    codes_2, uniques_2 = data_for_grouping.factorize(na_sentinel=na_sentinel)
    tm.assert_numpy_array_equal(codes_1, codes_2)
    self.assert_extension_array_equal(uniques_1, uniques_2)