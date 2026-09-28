def test_set_index_verify_integrity(self, frame_of_index_cols):
    df = frame_of_index_cols
    with pytest.raises(ValueError, match='Index has duplicate keys'):
        df.set_index('A', verify_integrity=True)
    with pytest.raises(ValueError, match='Index has duplicate keys'):
        df.set_index([df['A'], df['A']], verify_integrity=True)