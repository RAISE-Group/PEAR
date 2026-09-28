def test_drop_column(self):
    expected = self.read_csv(self.csv15)
    expected['byte_'] = expected['byte_'].astype(np.int8)
    expected['int_'] = expected['int_'].astype(np.int16)
    expected['long_'] = expected['long_'].astype(np.int32)
    expected['float_'] = expected['float_'].astype(np.float32)
    expected['double_'] = expected['double_'].astype(np.float64)
    expected['date_td'] = expected['date_td'].apply(datetime.strptime, args=('%Y-%m-%d',))
    columns = ['byte_', 'int_', 'long_']
    expected = expected[columns]
    dropped = read_stata(self.dta15_117, convert_dates=True, columns=columns)
    tm.assert_frame_equal(expected, dropped)
    columns = ['int_', 'long_', 'byte_']
    expected = expected[columns]
    reordered = read_stata(self.dta15_117, convert_dates=True, columns=columns)
    tm.assert_frame_equal(expected, reordered)
    msg = 'columns contains duplicate entries'
    with pytest.raises(ValueError, match=msg):
        columns = ['byte_', 'byte_']
        read_stata(self.dta15_117, convert_dates=True, columns=columns)
    msg = 'The following columns were not found in the Stata data set: not_found'
    with pytest.raises(ValueError, match=msg):
        columns = ['byte_', 'int_', 'long_', 'not_found']
        read_stata(self.dta15_117, convert_dates=True, columns=columns)