def test_uses_pandas_na(self):
    a = pd.array([1, None], dtype=pd.Int64Dtype())
    assert a[1] is pd.NA