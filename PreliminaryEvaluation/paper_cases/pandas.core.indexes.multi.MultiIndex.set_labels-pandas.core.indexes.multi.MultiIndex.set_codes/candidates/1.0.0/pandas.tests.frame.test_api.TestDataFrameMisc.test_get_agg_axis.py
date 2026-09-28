def test_get_agg_axis(self, float_frame):
    cols = float_frame._get_agg_axis(0)
    assert cols is float_frame.columns
    idx = float_frame._get_agg_axis(1)
    assert idx is float_frame.index
    msg = 'Axis must be 0 or 1 \\(got 2\\)'
    with pytest.raises(ValueError, match=msg):
        float_frame._get_agg_axis(2)