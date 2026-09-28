@pytest.mark.parametrize('val', [[b'E\xc9, 17', b'', b'a', b'b', b'c'], [b'E\xc9, 17', b'a', b'b', b'c'], [b'EE, 17', b'', b'a', b'b', b'c'], [b'E\xc9, 17', b'\xf8\xfc', b'a', b'b', b'c'], [b'', b'a', b'b', b'c'], [b'\xf8\xfc', b'a', b'b', b'c'], [b'A\xf8\xfc', b'', b'a', b'b', b'c'], [np.nan, b'', b'b', b'c'], [b'A\xf8\xfc', np.nan, b'', b'b', b'c']])
@pytest.mark.parametrize('dtype', ['category', object])
def test_latin_encoding(self, setup_path, dtype, val):
    enc = 'latin-1'
    nan_rep = ''
    key = 'data'
    val = [x.decode(enc) if isinstance(x, bytes) else x for x in val]
    ser = pd.Series(val, dtype=dtype)
    with ensure_clean_path(setup_path) as store:
        ser.to_hdf(store, key, format='table', encoding=enc, nan_rep=nan_rep)
        retr = read_hdf(store, key)
    s_nan = ser.replace(nan_rep, np.nan)
    if is_categorical_dtype(s_nan):
        assert is_categorical_dtype(retr)
        tm.assert_series_equal(s_nan, retr, check_dtype=False, check_categorical=False)
    else:
        tm.assert_series_equal(s_nan, retr)