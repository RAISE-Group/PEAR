def test_datetimeindex(self):
    index = date_range('20130102', periods=6)
    s = Series(1, index=index)
    result = s.to_string()
    assert '2013-01-02' in result
    s2 = Series(2, index=[Timestamp('20130111'), NaT])
    s = s2.append(s)
    result = s.to_string()
    assert 'NaT' in result
    result = str(s2.index)
    assert 'NaT' in result