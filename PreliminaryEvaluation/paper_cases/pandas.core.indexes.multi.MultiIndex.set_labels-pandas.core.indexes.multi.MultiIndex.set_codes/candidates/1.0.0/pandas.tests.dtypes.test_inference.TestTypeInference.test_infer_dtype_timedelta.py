def test_infer_dtype_timedelta(self):
    arr = np.array([pd.Timedelta('1 days'), pd.Timedelta('2 days')])
    assert lib.infer_dtype(arr, skipna=True) == 'timedelta'
    arr = np.array([np.timedelta64(1, 'D'), np.timedelta64(2, 'D')], dtype=object)
    assert lib.infer_dtype(arr, skipna=True) == 'timedelta'
    arr = np.array([timedelta(1), timedelta(2)])
    assert lib.infer_dtype(arr, skipna=True) == 'timedelta'
    for n in [pd.NaT, np.nan]:
        arr = np.array([n, Timedelta('1 days')])
        assert lib.infer_dtype(arr, skipna=True) == 'timedelta'
        arr = np.array([n, np.timedelta64(1, 'D')])
        assert lib.infer_dtype(arr, skipna=True) == 'timedelta'
        arr = np.array([n, timedelta(1)])
        assert lib.infer_dtype(arr, skipna=True) == 'timedelta'
        arr = np.array([n, pd.Timedelta('1 days'), n])
        assert lib.infer_dtype(arr, skipna=True) == 'timedelta'
        arr = np.array([n, np.timedelta64(1, 'D'), n])
        assert lib.infer_dtype(arr, skipna=True) == 'timedelta'
        arr = np.array([n, timedelta(1), n])
        assert lib.infer_dtype(arr, skipna=True) == 'timedelta'
    arr = np.array([np.datetime64('nat'), np.timedelta64(1, 'D')], dtype=object)
    assert lib.infer_dtype(arr, skipna=False) == 'mixed'
    arr = np.array([np.timedelta64(1, 'D'), np.datetime64('nat')], dtype=object)
    assert lib.infer_dtype(arr, skipna=False) == 'mixed'