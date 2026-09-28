def test_setitem_other_callable(self):

    def inc(x):
        return x + 1
    df = pd.DataFrame([[-1, 1], [1, -1]])
    df[df > 0] = inc
    expected = pd.DataFrame([[-1, inc], [inc, -1]])
    tm.assert_frame_equal(df, expected)