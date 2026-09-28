def test_constructor_same(self):
    index = RangeIndex(1, 5, 2)
    result = RangeIndex(index, copy=False)
    assert result.identical(index)
    result = RangeIndex(index, copy=True)
    tm.assert_index_equal(result, index, exact=True)
    result = RangeIndex(index)
    tm.assert_index_equal(result, index, exact=True)
    with pytest.raises(ValueError, match='Incorrect `dtype` passed: expected signed integer, received float64'):
        RangeIndex(index, dtype='float64')