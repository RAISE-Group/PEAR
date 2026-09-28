def test_comparison_of_ordered_categorical_with_nan_to_scalar(self, compare_operators_no_eq_ne):
    cat = Categorical([1, 2, 3, None], categories=[1, 2, 3], ordered=True)
    scalar = 2
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', RuntimeWarning)
        expected = getattr(np.array(cat), compare_operators_no_eq_ne)(scalar)
    actual = getattr(cat, compare_operators_no_eq_ne)(scalar)
    tm.assert_numpy_array_equal(actual, expected)