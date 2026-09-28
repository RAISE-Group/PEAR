@pytest.mark.parametrize('fold', [0, 1])
@pytest.mark.parametrize('tz', ['dateutil/Europe/London', 'Europe/London'])
def test_replace_dst_fold(self, fold, tz):
    d = datetime(2019, 10, 27, 2, 30)
    ts = Timestamp(d, tz=tz)
    result = ts.replace(hour=1, fold=fold)
    expected = Timestamp(datetime(2019, 10, 27, 1, 30)).tz_localize(tz, ambiguous=not fold)
    assert result == expected