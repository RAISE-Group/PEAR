def test_is_scalar_pandas_containers(self):
    assert not is_scalar(Series(dtype=object))
    assert not is_scalar(Series([1]))
    assert not is_scalar(DataFrame())
    assert not is_scalar(DataFrame([[1]]))
    assert not is_scalar(Index([]))
    assert not is_scalar(Index([1]))