def test_constructor_Series_named_and_columns(self):
    s0 = Series(range(5), name=0)
    s1 = Series(range(5), name=1)
    tm.assert_frame_equal(pd.DataFrame(s0, columns=[0]), s0.to_frame())
    tm.assert_frame_equal(pd.DataFrame(s1, columns=[1]), s1.to_frame())
    assert pd.DataFrame(s0, columns=[1]).empty
    assert pd.DataFrame(s1, columns=[0]).empty