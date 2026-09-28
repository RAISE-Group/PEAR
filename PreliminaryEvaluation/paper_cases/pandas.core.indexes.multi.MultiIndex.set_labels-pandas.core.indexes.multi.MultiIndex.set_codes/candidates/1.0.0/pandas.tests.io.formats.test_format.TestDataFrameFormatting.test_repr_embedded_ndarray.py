def test_repr_embedded_ndarray(self):
    arr = np.empty(10, dtype=[('err', object)])
    for i in range(len(arr)):
        arr['err'][i] = np.random.randn(i)
    df = DataFrame(arr)
    repr(df['err'])
    repr(df)
    df.to_string()