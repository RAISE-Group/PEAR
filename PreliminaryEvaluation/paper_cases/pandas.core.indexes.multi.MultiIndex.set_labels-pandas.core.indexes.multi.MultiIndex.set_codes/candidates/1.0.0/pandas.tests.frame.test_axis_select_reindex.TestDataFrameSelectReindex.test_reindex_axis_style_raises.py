def test_reindex_axis_style_raises(self):
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    with pytest.raises(TypeError, match="Cannot specify both 'axis'"):
        df.reindex([0, 1], ['A'], axis=1)
    with pytest.raises(TypeError, match="Cannot specify both 'axis'"):
        df.reindex([0, 1], ['A'], axis='index')
    with pytest.raises(TypeError, match="Cannot specify both 'axis'"):
        df.reindex(index=[0, 1], axis='index')
    with pytest.raises(TypeError, match="Cannot specify both 'axis'"):
        df.reindex(index=[0, 1], axis='columns')
    with pytest.raises(TypeError, match="Cannot specify both 'axis'"):
        df.reindex(columns=[0, 1], axis='columns')
    with pytest.raises(TypeError, match="Cannot specify both 'axis'"):
        df.reindex(index=[0, 1], columns=[0, 1], axis='columns')
    with pytest.raises(TypeError, match='Cannot specify all'):
        df.reindex([0, 1], [0], ['A'])
    with pytest.raises(TypeError, match="Cannot specify both 'axis'"):
        df.reindex(index=[0, 1], axis='index')
    with pytest.raises(TypeError, match="Cannot specify both 'axis'"):
        df.reindex(index=[0, 1], axis='columns')
    with pytest.raises(TypeError, match='multiple values'):
        df.reindex([0, 1], labels=[0, 1])