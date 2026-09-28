@pytest.mark.parametrize('freq, n', [('H', 1), ('T', 60), ('S', 3600)])
def test_dti_tz_convert_trans_pos_plus_1__bug(self, freq, n):
    idx = date_range(datetime(2011, 3, 26, 23), datetime(2011, 3, 27, 1), freq=freq)
    idx = idx.tz_localize('UTC')
    idx = idx.tz_convert('Europe/Moscow')
    expected = np.repeat(np.array([3, 4, 5]), np.array([n, n, 1]))
    tm.assert_index_equal(idx.hour, Index(expected))