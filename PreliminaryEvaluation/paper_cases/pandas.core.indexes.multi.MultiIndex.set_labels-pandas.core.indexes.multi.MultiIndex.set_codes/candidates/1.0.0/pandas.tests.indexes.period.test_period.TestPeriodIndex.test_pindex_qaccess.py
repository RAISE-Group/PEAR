def test_pindex_qaccess(self):
    pi = PeriodIndex(['2Q05', '3Q05', '4Q05', '1Q06', '2Q06'], freq='Q')
    s = Series(np.random.rand(len(pi)), index=pi).cumsum()
    assert s['05Q4'] == s[2]