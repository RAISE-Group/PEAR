@pytest.mark.parametrize('right_vals', [['foo', 'bar'], Series(['foo', 'bar']).astype('category')])
def test_different(self, right_vals):
    left = DataFrame({'A': ['foo', 'bar'], 'B': Series(['foo', 'bar']).astype('category'), 'C': [1, 2], 'D': [1.0, 2.0], 'E': Series([1, 2], dtype='uint64'), 'F': Series([1, 2], dtype='int32')})
    right = DataFrame({'A': right_vals})
    result = pd.merge(left, right, on='A')
    assert is_object_dtype(result.A.dtype)