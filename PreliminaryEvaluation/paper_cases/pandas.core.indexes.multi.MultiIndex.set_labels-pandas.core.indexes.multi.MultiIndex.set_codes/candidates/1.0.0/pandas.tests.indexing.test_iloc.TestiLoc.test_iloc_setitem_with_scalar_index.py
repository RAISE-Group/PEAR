@pytest.mark.parametrize('indexer', [[0], slice(None, 1, None), np.array([0])])
@pytest.mark.parametrize('value', [['Z'], np.array(['Z'])])
def test_iloc_setitem_with_scalar_index(self, indexer, value):
    df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
    df.iloc[0, indexer] = value
    result = df.iloc[0, 0]
    assert is_scalar(result) and result == 'Z'