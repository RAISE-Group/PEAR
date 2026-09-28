def test_infer_dtype_datetime(self):
    arr = np.array([Timestamp('2011-01-01'), Timestamp('2011-01-02')])
    assert lib.infer_dtype(arr, skipna=True) == 'datetime'
    arr = np.array([np.datetime64('2011-01-01'), np.datetime64('2011-01-01')], dtype=object)
    assert lib.infer_dtype(arr, skipna=True) == 'datetime64'
    arr = np.array([datetime(2011, 1, 1), datetime(2012, 2, 1)])
    assert lib.infer_dtype(arr, skipna=True) == 'datetime'
    for n in [pd.NaT, np.nan]:
        arr = np.array([n, pd.Timestamp('2011-01-02')])
        assert lib.infer_dtype(arr, skipna=True) == 'datetime'
        arr = np.array([n, np.datetime64('2011-01-02')])
        assert lib.infer_dtype(arr, skipna=True) == 'datetime64'
        arr = np.array([n, datetime(2011, 1, 1)])
        assert lib.infer_dtype(arr, skipna=True) == 'datetime'
        arr = np.array([n, pd.Timestamp('2011-01-02'), n])
        assert lib.infer_dtype(arr, skipna=True) == 'datetime'
        arr = np.array([n, np.datetime64('2011-01-02'), n])
        assert lib.infer_dtype(arr, skipna=True) == 'datetime64'
        arr = np.array([n, datetime(2011, 1, 1), n])
        assert lib.infer_dtype(arr, skipna=True) == 'datetime'
    arr = np.array([np.timedelta64('nat'), np.datetime64('2011-01-02')], dtype=object)
    assert lib.infer_dtype(arr, skipna=False) == 'mixed'
    arr = np.array([np.datetime64('2011-01-02'), np.timedelta64('nat')], dtype=object)
    assert lib.infer_dtype(arr, skipna=False) == 'mixed'
    arr = np.array([datetime(2011, 1, 1), pd.Timestamp('2011-01-02')])
    assert lib.infer_dtype(arr, skipna=True) == 'datetime'
    arr = np.array([np.datetime64('2011-01-01'), pd.Timestamp('2011-01-02')])
    assert lib.infer_dtype(arr, skipna=True) == 'mixed'
    arr = np.array([pd.Timestamp('2011-01-02'), np.datetime64('2011-01-01')])
    assert lib.infer_dtype(arr, skipna=True) == 'mixed'
    arr = np.array([np.nan, pd.Timestamp('2011-01-02'), 1])
    assert lib.infer_dtype(arr, skipna=True) == 'mixed-integer'
    arr = np.array([np.nan, pd.Timestamp('2011-01-02'), 1.1])
    assert lib.infer_dtype(arr, skipna=True) == 'mixed'
    arr = np.array([np.nan, '2011-01-01', pd.Timestamp('2011-01-02')])
    assert lib.infer_dtype(arr, skipna=True) == 'mixed'