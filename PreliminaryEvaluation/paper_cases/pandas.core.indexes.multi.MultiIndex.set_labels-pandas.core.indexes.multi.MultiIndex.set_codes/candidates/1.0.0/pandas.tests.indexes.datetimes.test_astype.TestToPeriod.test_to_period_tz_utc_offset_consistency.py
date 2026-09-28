@pytest.mark.parametrize('tz', ['Etc/GMT-1', 'Etc/GMT+1'])
def test_to_period_tz_utc_offset_consistency(self, tz):
    ts = pd.date_range('1/1/2000', '2/1/2000', tz='Etc/GMT-1')
    with tm.assert_produces_warning(UserWarning):
        result = ts.to_period()[0]
        expected = ts[0].to_period()
        assert result == expected