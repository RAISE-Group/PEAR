@pytest.mark.parametrize('dtype', [np.float32, np.float64])
def test_float_comparison_bin_op(self, dtype):
    df = pd.DataFrame({'x': np.array([0], dtype=dtype)})
    res = df.eval('x < -0.1')
    assert res.values == np.array([False])
    res = df.eval('-5 > x')
    assert res.values == np.array([False])