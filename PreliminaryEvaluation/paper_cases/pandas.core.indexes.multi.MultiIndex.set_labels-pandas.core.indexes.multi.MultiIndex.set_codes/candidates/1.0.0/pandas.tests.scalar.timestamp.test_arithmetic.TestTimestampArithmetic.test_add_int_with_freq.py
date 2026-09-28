@pytest.mark.parametrize('ts', [Timestamp('1776-07-04', freq='D'), Timestamp('1776-07-04', tz='UTC', freq='D')])
@pytest.mark.parametrize('other', [1, np.int64(1), np.array([1, 2], dtype=np.int32), np.array([3, 4], dtype=np.uint64)])
def test_add_int_with_freq(self, ts, other):
    with pytest.raises(TypeError):
        ts + other
    with pytest.raises(TypeError):
        other + ts
    with pytest.raises(TypeError):
        ts - other
    with pytest.raises(TypeError):
        other - ts