def test_to_numpy_copy(self):
    arr = np.random.randn(4, 3)
    df = pd.DataFrame(arr)
    assert df.values.base is arr
    assert df.to_numpy(copy=False).base is arr
    assert df.to_numpy(copy=True).base is None