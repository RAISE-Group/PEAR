def test_np_sum(self):
    vals = np.arange(5, dtype=np.int64).view('m8[h]').astype('m8[ns]')
    arr = TimedeltaArray(vals)
    result = np.sum(arr)
    assert result == vals.sum()
    result = np.sum(pd.TimedeltaIndex(arr))
    assert result == vals.sum()