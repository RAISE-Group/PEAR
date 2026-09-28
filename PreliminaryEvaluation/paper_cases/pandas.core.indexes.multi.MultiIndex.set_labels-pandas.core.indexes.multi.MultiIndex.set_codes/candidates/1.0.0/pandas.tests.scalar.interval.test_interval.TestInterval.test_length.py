@pytest.mark.parametrize('left, right, expected', [(0, 5, 5), (-2, 5.5, 7.5), (10, 10, 0), (10, np.inf, np.inf), (-np.inf, -5, np.inf), (-np.inf, np.inf, np.inf), (Timedelta('0 days'), Timedelta('5 days'), Timedelta('5 days')), (Timedelta('10 days'), Timedelta('10 days'), Timedelta('0 days')), (Timedelta('1H10M'), Timedelta('5H5M'), Timedelta('3H55M')), (Timedelta('5S'), Timedelta('1H'), Timedelta('59M55S'))])
def test_length(self, left, right, expected):
    iv = Interval(left, right)
    result = iv.length
    assert result == expected