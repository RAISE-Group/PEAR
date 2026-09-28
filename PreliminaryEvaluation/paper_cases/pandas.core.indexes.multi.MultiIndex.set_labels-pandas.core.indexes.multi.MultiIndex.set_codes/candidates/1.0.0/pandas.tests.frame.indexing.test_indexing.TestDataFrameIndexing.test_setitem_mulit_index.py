def test_setitem_mulit_index(self):
    it = (['jim', 'joe', 'jolie'], ['first', 'last'], ['left', 'center', 'right'])
    cols = MultiIndex.from_product(it)
    index = pd.date_range('20141006', periods=20)
    vals = np.random.randint(1, 1000, (len(index), len(cols)))
    df = pd.DataFrame(vals, columns=cols, index=index)
    i, j = (df.index.values.copy(), it[-1][:])
    np.random.shuffle(i)
    df['jim'] = df['jolie'].loc[i, ::-1]
    tm.assert_frame_equal(df['jim'], df['jolie'])
    np.random.shuffle(j)
    df['joe', 'first'] = df['jolie', 'last'].loc[i, j]
    tm.assert_frame_equal(df['joe', 'first'], df['jolie', 'last'])
    np.random.shuffle(j)
    df['joe', 'last'] = df['jolie', 'first'].loc[i, j]
    tm.assert_frame_equal(df['joe', 'last'], df['jolie', 'first'])