@pytest.mark.parametrize('prefix', ['', 'dateutil/'])
def test_dti_constructor_static_tzinfo(self, prefix):
    index = DatetimeIndex([datetime(2012, 1, 1)], tz=prefix + 'EST')
    index.hour
    index[0]