def test_to_html_compat(self):
    df = tm.makeCustomDataframe(4, 3, data_gen_f=lambda *args: rand(), c_idx_names=False, r_idx_names=False).applymap('{0:.3f}'.format).astype(float)
    out = df.to_html()
    res = self.read_html(out, attrs={'class': 'dataframe'}, index_col=0)[0]
    tm.assert_frame_equal(res, df)