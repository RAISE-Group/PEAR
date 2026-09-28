@pytest.mark.parametrize('dti,exp', [(Series([1, 2], index=pd.DatetimeIndex([0, 31536000000])), DataFrame(np.repeat([[1, 2]], 2, axis=0), dtype='int64')), (tm.makeTimeSeries(nper=30), DataFrame(np.repeat([[1, 2]], 30, axis=0), dtype='int64'))])
def test_apply_series_on_date_time_index_aware_series(self, dti, exp):
    index = dti.tz_localize('UTC').index
    result = pd.Series(index).apply(lambda x: pd.Series([1, 2]))
    tm.assert_frame_equal(result, exp)