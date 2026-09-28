def test_to_frame_with_falsey_names(self):
    result = Series(name=0, dtype=object).to_frame().dtypes
    expected = Series({0: object})
    tm.assert_series_equal(result, expected)
    result = DataFrame(Series(name=0, dtype=object)).dtypes
    tm.assert_series_equal(result, expected)