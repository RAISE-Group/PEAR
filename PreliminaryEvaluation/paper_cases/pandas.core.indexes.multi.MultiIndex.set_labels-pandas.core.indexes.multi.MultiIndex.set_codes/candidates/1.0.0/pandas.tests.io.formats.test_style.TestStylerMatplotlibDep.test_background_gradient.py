def test_background_gradient(self):
    df = pd.DataFrame([[1, 2], [2, 4]], columns=['A', 'B'])
    for c_map in [None, 'YlOrRd']:
        result = df.style.background_gradient(cmap=c_map)._compute().ctx
        assert all(('#' in x[0] for x in result.values()))
        assert result[0, 0] == result[0, 1]
        assert result[1, 0] == result[1, 1]
    result = df.style.background_gradient(subset=pd.IndexSlice[1, 'A'])._compute().ctx
    assert result[1, 0] == ['background-color: #fff7fb', 'color: #000000']