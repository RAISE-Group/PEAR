def test_interval(self):
    idx = pd.IntervalIndex.from_breaks(range(5), closed='both')
    inferred = lib.infer_dtype(idx, skipna=False)
    assert inferred == 'interval'
    inferred = lib.infer_dtype(idx._data, skipna=False)
    assert inferred == 'interval'
    inferred = lib.infer_dtype(pd.Series(idx), skipna=False)
    assert inferred == 'interval'