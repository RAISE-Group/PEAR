@pytest.mark.parametrize('hour', ['1:00', '1:00AM', time(1), time(1, tzinfo=pytz.UTC)])
def test_at_time_errors(self, hour):
    dti = pd.date_range('2018', periods=3, freq='H')
    df = pd.DataFrame(list(range(len(dti))), index=dti)
    if getattr(hour, 'tzinfo', None) is None:
        result = df.at_time(hour)
        expected = df.iloc[1:2]
        tm.assert_frame_equal(result, expected)
    else:
        with pytest.raises(ValueError, match='Index must be timezone'):
            df.at_time(hour)