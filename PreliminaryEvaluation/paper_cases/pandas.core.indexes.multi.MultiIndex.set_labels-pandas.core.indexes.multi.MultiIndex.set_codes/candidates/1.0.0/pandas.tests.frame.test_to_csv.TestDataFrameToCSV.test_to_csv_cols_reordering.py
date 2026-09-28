def test_to_csv_cols_reordering(self):
    import pandas as pd
    chunksize = 5
    N = int(chunksize * 2.5)
    df = tm.makeCustomDataframe(N, 3)
    cs = df.columns
    cols = [cs[2], cs[0]]
    with tm.ensure_clean() as path:
        df.to_csv(path, columns=cols, chunksize=chunksize)
        rs_c = pd.read_csv(path, index_col=0)
    tm.assert_frame_equal(df[cols], rs_c, check_names=False)