def _check_basic_constructor(self, empty):
    mat = empty((2, 3), dtype=float)
    frame = DataFrame(mat, columns=['A', 'B', 'C'], index=[1, 2])
    assert len(frame.index) == 2
    assert len(frame.columns) == 3
    frame = DataFrame(empty((3,)), columns=['A'], index=[1, 2, 3])
    assert len(frame.index) == 3
    assert len(frame.columns) == 1
    frame = DataFrame(mat, columns=['A', 'B', 'C'], index=[1, 2], dtype=np.int64)
    assert frame.values.dtype == np.int64
    msg = 'Shape of passed values is \\(2, 3\\), indices imply \\(1, 3\\)'
    with pytest.raises(ValueError, match=msg):
        DataFrame(mat, columns=['A', 'B', 'C'], index=[1])
    msg = 'Shape of passed values is \\(2, 3\\), indices imply \\(2, 2\\)'
    with pytest.raises(ValueError, match=msg):
        DataFrame(mat, columns=['A', 'B'], index=[1, 2])
    with pytest.raises(ValueError, match='Must pass 2-d input'):
        DataFrame(empty((3, 3, 3)), columns=['A', 'B', 'C'], index=[1])
    frame = DataFrame(mat)
    tm.assert_index_equal(frame.index, pd.Int64Index(range(2)))
    tm.assert_index_equal(frame.columns, pd.Int64Index(range(3)))
    frame = DataFrame(mat, index=[1, 2])
    tm.assert_index_equal(frame.columns, pd.Int64Index(range(3)))
    frame = DataFrame(mat, columns=['A', 'B', 'C'])
    tm.assert_index_equal(frame.index, pd.Int64Index(range(2)))
    frame = DataFrame(empty((0, 3)))
    assert len(frame.index) == 0
    frame = DataFrame(empty((3, 0)))
    assert len(frame.columns) == 0