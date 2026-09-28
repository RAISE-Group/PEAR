def test_delete(self):
    idx = RangeIndex(5, name='Foo')
    expected = idx[1:].astype(int)
    result = idx.delete(0)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    expected = idx[:-1].astype(int)
    result = idx.delete(-1)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    with pytest.raises((IndexError, ValueError)):
        result = idx.delete(len(idx))