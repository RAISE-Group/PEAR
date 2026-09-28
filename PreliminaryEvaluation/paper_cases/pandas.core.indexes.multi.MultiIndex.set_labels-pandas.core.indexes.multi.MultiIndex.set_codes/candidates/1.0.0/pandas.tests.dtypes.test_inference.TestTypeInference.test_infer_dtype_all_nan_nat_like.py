def test_infer_dtype_all_nan_nat_like(self):
    arr = np.array([np.nan, np.nan])
    assert lib.infer_dtype(arr, skipna=True) == 'floating'
    arr = np.array([np.nan, np.nan, None])
    assert lib.infer_dtype(arr, skipna=True) == 'empty'
    assert lib.infer_dtype(arr, skipna=False) == 'mixed'
    arr = np.array([None, np.nan, np.nan])
    assert lib.infer_dtype(arr, skipna=True) == 'empty'
    assert lib.infer_dtype(arr, skipna=False) == 'mixed'
    arr = np.array([pd.NaT])
    assert lib.infer_dtype(arr, skipna=False) == 'datetime'
    arr = np.array([pd.NaT, np.nan])
    assert lib.infer_dtype(arr, skipna=False) == 'datetime'
    arr = np.array([np.nan, pd.NaT])
    assert lib.infer_dtype(arr, skipna=False) == 'datetime'
    arr = np.array([np.nan, pd.NaT, np.nan])
    assert lib.infer_dtype(arr, skipna=False) == 'datetime'
    arr = np.array([None, pd.NaT, None])
    assert lib.infer_dtype(arr, skipna=False) == 'datetime'
    arr = np.array([np.datetime64('nat')])
    assert lib.infer_dtype(arr, skipna=False) == 'datetime64'
    for n in [np.nan, pd.NaT, None]:
        arr = np.array([n, np.datetime64('nat'), n])
        assert lib.infer_dtype(arr, skipna=False) == 'datetime64'
        arr = np.array([pd.NaT, n, np.datetime64('nat'), n])
        assert lib.infer_dtype(arr, skipna=False) == 'datetime64'
    arr = np.array([np.timedelta64('nat')], dtype=object)
    assert lib.infer_dtype(arr, skipna=False) == 'timedelta'
    for n in [np.nan, pd.NaT, None]:
        arr = np.array([n, np.timedelta64('nat'), n])
        assert lib.infer_dtype(arr, skipna=False) == 'timedelta'
        arr = np.array([pd.NaT, n, np.timedelta64('nat'), n])
        assert lib.infer_dtype(arr, skipna=False) == 'timedelta'
    arr = np.array([pd.NaT, np.datetime64('nat'), np.timedelta64('nat'), np.nan])
    assert lib.infer_dtype(arr, skipna=False) == 'mixed'
    arr = np.array([np.timedelta64('nat'), np.datetime64('nat')], dtype=object)
    assert lib.infer_dtype(arr, skipna=False) == 'mixed'