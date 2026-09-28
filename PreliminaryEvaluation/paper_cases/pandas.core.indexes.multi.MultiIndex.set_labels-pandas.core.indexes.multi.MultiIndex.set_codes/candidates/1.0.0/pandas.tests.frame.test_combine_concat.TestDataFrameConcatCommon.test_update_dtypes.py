def test_update_dtypes(self):
    df = DataFrame([[1.0, 2.0, False, True], [4.0, 5.0, True, False]], columns=['A', 'B', 'bool1', 'bool2'])
    other = DataFrame([[45, 45]], index=[0], columns=['A', 'B'])
    df.update(other)
    expected = DataFrame([[45.0, 45.0, False, True], [4.0, 5.0, True, False]], columns=['A', 'B', 'bool1', 'bool2'])
    tm.assert_frame_equal(df, expected)