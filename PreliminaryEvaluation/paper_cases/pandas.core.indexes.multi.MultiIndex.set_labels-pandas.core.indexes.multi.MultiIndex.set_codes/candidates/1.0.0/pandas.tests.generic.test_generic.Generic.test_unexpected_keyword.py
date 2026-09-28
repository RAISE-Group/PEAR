def test_unexpected_keyword(self):
    df = DataFrame(np.random.randn(5, 2), columns=['jim', 'joe'])
    ca = pd.Categorical([0, 0, 2, 2, 3, np.nan])
    ts = df['joe'].copy()
    ts[2] = np.nan
    with pytest.raises(TypeError, match='unexpected keyword'):
        df.drop('joe', axis=1, in_place=True)
    with pytest.raises(TypeError, match='unexpected keyword'):
        df.reindex([1, 0], inplace=True)
    with pytest.raises(TypeError, match='unexpected keyword'):
        ca.fillna(0, inplace=True)
    with pytest.raises(TypeError, match='unexpected keyword'):
        ts.fillna(0, in_place=True)