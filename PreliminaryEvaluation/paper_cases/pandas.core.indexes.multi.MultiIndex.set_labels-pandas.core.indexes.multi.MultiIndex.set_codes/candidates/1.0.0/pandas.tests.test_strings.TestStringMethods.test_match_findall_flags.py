def test_match_findall_flags(self):
    data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com', 'Rob': 'rob@gmail.com', 'Wes': np.nan}
    data = Series(data)
    pat = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})'
    result = data.str.extract(pat, flags=re.IGNORECASE, expand=True)
    assert result.iloc[0].tolist() == ['dave', 'google', 'com']
    result = data.str.match(pat, flags=re.IGNORECASE)
    assert result[0]
    result = data.str.findall(pat, flags=re.IGNORECASE)
    assert result[0][0] == ('dave', 'google', 'com')
    result = data.str.count(pat, flags=re.IGNORECASE)
    assert result[0] == 1
    with tm.assert_produces_warning(UserWarning):
        result = data.str.contains(pat, flags=re.IGNORECASE)
    assert result[0]