def test_init_with_na_rep(self):
    df = pd.DataFrame([[None, None], [1.1, 1.2]], columns=['A', 'B'])
    ctx = Styler(df, na_rep='NA')._translate()
    assert ctx['body'][0][1]['display_value'] == 'NA'
    assert ctx['body'][0][2]['display_value'] == 'NA'