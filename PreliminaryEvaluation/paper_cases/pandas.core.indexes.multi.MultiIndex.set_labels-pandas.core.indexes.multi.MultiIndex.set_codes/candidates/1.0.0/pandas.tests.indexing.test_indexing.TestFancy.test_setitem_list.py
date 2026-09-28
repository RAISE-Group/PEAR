def test_setitem_list(self):
    df = DataFrame(index=[0, 1], columns=[0])
    df.iloc[1, 0] = [1, 2, 3]
    df.iloc[1, 0] = [1, 2]
    result = DataFrame(index=[0, 1], columns=[0])
    result.iloc[1, 0] = [1, 2]
    tm.assert_frame_equal(result, df)

    class TO:

        def __init__(self, value):
            self.value = value

        def __str__(self) -> str:
            return '[{0}]'.format(self.value)
        __repr__ = __str__

        def __eq__(self, other) -> bool:
            return self.value == other.value

        def view(self):
            return self
    df = DataFrame(index=[0, 1], columns=[0])
    df.iloc[1, 0] = TO(1)
    df.iloc[1, 0] = TO(2)
    result = DataFrame(index=[0, 1], columns=[0])
    result.iloc[1, 0] = TO(2)
    tm.assert_frame_equal(result, df)
    df = DataFrame(index=[0, 1], columns=[0])
    df.iloc[1, 0] = TO(1)
    df.iloc[1, 0] = np.nan
    result = DataFrame(index=[0, 1], columns=[0])
    tm.assert_frame_equal(result, df)