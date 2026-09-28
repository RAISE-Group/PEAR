def test_constructor_datelike_coercion(self):
    s = Series([Timestamp('20130101'), 'NOV'], dtype=object)
    assert s.iloc[0] == Timestamp('20130101')
    assert s.iloc[1] == 'NOV'
    assert s.dtype == object
    belly = '216 3T19'.split()
    wing1 = '2T15 4H19'.split()
    wing2 = '416 4T20'.split()
    mat = pd.to_datetime('2016-01-22 2019-09-07'.split())
    df = pd.DataFrame({'wing1': wing1, 'wing2': wing2, 'mat': mat}, index=belly)
    result = df.loc['3T19']
    assert result.dtype == object
    result = df.loc['216']
    assert result.dtype == object