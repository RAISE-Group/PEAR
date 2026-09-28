def test_concat_different_extension_dtypes_upcasts(self):
    a = pd.Series(pd.core.arrays.integer_array([1, 2]))
    b = pd.Series(to_decimal([1, 2]))
    result = pd.concat([a, b], ignore_index=True)
    expected = pd.Series([1, 2, Decimal(1), Decimal(2)], dtype=object)
    tm.assert_series_equal(result, expected)