@pytest.mark.parametrize('ts', [Timestamp.now(), Timestamp.now('utc')])
@pytest.mark.parametrize('other', [1, np.int64(1), np.array([1, 2], dtype=np.int32), np.array([3, 4], dtype=np.uint64)])
def test_add_int_no_freq_raises(self, ts, other):
    msg = 'Addition/subtraction of integers and integer-arrays'
    with pytest.raises(TypeError, match=msg):
        ts + other
    with pytest.raises(TypeError, match=msg):
        other + ts
    with pytest.raises(TypeError, match=msg):
        ts - other
    with pytest.raises(TypeError):
        other - ts