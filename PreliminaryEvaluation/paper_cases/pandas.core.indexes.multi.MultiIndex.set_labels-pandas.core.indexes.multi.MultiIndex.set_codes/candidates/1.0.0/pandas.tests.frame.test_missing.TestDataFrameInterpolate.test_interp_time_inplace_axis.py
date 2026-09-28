@pytest.mark.parametrize('axis', [0, 1])
def test_interp_time_inplace_axis(self, axis):
    periods = 5
    idx = pd.date_range(start='2014-01-01', periods=periods)
    data = np.random.rand(periods, periods)
    data[data < 0.5] = np.nan
    expected = pd.DataFrame(index=idx, columns=idx, data=data)
    result = expected.interpolate(axis=0, method='time')
    expected.interpolate(axis=0, method='time', inplace=True)
    tm.assert_frame_equal(result, expected)