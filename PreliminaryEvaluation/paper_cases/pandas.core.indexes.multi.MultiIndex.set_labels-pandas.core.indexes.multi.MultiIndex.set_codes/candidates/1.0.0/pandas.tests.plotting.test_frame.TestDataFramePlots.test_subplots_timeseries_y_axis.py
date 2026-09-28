def test_subplots_timeseries_y_axis(self):
    data = {'numeric': np.array([1, 2, 5]), 'timedelta': [pd.Timedelta(-10, unit='s'), pd.Timedelta(10, unit='m'), pd.Timedelta(10, unit='h')], 'datetime_no_tz': [pd.to_datetime('2017-08-01 00:00:00'), pd.to_datetime('2017-08-01 02:00:00'), pd.to_datetime('2017-08-02 00:00:00')], 'datetime_all_tz': [pd.to_datetime('2017-08-01 00:00:00', utc=True), pd.to_datetime('2017-08-01 02:00:00', utc=True), pd.to_datetime('2017-08-02 00:00:00', utc=True)], 'text': ['This', 'should', 'fail']}
    testdata = DataFrame(data)
    ax_numeric = testdata.plot(y='numeric')
    assert (ax_numeric.get_lines()[0].get_data()[1] == testdata['numeric'].values).all()
    ax_timedelta = testdata.plot(y='timedelta')
    assert (ax_timedelta.get_lines()[0].get_data()[1] == testdata['timedelta'].values).all()
    ax_datetime_no_tz = testdata.plot(y='datetime_no_tz')
    assert (ax_datetime_no_tz.get_lines()[0].get_data()[1] == testdata['datetime_no_tz'].values).all()
    ax_datetime_all_tz = testdata.plot(y='datetime_all_tz')
    assert (ax_datetime_all_tz.get_lines()[0].get_data()[1] == testdata['datetime_all_tz'].values).all()
    msg = 'no numeric data to plot'
    with pytest.raises(TypeError, match=msg):
        testdata.plot(y='text')