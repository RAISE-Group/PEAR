def test_alignment_non_pandas(self):
    index = ['A', 'B', 'C']
    columns = ['X', 'Y', 'Z']
    df = pd.DataFrame(np.random.randn(3, 3), index=index, columns=columns)
    align = pd.core.ops._align_method_FRAME
    for val in [[1, 2, 3], (1, 2, 3), np.array([1, 2, 3], dtype=np.int64), range(1, 4)]:
        tm.assert_series_equal(align(df, val, 'index'), Series([1, 2, 3], index=df.index))
        tm.assert_series_equal(align(df, val, 'columns'), Series([1, 2, 3], index=df.columns))
    msg = 'Unable to coerce to Series, length must be 3: given 2'
    for val in [[1, 2], (1, 2), np.array([1, 2]), range(1, 3)]:
        with pytest.raises(ValueError, match=msg):
            align(df, val, 'index')
        with pytest.raises(ValueError, match=msg):
            align(df, val, 'columns')
    val = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    tm.assert_frame_equal(align(df, val, 'index'), DataFrame(val, index=df.index, columns=df.columns))
    tm.assert_frame_equal(align(df, val, 'columns'), DataFrame(val, index=df.index, columns=df.columns))
    msg = 'Unable to coerce to DataFrame, shape must be'
    val = np.array([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError, match=msg):
        align(df, val, 'index')
    with pytest.raises(ValueError, match=msg):
        align(df, val, 'columns')
    val = np.zeros((3, 3, 3))
    with pytest.raises(ValueError):
        align(df, val, 'index')
    with pytest.raises(ValueError):
        align(df, val, 'columns')