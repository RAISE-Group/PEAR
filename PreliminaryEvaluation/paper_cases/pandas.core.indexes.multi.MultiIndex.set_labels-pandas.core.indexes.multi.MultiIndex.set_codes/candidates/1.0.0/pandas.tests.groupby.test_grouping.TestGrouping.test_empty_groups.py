def test_empty_groups(self, df):
    with pytest.raises(ValueError, match='No group keys passed!'):
        df.groupby([])