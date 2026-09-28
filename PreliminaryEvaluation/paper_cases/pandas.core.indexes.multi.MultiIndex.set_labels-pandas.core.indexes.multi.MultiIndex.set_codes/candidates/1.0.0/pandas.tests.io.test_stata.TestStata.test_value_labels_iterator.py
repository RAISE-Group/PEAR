@pytest.mark.parametrize('write_index', [True, False])
def test_value_labels_iterator(self, write_index):
    d = {'A': ['B', 'E', 'C', 'A', 'E']}
    df = pd.DataFrame(data=d)
    df['A'] = df['A'].astype('category')
    with tm.ensure_clean() as path:
        df.to_stata(path, write_index=write_index)
        with pd.read_stata(path, iterator=True) as dta_iter:
            value_labels = dta_iter.value_labels()
    assert value_labels == {'A': {0: 'A', 1: 'B', 2: 'C', 3: 'E'}}