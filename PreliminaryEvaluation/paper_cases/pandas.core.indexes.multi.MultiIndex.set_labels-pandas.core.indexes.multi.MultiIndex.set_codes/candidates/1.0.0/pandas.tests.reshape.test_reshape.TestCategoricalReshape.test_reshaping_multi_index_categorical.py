def test_reshaping_multi_index_categorical(self):
    cols = ['ItemA', 'ItemB', 'ItemC']
    data = {c: tm.makeTimeDataFrame() for c in cols}
    df = pd.concat({c: data[c].stack() for c in data}, axis='columns')
    df.index.names = ['major', 'minor']
    df['str'] = 'foo'
    df['category'] = df['str'].astype('category')
    result = df['category'].unstack()
    dti = df.index.levels[0]
    c = Categorical(['foo'] * len(dti))
    expected = DataFrame({'A': c.copy(), 'B': c.copy(), 'C': c.copy(), 'D': c.copy()}, columns=Index(list('ABCD'), name='minor'), index=dti.rename('major'))
    tm.assert_frame_equal(result, expected)