def test_rename_errors_raises(self):
    df = DataFrame(columns=['A', 'B', 'C', 'D'])
    with pytest.raises(KeyError, match="'E'] not found in axis"):
        df.rename(columns={'A': 'a', 'E': 'e'}, errors='raise')