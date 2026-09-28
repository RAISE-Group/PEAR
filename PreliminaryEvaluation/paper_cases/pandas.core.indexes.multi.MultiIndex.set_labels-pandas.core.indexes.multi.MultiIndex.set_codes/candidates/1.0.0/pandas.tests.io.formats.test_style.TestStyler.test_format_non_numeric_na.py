def test_format_non_numeric_na(self):
    df = pd.DataFrame({'object': [None, np.nan, 'foo'], 'datetime': [None, pd.NaT, pd.Timestamp('20120101')]})
    ctx = df.style.set_na_rep('NA')._translate()
    assert ctx['body'][0][1]['display_value'] == 'NA'
    assert ctx['body'][0][2]['display_value'] == 'NA'
    assert ctx['body'][1][1]['display_value'] == 'NA'
    assert ctx['body'][1][2]['display_value'] == 'NA'
    ctx = df.style.format(None, na_rep='-')._translate()
    assert ctx['body'][0][1]['display_value'] == '-'
    assert ctx['body'][0][2]['display_value'] == '-'
    assert ctx['body'][1][1]['display_value'] == '-'
    assert ctx['body'][1][2]['display_value'] == '-'