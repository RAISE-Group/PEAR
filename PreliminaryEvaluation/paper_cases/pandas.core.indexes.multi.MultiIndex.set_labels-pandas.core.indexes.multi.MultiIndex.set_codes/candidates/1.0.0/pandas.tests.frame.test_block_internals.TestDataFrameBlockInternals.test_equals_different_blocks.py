def test_equals_different_blocks(self):
    df0 = pd.DataFrame({'A': ['x', 'y'], 'B': [1, 2], 'C': ['w', 'z']})
    df1 = df0.reset_index()[['A', 'B', 'C']]
    assert df0._data.blocks[0].dtype != df1._data.blocks[0].dtype
    tm.assert_frame_equal(df0, df1)
    assert df0.equals(df1)
    assert df1.equals(df0)