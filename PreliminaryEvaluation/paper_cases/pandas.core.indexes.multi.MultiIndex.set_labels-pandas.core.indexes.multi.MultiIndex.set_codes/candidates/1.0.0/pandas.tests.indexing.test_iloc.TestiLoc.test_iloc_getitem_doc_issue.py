def test_iloc_getitem_doc_issue(self):
    arr = np.random.randn(6, 4)
    index = date_range('20130101', periods=6)
    columns = list('ABCD')
    df = DataFrame(arr, index=index, columns=columns)
    df.describe()
    result = df.iloc[3:5, 0:2]
    str(result)
    result.dtypes
    expected = DataFrame(arr[3:5, 0:2], index=index[3:5], columns=columns[0:2])
    tm.assert_frame_equal(result, expected)
    df.columns = list('aaaa')
    result = df.iloc[3:5, 0:2]
    str(result)
    result.dtypes
    expected = DataFrame(arr[3:5, 0:2], index=index[3:5], columns=list('aa'))
    tm.assert_frame_equal(result, expected)
    arr = np.random.randn(6, 4)
    index = list(range(0, 12, 2))
    columns = list(range(0, 8, 2))
    df = DataFrame(arr, index=index, columns=columns)
    df._data.blocks[0].mgr_locs
    result = df.iloc[1:5, 2:4]
    str(result)
    result.dtypes
    expected = DataFrame(arr[1:5, 2:4], index=index[1:5], columns=columns[2:4])
    tm.assert_frame_equal(result, expected)