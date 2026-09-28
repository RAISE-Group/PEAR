def test_agg_namedtuple(self):
    df = pd.DataFrame({'A': [0, 1], 'B': [1, 2]})
    result = df.groupby('A').agg(b=pd.NamedAgg('B', 'sum'), c=pd.NamedAgg(column='B', aggfunc='count'))
    expected = df.groupby('A').agg(b=('B', 'sum'), c=('B', 'count'))
    tm.assert_frame_equal(result, expected)