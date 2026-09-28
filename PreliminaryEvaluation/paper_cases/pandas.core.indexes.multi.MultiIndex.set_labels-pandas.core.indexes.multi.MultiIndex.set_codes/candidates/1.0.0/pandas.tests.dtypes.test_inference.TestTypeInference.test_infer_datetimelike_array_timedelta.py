@pytest.mark.parametrize('data', [[timedelta(2017, 6, 12), timedelta(2017, 3, 11)], [timedelta(2017, 6, 12), date(2017, 3, 11)], [np.timedelta64(2017, 'D'), np.timedelta64(6, 's')], [np.timedelta64(2017, 'D'), timedelta(2017, 3, 11)]])
def test_infer_datetimelike_array_timedelta(self, data):
    assert lib.infer_datetimelike_array(data) == 'timedelta'