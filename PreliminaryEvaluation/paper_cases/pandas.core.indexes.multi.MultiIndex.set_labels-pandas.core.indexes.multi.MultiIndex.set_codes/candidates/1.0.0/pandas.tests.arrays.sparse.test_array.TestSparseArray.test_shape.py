@pytest.mark.parametrize('data,shape,dtype', [([0, 0, 0, 0, 0], (5,), None), ([], (0,), None), ([0], (1,), None), (['A', 'A', np.nan, 'B'], (4,), np.object)])
def test_shape(self, data, shape, dtype):
    out = SparseArray(data, dtype=dtype)
    assert out.shape == shape