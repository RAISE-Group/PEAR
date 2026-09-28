def test_objects(self):
    arr = np.random.randint(0, 100, size=50).astype('O')
    result = algos.unique(arr)
    assert isinstance(result, np.ndarray)