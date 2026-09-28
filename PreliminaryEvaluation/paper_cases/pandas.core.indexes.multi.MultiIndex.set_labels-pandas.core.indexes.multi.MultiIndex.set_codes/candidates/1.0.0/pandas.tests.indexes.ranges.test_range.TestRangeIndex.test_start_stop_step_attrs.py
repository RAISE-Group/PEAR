@pytest.mark.parametrize('index, start, stop, step', [(RangeIndex(5), 0, 5, 1), (RangeIndex(0, 5), 0, 5, 1), (RangeIndex(5, step=2), 0, 5, 2), (RangeIndex(1, 5, 2), 1, 5, 2)])
def test_start_stop_step_attrs(self, index, start, stop, step):
    assert index.start == start
    assert index.stop == stop
    assert index.step == step