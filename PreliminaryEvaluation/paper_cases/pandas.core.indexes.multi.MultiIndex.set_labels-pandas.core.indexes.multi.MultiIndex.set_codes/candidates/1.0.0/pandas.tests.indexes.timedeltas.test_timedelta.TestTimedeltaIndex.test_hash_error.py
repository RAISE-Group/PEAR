def test_hash_error(self):
    index = timedelta_range('1 days', periods=10)
    with pytest.raises(TypeError, match=f'unhashable type: {repr(type(index).__name__)}'):
        hash(index)