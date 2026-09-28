def test_split_noargs(self):
    s = Series(['Wes McKinney', 'Travis  Oliphant'])
    result = s.str.split()
    expected = ['Travis', 'Oliphant']
    assert result[1] == expected
    result = s.str.rsplit()
    assert result[1] == expected