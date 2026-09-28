def test_column_contains_raises(self, float_frame):
    with pytest.raises(TypeError, match="unhashable type: 'Index'"):
        float_frame.columns in float_frame