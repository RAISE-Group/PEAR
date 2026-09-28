def test_apply_differently_indexed(self):
    df = DataFrame(np.random.randn(20, 10))
    result0 = df.apply(Series.describe, axis=0)
    expected0 = DataFrame({i: v.describe() for i, v in df.items()}, columns=df.columns)
    tm.assert_frame_equal(result0, expected0)
    result1 = df.apply(Series.describe, axis=1)
    expected1 = DataFrame({i: v.describe() for i, v in df.T.items()}, columns=df.index).T
    tm.assert_frame_equal(result1, expected1)