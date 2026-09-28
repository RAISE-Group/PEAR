def test_constructor_dict_cast(self):
    test_data = {'A': {'1': 1, '2': 2}, 'B': {'1': '1', '2': '2', '3': '3'}}
    frame = DataFrame(test_data, dtype=float)
    assert len(frame) == 3
    assert frame['B'].dtype == np.float64
    assert frame['A'].dtype == np.float64
    frame = DataFrame(test_data)
    assert len(frame) == 3
    assert frame['B'].dtype == np.object_
    assert frame['A'].dtype == np.float64
    test_data = {'A': dict(zip(range(20), tm.makeStringIndex(20))), 'B': dict(zip(range(15), np.random.randn(15)))}
    frame = DataFrame(test_data, dtype=float)
    assert len(frame) == 20
    assert frame['A'].dtype == np.object_
    assert frame['B'].dtype == np.float64