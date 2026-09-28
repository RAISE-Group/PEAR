def test_constructor_dtype_nocast_view(self):
    df = DataFrame([[1, 2]])
    should_be_view = DataFrame(df, dtype=df[0].dtype)
    should_be_view[0][0] = 99
    assert df.values[0, 0] == 99
    should_be_view = DataFrame(df.values, dtype=df[0].dtype)
    should_be_view[0][0] = 97
    assert df.values[0, 0] == 97