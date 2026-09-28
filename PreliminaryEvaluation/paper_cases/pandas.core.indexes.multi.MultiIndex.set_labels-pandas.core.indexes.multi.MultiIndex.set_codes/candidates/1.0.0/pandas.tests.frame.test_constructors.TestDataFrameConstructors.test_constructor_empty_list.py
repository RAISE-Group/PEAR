def test_constructor_empty_list(self):
    df = DataFrame([], index=[])
    expected = DataFrame(index=[])
    tm.assert_frame_equal(df, expected)
    df = DataFrame([], columns=['A', 'B'])
    expected = DataFrame({}, columns=['A', 'B'])
    tm.assert_frame_equal(df, expected)

    def empty_gen():
        return
        yield
    df = DataFrame(empty_gen(), columns=['A', 'B'])
    tm.assert_frame_equal(df, expected)