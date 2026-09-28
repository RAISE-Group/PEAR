def test_empty_sequence_concat(self):
    empty_pat = '[Nn]o objects'
    none_pat = 'objects.*None'
    test_cases = [((), empty_pat), ([], empty_pat), ({}, empty_pat), ([None], none_pat), ([None, None], none_pat)]
    for df_seq, pattern in test_cases:
        with pytest.raises(ValueError, match=pattern):
            pd.concat(df_seq)
    pd.concat([pd.DataFrame()])
    pd.concat([None, pd.DataFrame()])
    pd.concat([pd.DataFrame(), None])