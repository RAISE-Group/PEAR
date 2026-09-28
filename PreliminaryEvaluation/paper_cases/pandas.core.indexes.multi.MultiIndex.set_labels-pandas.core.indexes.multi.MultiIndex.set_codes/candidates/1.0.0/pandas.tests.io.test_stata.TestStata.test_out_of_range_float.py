def test_out_of_range_float(self):
    original = DataFrame({'ColumnOk': [0.0, np.finfo(np.float32).eps, np.finfo(np.float32).max / 10.0], 'ColumnTooBig': [0.0, np.finfo(np.float32).eps, np.finfo(np.float32).max]})
    original.index.name = 'index'
    for col in original:
        original[col] = original[col].astype(np.float32)
    with tm.ensure_clean() as path:
        original.to_stata(path)
        reread = read_stata(path)
        original['ColumnTooBig'] = original['ColumnTooBig'].astype(np.float64)
        tm.assert_frame_equal(original, reread.set_index('index'))
    original.loc[2, 'ColumnTooBig'] = np.inf
    msg = 'Column ColumnTooBig has a maximum value of infinity which is outside the range supported by Stata'
    with pytest.raises(ValueError, match=msg):
        with tm.ensure_clean() as path:
            original.to_stata(path)