def test_hash_pandas_object_works(self, data, as_frame):
    data = pd.Series(data)
    if as_frame:
        data = data.to_frame()
    a = pd.util.hash_pandas_object(data)
    b = pd.util.hash_pandas_object(data)
    self.assert_equal(a, b)