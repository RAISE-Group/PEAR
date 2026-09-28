def test_fillna_copy_frame(self, data_missing):
    arr = data_missing.take([1, 1])
    df = pd.DataFrame({'A': arr})
    filled_val = df.iloc[0, 0]
    result = df.fillna(filled_val)
    assert df.values.base is not result.values.base
    assert df.A._values.to_dense() is arr.to_dense()