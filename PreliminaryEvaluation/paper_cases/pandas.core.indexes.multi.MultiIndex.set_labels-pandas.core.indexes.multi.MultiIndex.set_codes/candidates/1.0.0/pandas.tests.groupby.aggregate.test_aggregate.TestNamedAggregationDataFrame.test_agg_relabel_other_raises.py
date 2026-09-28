def test_agg_relabel_other_raises(self):
    df = pd.DataFrame({'A': [0, 0, 1], 'B': [1, 2, 3]})
    grouped = df.groupby('A')
    match = 'Must provide'
    with pytest.raises(TypeError, match=match):
        grouped.agg(foo=1)
    with pytest.raises(TypeError, match=match):
        grouped.agg()
    with pytest.raises(TypeError, match=match):
        grouped.agg(a=('B', 'max'), b=(1, 2, 3))