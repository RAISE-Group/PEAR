def test_getitem_setitem_float_labels(self):
    index = Index([1.5, 2, 3, 4, 5])
    df = DataFrame(np.random.randn(5, 5), index=index)
    result = df.loc[1.5:4]
    expected = df.reindex([1.5, 2, 3, 4])
    tm.assert_frame_equal(result, expected)
    assert len(result) == 4
    result = df.loc[4:5]
    expected = df.reindex([4, 5])
    tm.assert_frame_equal(result, expected, check_index_type=False)
    assert len(result) == 2
    result = df.loc[4:5]
    expected = df.reindex([4.0, 5.0])
    tm.assert_frame_equal(result, expected)
    assert len(result) == 2
    result = df.loc[1:2]
    expected = df.iloc[0:2]
    tm.assert_frame_equal(result, expected)
    df.loc[1:2] = 0
    result = df[1:2]
    assert (result == 0).all().all()
    index = Index([1.0, 2.5, 3.5, 4.5, 5.0])
    df = DataFrame(np.random.randn(5, 5), index=index)
    msg = "cannot do slice indexing on <class 'pandas\\.core\\.indexes\\.numeric\\.Float64Index'> with these indexers \\[1.0\\] of <class 'float'>"
    with pytest.raises(TypeError, match=msg):
        df.iloc[1.0:5]
    result = df.iloc[4:5]
    expected = df.reindex([5.0])
    tm.assert_frame_equal(result, expected)
    assert len(result) == 1
    cp = df.copy()
    with pytest.raises(TypeError):
        cp.iloc[1.0:5] = 0
    with pytest.raises(TypeError):
        result = cp.iloc[1.0:5] == 0
    assert result.values.all()
    assert (cp.iloc[0:1] == df.iloc[0:1]).values.all()
    cp = df.copy()
    cp.iloc[4:5] = 0
    assert (cp.iloc[4:5] == 0).values.all()
    assert (cp.iloc[0:4] == df.iloc[0:4]).values.all()
    result = df.loc[1.0:5]
    expected = df
    tm.assert_frame_equal(result, expected)
    assert len(result) == 5
    result = df.loc[1.1:5]
    expected = df.reindex([2.5, 3.5, 4.5, 5.0])
    tm.assert_frame_equal(result, expected)
    assert len(result) == 4
    result = df.loc[4.51:5]
    expected = df.reindex([5.0])
    tm.assert_frame_equal(result, expected)
    assert len(result) == 1
    result = df.loc[1.0:5.0]
    expected = df.reindex([1.0, 2.5, 3.5, 4.5, 5.0])
    tm.assert_frame_equal(result, expected)
    assert len(result) == 5
    cp = df.copy()
    cp.loc[1.0:5.0] = 0
    result = cp.loc[1.0:5.0]
    assert (result == 0).values.all()