@pytest.mark.parametrize('weekday', range(7))
def test_is_on_offset(self, weekday):
    offset = Week(weekday=weekday)
    for day in range(1, 8):
        date = datetime(2008, 1, day)
        if day % 7 == weekday:
            expected = True
        else:
            expected = False
    assert_is_on_offset(offset, date, expected)