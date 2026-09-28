def test_stack_multiple_bug(self):
    """ bug when some uniques are not present in the data #3170"""
    id_col = [1] * 3 + [2] * 3
    name = ['a'] * 3 + ['b'] * 3
    date = pd.to_datetime(['2013-01-03', '2013-01-04', '2013-01-05'] * 2)
    var1 = np.random.randint(0, 100, 6)
    df = DataFrame(dict(ID=id_col, NAME=name, DATE=date, VAR1=var1))
    multi = df.set_index(['DATE', 'ID'])
    multi.columns.name = 'Params'
    unst = multi.unstack('ID')
    down = unst.resample('W-THU').mean()
    rs = down.stack('ID')
    xp = unst.loc[:, ['VAR1']].resample('W-THU').mean().stack('ID')
    xp.columns.name = 'Params'
    tm.assert_frame_equal(rs, xp)