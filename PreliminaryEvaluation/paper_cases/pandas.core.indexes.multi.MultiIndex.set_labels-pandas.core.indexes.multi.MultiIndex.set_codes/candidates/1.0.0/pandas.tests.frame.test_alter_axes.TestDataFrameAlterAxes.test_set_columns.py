def test_set_columns(self, float_string_frame):
    cols = Index(np.arange(len(float_string_frame.columns)))
    float_string_frame.columns = cols
    with pytest.raises(ValueError, match='Length mismatch'):
        float_string_frame.columns = cols[::2]