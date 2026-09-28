@pytest.mark.parametrize('s, _format, dt', [['2015-1-1', '%G-%V-%u', datetime(2014, 12, 29, 0, 0)], ['2015-1-4', '%G-%V-%u', datetime(2015, 1, 1, 0, 0)], ['2015-1-7', '%G-%V-%u', datetime(2015, 1, 4, 0, 0)]])
def test_to_datetime_iso_week_year_format(self, s, _format, dt):
    assert to_datetime(s, format=_format) == dt