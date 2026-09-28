@pytest.mark.parametrize('value', [[], iter([]), (_ for _ in [])])
@pytest.mark.parametrize('klass', [Index, Float64Index, Int64Index, UInt64Index, CategoricalIndex, DatetimeIndex, TimedeltaIndex])
def test_constructor_empty(self, value, klass):
    empty = klass(value)
    assert isinstance(empty, klass)
    assert not len(empty)