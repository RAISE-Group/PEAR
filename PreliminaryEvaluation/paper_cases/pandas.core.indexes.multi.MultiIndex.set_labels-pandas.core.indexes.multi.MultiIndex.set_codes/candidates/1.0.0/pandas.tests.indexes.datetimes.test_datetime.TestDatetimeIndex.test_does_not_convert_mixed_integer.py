def test_does_not_convert_mixed_integer(self):
    df = tm.makeCustomDataframe(10, 10, data_gen_f=lambda *args, **kwargs: randn(), r_idx_type='i', c_idx_type='dt')
    cols = df.columns.join(df.index, how='outer')
    joined = cols.join(df.columns)
    assert cols.dtype == np.dtype('O')
    assert cols.dtype == joined.dtype
    tm.assert_numpy_array_equal(cols.values, joined.values)