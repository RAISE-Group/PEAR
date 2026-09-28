def test_partial_set_empty_frame_set_series(self):
    df = DataFrame(Series(dtype=object))
    tm.assert_frame_equal(df, DataFrame({0: Series(dtype=object)}))
    df = DataFrame(Series(name='foo', dtype=object))
    tm.assert_frame_equal(df, DataFrame({'foo': Series(dtype=object)}))