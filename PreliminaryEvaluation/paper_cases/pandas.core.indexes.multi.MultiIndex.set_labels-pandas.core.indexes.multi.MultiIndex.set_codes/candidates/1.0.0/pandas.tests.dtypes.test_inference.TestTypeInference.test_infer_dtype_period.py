def test_infer_dtype_period(self):
    arr = np.array([pd.Period('2011-01', freq='D'), pd.Period('2011-02', freq='D')])
    assert lib.infer_dtype(arr, skipna=True) == 'period'
    arr = np.array([pd.Period('2011-01', freq='D'), pd.Period('2011-02', freq='M')])
    assert lib.infer_dtype(arr, skipna=True) == 'period'
    for n in [pd.NaT, np.nan]:
        arr = np.array([n, pd.Period('2011-01', freq='D')])
        assert lib.infer_dtype(arr, skipna=True) == 'period'
        arr = np.array([n, pd.Period('2011-01', freq='D'), n])
        assert lib.infer_dtype(arr, skipna=True) == 'period'
    arr = np.array([np.datetime64('nat'), pd.Period('2011-01', freq='M')], dtype=object)
    assert lib.infer_dtype(arr, skipna=False) == 'mixed'
    arr = np.array([pd.Period('2011-01', freq='M'), np.datetime64('nat')], dtype=object)
    assert lib.infer_dtype(arr, skipna=False) == 'mixed'