@pytest.mark.parametrize('values,categories,exp_mode', [([1, 1, 2, 4, 5, 5, 5], [5, 4, 3, 2, 1], [5]), ([1, 1, 1, 4, 5, 5, 5], [5, 4, 3, 2, 1], [5, 1]), ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1]), ([np.nan, np.nan, np.nan, 4, 5], [5, 4, 3, 2, 1], [5, 4]), ([np.nan, np.nan, np.nan, 4, 5, 4], [5, 4, 3, 2, 1], [4]), ([np.nan, np.nan, 4, 5, 4], [5, 4, 3, 2, 1], [4])])
def test_mode(self, values, categories, exp_mode):
    s = Categorical(values, categories=categories, ordered=True)
    res = s.mode()
    exp = Categorical(exp_mode, categories=categories, ordered=True)
    tm.assert_categorical_equal(res, exp)