@pytest.mark.parametrize('date, format', [('2017-20', '%Y-%W'), ('20 Sunday', '%W %A'), ('20 Sun', '%W %a'), ('2017-21', '%Y-%U'), ('20 Sunday', '%U %A'), ('20 Sun', '%U %a')])
def test_week_without_day_and_calendar_year(self, date, format):
    msg = "Cannot use '%W' or '%U' without day and year"
    with pytest.raises(ValueError, match=msg):
        pd.to_datetime(date, format=format)