def test_frame_append_datetime64_col_other_units(self):
    n = 100
    units = ['h', 'm', 's', 'ms', 'D', 'M', 'Y']
    ns_dtype = np.dtype('M8[ns]')
    for unit in units:
        dtype = np.dtype('M8[{unit}]'.format(unit=unit))
        vals = np.arange(n, dtype=np.int64).view(dtype)
        df = DataFrame({'ints': np.arange(n)}, index=np.arange(n))
        df[unit] = vals
        ex_vals = to_datetime(vals.astype('O')).values
        assert df[unit].dtype == ns_dtype
        assert (df[unit].values == ex_vals).all()
    df = DataFrame({'ints': np.arange(n)}, index=np.arange(n))
    df['dates'] = np.arange(n, dtype=np.int64).view(ns_dtype)
    for unit in units:
        dtype = np.dtype('M8[{unit}]'.format(unit=unit))
        vals = np.arange(n, dtype=np.int64).view(dtype)
        tmp = df.copy()
        tmp['dates'] = vals
        ex_vals = to_datetime(vals.astype('O')).values
        assert (tmp['dates'].values == ex_vals).all()