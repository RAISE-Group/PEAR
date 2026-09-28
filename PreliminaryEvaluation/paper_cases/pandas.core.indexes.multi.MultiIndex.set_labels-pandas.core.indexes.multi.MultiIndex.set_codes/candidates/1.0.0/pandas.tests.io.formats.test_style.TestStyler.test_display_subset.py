def test_display_subset(self):
    df = pd.DataFrame([[0.1234, 0.1234], [1.1234, 1.1234]], columns=['a', 'b'])
    ctx = df.style.format({'a': '{:0.1f}', 'b': '{0:.2%}'}, subset=pd.IndexSlice[0, :])._translate()
    expected = '0.1'
    raw_11 = '1.123400'
    assert ctx['body'][0][1]['display_value'] == expected
    assert ctx['body'][1][1]['display_value'] == raw_11
    assert ctx['body'][0][2]['display_value'] == '12.34%'
    ctx = df.style.format('{:0.1f}', subset=pd.IndexSlice[0, :])._translate()
    assert ctx['body'][0][1]['display_value'] == expected
    assert ctx['body'][1][1]['display_value'] == raw_11
    ctx = df.style.format('{:0.1f}', subset=pd.IndexSlice['a'])._translate()
    assert ctx['body'][0][1]['display_value'] == expected
    assert ctx['body'][0][2]['display_value'] == '0.123400'
    ctx = df.style.format('{:0.1f}', subset=pd.IndexSlice[0, 'a'])._translate()
    assert ctx['body'][0][1]['display_value'] == expected
    assert ctx['body'][1][1]['display_value'] == raw_11
    ctx = df.style.format('{:0.1f}', subset=pd.IndexSlice[[0, 1], ['a']])._translate()
    assert ctx['body'][0][1]['display_value'] == expected
    assert ctx['body'][1][1]['display_value'] == '1.1'
    assert ctx['body'][0][2]['display_value'] == '0.123400'
    assert ctx['body'][1][2]['display_value'] == raw_11