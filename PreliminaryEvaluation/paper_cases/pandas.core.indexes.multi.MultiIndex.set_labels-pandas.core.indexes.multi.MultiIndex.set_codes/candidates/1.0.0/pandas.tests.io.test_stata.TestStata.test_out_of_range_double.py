def test_out_of_range_double(self):
    df = DataFrame({'ColumnOk': [0.0, np.finfo(np.double).eps, 4.49423283715579e+307], 'ColumnTooBig': [0.0, np.finfo(np.double).eps, np.finfo(np.double).max]})
    msg = 'Column ColumnTooBig has a maximum value \\(.+\\) outside the range supported by Stata \\(.+\\)'
    with pytest.raises(ValueError, match=msg):
        with tm.ensure_clean() as path:
            df.to_stata(path)
    df.loc[2, 'ColumnTooBig'] = np.inf
    msg = 'Column ColumnTooBig has a maximum value of infinity which is outside the range supported by Stata'
    with pytest.raises(ValueError, match=msg):
        with tm.ensure_clean() as path:
            df.to_stata(path)