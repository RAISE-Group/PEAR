def test_from_records_to_records(self):
    arr = np.zeros((2,), dtype='i4,f4,a10')
    arr[:] = [(1, 2.0, 'Hello'), (2, 3.0, 'World')]
    frame = DataFrame.from_records(arr)
    index = pd.Index(np.arange(len(arr))[::-1])
    indexed_frame = DataFrame.from_records(arr, index=index)
    tm.assert_index_equal(indexed_frame.index, index)
    arr2 = np.zeros((2, 3))
    tm.assert_frame_equal(DataFrame.from_records(arr2), DataFrame(arr2))
    msg = 'Shape of passed values is \\(2, 3\\), indices imply \\(1, 3\\)'
    with pytest.raises(ValueError, match=msg):
        DataFrame.from_records(arr, index=index[:-1])
    indexed_frame = DataFrame.from_records(arr, index='f1')
    records = indexed_frame.to_records()
    assert len(records.dtype.names) == 3
    records = indexed_frame.to_records(index=False)
    assert len(records.dtype.names) == 2
    assert 'index' not in records.dtype.names