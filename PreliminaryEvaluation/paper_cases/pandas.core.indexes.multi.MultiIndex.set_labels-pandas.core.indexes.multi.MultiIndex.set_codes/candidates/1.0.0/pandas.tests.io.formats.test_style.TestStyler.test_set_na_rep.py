def test_set_na_rep(self):
    df = pd.DataFrame([[None, None], [1.1, 1.2]], columns=['A', 'B'])
    ctx = df.style.set_na_rep('NA')._translate()
    assert ctx['body'][0][1]['display_value'] == 'NA'
    assert ctx['body'][0][2]['display_value'] == 'NA'
    ctx = df.style.set_na_rep('NA').format(None, na_rep='-', subset=['B'])._translate()
    assert ctx['body'][0][1]['display_value'] == 'NA'
    assert ctx['body'][0][2]['display_value'] == '-'