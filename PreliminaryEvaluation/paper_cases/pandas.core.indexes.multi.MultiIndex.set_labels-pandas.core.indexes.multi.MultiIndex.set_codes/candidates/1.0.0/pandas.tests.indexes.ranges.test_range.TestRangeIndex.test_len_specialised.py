@pytest.mark.parametrize('step', set(range(-5, 6)) - {0})
def test_len_specialised(self, step):
    start, stop = (0, 5) if step > 0 else (5, 0)
    arr = np.arange(start, stop, step)
    index = RangeIndex(start, stop, step)
    assert len(index) == len(arr)
    index = RangeIndex(stop, start, step)
    assert len(index) == 0