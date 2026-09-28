def test_deepcopy(self, float_frame):
    cp = deepcopy(float_frame)
    series = cp['A']
    series[:] = 10
    for idx, value in series.items():
        assert float_frame['A'][idx] != value