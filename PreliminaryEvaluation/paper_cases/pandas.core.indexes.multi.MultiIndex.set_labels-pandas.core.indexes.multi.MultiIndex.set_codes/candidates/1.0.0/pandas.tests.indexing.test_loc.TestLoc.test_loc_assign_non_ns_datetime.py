@pytest.mark.parametrize('unit', ['Y', 'M', 'D', 'h', 'm', 's', 'ms', 'us'])
def test_loc_assign_non_ns_datetime(self, unit):
    df = DataFrame({'timestamp': [np.datetime64('2017-02-11 12:41:29'), np.datetime64('1991-11-07 04:22:37')]})
    df.loc[:, unit] = df.loc[:, 'timestamp'].values.astype('datetime64[{unit}]'.format(unit=unit))
    df['expected'] = df.loc[:, 'timestamp'].values.astype('datetime64[{unit}]'.format(unit=unit))
    expected = Series(df.loc[:, 'expected'], name=unit)
    tm.assert_series_equal(df.loc[:, unit], expected)