def test_setitem_with_string_index(self):
    x = pd.Series([1, 2, 3], index=['Date', 'b', 'other'])
    x['Date'] = date.today()
    assert x.Date == date.today()
    assert x['Date'] == date.today()