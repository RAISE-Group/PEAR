def test_infer_row_shape(self):
    df = pd.DataFrame(np.random.rand(10, 2))
    result = df.apply(np.fft.fft, axis=0)
    assert result.shape == (10, 2)
    result = df.apply(np.fft.rfft, axis=0)
    assert result.shape == (6, 2)