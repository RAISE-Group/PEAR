def test_bool_flex_frame(self):
    data = np.random.randn(5, 3)
    other_data = np.random.randn(5, 3)
    df = pd.DataFrame(data)
    other = pd.DataFrame(other_data)
    ndim_5 = np.ones(df.shape + (1, 3))

    def _check_unaligned_frame(meth, op, df, other):
        part_o = other.loc[3:, 1:].copy()
        rs = meth(part_o)
        xp = op(df, part_o.reindex(index=df.index, columns=df.columns))
        tm.assert_frame_equal(rs, xp)
    assert df.eq(df).values.all()
    assert not df.ne(df).values.any()
    for op in ['eq', 'ne', 'gt', 'lt', 'ge', 'le']:
        f = getattr(df, op)
        o = getattr(operator, op)
        tm.assert_frame_equal(f(other), o(df, other))
        _check_unaligned_frame(f, o, df, other)
        tm.assert_frame_equal(f(other.values), o(df, other.values))
        tm.assert_frame_equal(f(0), o(df, 0))
        msg = 'Unable to coerce to Series/DataFrame'
        tm.assert_frame_equal(f(np.nan), o(df, np.nan))
        with pytest.raises(ValueError, match=msg):
            f(ndim_5)

    def _test_seq(df, idx_ser, col_ser):
        idx_eq = df.eq(idx_ser, axis=0)
        col_eq = df.eq(col_ser)
        idx_ne = df.ne(idx_ser, axis=0)
        col_ne = df.ne(col_ser)
        tm.assert_frame_equal(col_eq, df == pd.Series(col_ser))
        tm.assert_frame_equal(col_eq, -col_ne)
        tm.assert_frame_equal(idx_eq, -idx_ne)
        tm.assert_frame_equal(idx_eq, df.T.eq(idx_ser).T)
        tm.assert_frame_equal(col_eq, df.eq(list(col_ser)))
        tm.assert_frame_equal(idx_eq, df.eq(pd.Series(idx_ser), axis=0))
        tm.assert_frame_equal(idx_eq, df.eq(list(idx_ser), axis=0))
        idx_gt = df.gt(idx_ser, axis=0)
        col_gt = df.gt(col_ser)
        idx_le = df.le(idx_ser, axis=0)
        col_le = df.le(col_ser)
        tm.assert_frame_equal(col_gt, df > pd.Series(col_ser))
        tm.assert_frame_equal(col_gt, -col_le)
        tm.assert_frame_equal(idx_gt, -idx_le)
        tm.assert_frame_equal(idx_gt, df.T.gt(idx_ser).T)
        idx_ge = df.ge(idx_ser, axis=0)
        col_ge = df.ge(col_ser)
        idx_lt = df.lt(idx_ser, axis=0)
        col_lt = df.lt(col_ser)
        tm.assert_frame_equal(col_ge, df >= pd.Series(col_ser))
        tm.assert_frame_equal(col_ge, -col_lt)
        tm.assert_frame_equal(idx_ge, -idx_lt)
        tm.assert_frame_equal(idx_ge, df.T.ge(idx_ser).T)
    idx_ser = pd.Series(np.random.randn(5))
    col_ser = pd.Series(np.random.randn(3))
    _test_seq(df, idx_ser, col_ser)
    _test_seq(df, idx_ser.values, col_ser.values)
    df.loc[0, 0] = np.nan
    rs = df.eq(df)
    assert not rs.loc[0, 0]
    rs = df.ne(df)
    assert rs.loc[0, 0]
    rs = df.gt(df)
    assert not rs.loc[0, 0]
    rs = df.lt(df)
    assert not rs.loc[0, 0]
    rs = df.ge(df)
    assert not rs.loc[0, 0]
    rs = df.le(df)
    assert not rs.loc[0, 0]