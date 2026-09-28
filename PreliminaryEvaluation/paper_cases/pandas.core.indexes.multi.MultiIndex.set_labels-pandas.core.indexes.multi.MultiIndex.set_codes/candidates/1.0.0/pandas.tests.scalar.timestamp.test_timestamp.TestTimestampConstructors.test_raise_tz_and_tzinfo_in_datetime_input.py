@pytest.mark.parametrize('box', [datetime, Timestamp])
def test_raise_tz_and_tzinfo_in_datetime_input(self, box):
    kwargs = {'year': 2018, 'month': 1, 'day': 1, 'tzinfo': utc}
    with pytest.raises(ValueError, match='Cannot pass a datetime or Timestamp'):
        Timestamp(box(**kwargs), tz='US/Pacific')
    with pytest.raises(ValueError, match='Cannot pass a datetime or Timestamp'):
        Timestamp(box(**kwargs), tzinfo=pytz.timezone('US/Pacific'))