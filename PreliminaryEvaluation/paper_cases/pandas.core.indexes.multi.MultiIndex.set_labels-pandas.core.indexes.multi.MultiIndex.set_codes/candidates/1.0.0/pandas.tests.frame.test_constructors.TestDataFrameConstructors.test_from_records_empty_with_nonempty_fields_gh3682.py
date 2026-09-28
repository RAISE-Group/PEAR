def test_from_records_empty_with_nonempty_fields_gh3682(self):
    a = np.array([(1, 2)], dtype=[('id', np.int64), ('value', np.int64)])
    df = DataFrame.from_records(a, index='id')
    tm.assert_index_equal(df.index, Index([1], name='id'))
    assert df.index.name == 'id'
    tm.assert_index_equal(df.columns, Index(['value']))
    b = np.array([], dtype=[('id', np.int64), ('value', np.int64)])
    df = DataFrame.from_records(b, index='id')
    tm.assert_index_equal(df.index, Index([], name='id'))
    assert df.index.name == 'id'