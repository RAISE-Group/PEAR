def test_concat_iterables(self):
    df1 = DataFrame([1, 2, 3])
    df2 = DataFrame([4, 5, 6])
    expected = DataFrame([1, 2, 3, 4, 5, 6])
    tm.assert_frame_equal(concat((df1, df2), ignore_index=True), expected)
    tm.assert_frame_equal(concat([df1, df2], ignore_index=True), expected)
    tm.assert_frame_equal(concat((df for df in (df1, df2)), ignore_index=True), expected)
    tm.assert_frame_equal(concat(deque((df1, df2)), ignore_index=True), expected)

    class CustomIterator1:

        def __len__(self) -> int:
            return 2

        def __getitem__(self, index):
            try:
                return {0: df1, 1: df2}[index]
            except KeyError:
                raise IndexError
    tm.assert_frame_equal(pd.concat(CustomIterator1(), ignore_index=True), expected)

    class CustomIterator2(abc.Iterable):

        def __iter__(self):
            yield df1
            yield df2
    tm.assert_frame_equal(pd.concat(CustomIterator2(), ignore_index=True), expected)