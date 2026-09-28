def test_take_empty(self, data, na_value, na_cmp):
    empty = data[:0]
    result = empty.take([-1], allow_fill=True)
    assert na_cmp(result[0], na_value)
    with pytest.raises(IndexError):
        empty.take([-1])
    with pytest.raises(IndexError, match='cannot do a non-empty take'):
        empty.take([0, 1])