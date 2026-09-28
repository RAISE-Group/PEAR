def test_replace_doesnt_replace_without_regex(self):
    raw = 'fol T_opp T_Dir T_Enh\n        0    1     0     0    vo\n        1    2    vr     0     0\n        2    2     0     0     0\n        3    3     0    bt     0'
    df = pd.read_csv(StringIO(raw), sep='\\s+')
    res = df.replace({'\\D': 1})
    tm.assert_frame_equal(df, res)