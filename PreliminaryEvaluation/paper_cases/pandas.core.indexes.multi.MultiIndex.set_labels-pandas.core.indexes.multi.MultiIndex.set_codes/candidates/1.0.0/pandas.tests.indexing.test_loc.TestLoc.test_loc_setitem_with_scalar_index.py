@pytest.mark.parametrize('indexer', [['A'], slice(None, 'A', None), np.array(['A'])])
@pytest.mark.parametrize('value', [['Z'], np.array(['Z'])])
def test_loc_setitem_with_scalar_index(self, indexer, value):
    df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
    df.loc[0, indexer] = value
    result = df.loc[0, 'A']
    assert is_scalar(result) and result == 'Z'