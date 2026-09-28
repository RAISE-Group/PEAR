def test_drop_by_numeric_label_raises_missing_keys(self):
    index = Index([1, 2, 3])
    with pytest.raises(KeyError, match=''):
        index.drop([3, 4])