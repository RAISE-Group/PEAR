def test_display_dict(self):
    df = pd.DataFrame([[0.1234, 0.1234], [1.1234, 1.1234]], columns=['a', 'b'])
    ctx = df.style.format({'a': '{:0.1f}', 'b': '{0:.2%}'})._translate()
    assert ctx['body'][0][1]['display_value'] == '0.1'
    assert ctx['body'][0][2]['display_value'] == '12.34%'
    df['c'] = ['aaa', 'bbb']
    ctx = df.style.format({'a': '{:0.1f}', 'c': str.upper})._translate()
    assert ctx['body'][0][1]['display_value'] == '0.1'
    assert ctx['body'][0][3]['display_value'] == 'AAA'