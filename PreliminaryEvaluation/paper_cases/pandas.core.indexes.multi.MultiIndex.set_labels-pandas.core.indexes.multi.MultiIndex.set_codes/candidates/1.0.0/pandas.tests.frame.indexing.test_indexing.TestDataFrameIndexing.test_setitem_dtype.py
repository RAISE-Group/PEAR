@pytest.mark.parametrize('dtype', ['int32', 'int64', 'float32', 'float64'])
def test_setitem_dtype(self, dtype, float_frame):
    arr = np.random.randn(len(float_frame))
    float_frame[dtype] = np.array(arr, dtype=dtype)
    assert float_frame[dtype].dtype.name == dtype