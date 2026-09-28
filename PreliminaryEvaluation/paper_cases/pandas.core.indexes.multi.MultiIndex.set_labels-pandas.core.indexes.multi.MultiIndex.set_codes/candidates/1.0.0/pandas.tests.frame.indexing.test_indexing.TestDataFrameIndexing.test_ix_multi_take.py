def test_ix_multi_take(self):
    df = DataFrame(np.random.randn(3, 2))
    rs = df.loc[df.index == 0, :]
    xp = df.reindex([0])
    tm.assert_frame_equal(rs, xp)
    ' #1321\n        df = DataFrame(np.random.randn(3, 2))\n        rs = df.loc[df.index==0, df.columns==1]\n        xp = df.reindex([0], [1])\n        tm.assert_frame_equal(rs, xp)\n        '