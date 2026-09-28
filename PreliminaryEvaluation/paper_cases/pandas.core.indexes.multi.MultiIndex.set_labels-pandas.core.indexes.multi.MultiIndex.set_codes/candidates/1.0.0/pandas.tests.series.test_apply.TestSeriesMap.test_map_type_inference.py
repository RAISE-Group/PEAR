def test_map_type_inference(self):
    s = Series(range(3))
    s2 = s.map(lambda x: np.where(x == 0, 0, 1))
    assert issubclass(s2.dtype.type, np.integer)