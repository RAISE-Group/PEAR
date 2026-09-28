@pytest.mark.parametrize('name', [None, 'new_name'])
def test_to_frame(self, name):
    idx = self.create_index()
    if name:
        idx_name = name
    else:
        idx_name = idx.name or 0
    df = idx.to_frame(name=idx_name)
    assert df.index is idx
    assert len(df.columns) == 1
    assert df.columns[0] == idx_name
    assert df[idx_name].values is not idx.values
    df = idx.to_frame(index=False, name=idx_name)
    assert df.index is not idx