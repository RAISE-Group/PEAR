def test_where(self, float_string_frame, mixed_float_frame, mixed_int_frame):
    default_frame = DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])

    def _safe_add(df):

        def is_ok(s):
            return issubclass(s.dtype.type, (np.integer, np.floating)) and s.dtype != 'uint8'
        return DataFrame(dict(((c, s + 1) if is_ok(s) else (c, s) for c, s in df.items())))

    def _check_get(df, cond, check_dtypes=True):
        other1 = _safe_add(df)
        rs = df.where(cond, other1)
        rs2 = df.where(cond.values, other1)
        for k, v in rs.items():
            exp = Series(np.where(cond[k], df[k], other1[k]), index=v.index)
            tm.assert_series_equal(v, exp, check_names=False)
        tm.assert_frame_equal(rs, rs2)
        if check_dtypes:
            assert (rs.dtypes == df.dtypes).all()
    for df in [default_frame, float_string_frame, mixed_float_frame, mixed_int_frame]:
        if df is float_string_frame:
            with pytest.raises(TypeError):
                df > 0
            continue
        cond = df > 0
        _check_get(df, cond)
    df = DataFrame({c: Series([1] * 3, dtype=c) for c in ['float32', 'float64', 'int32', 'int64']})
    df.iloc[1, :] = 0
    result = df.dtypes
    expected = Series([np.dtype('float32'), np.dtype('float64'), np.dtype('int32'), np.dtype('int64')], index=['float32', 'float64', 'int32', 'int64'])
    tm.assert_series_equal(result, expected)

    def _check_align(df, cond, other, check_dtypes=True):
        rs = df.where(cond, other)
        for i, k in enumerate(rs.columns):
            result = rs[k]
            d = df[k].values
            c = cond[k].reindex(df[k].index).fillna(False).values
            if is_scalar(other):
                o = other
            elif isinstance(other, np.ndarray):
                o = Series(other[:, i], index=result.index).values
            else:
                o = other[k].values
            new_values = d if c.all() else np.where(c, d, o)
            expected = Series(new_values, index=result.index, name=k)
            tm.assert_series_equal(result, expected, check_dtype=False)
        if check_dtypes and (not isinstance(other, np.ndarray)):
            assert (rs.dtypes == df.dtypes).all()
    for df in [float_string_frame, mixed_float_frame, mixed_int_frame]:
        if df is float_string_frame:
            with pytest.raises(TypeError):
                df > 0
            continue
        cond = (df > 0)[1:]
        _check_align(df, cond, _safe_add(df))
        cond = df > 0
        _check_align(df, cond, _safe_add(df).values)
        cond = df > 0
        check_dtypes = all((not issubclass(s.type, np.integer) for s in df.dtypes))
        _check_align(df, cond, np.nan, check_dtypes=check_dtypes)
    df = default_frame
    err1 = (df + 1).values[0:2, :]
    msg = 'other must be the same shape as self when an ndarray'
    with pytest.raises(ValueError, match=msg):
        df.where(cond, err1)
    err2 = cond.iloc[:2, :].values
    other1 = _safe_add(df)
    msg = 'Array conditional must be same shape as self'
    with pytest.raises(ValueError, match=msg):
        df.where(err2, other1)
    with pytest.raises(ValueError, match=msg):
        df.mask(True)
    with pytest.raises(ValueError, match=msg):
        df.mask(0)

    def _check_set(df, cond, check_dtypes=True):
        dfi = df.copy()
        econd = cond.reindex_like(df).fillna(True)
        expected = dfi.mask(~econd)
        dfi.where(cond, np.nan, inplace=True)
        tm.assert_frame_equal(dfi, expected)
        if check_dtypes:
            for k, v in df.dtypes.items():
                if issubclass(v.type, np.integer) and (not cond[k].all()):
                    v = np.dtype('float64')
                assert dfi[k].dtype == v
    for df in [default_frame, float_string_frame, mixed_float_frame, mixed_int_frame]:
        if df is float_string_frame:
            with pytest.raises(TypeError):
                df > 0
            continue
        cond = df > 0
        _check_set(df, cond)
        cond = df >= 0
        _check_set(df, cond)
        cond = (df >= 0)[1:]
        _check_set(df, cond)
    df = DataFrame({'a': range(3), 'b': range(4, 7)})
    result = df.where(df['a'] == 1)
    expected = df[df['a'] == 1].reindex(df.index)
    tm.assert_frame_equal(result, expected)