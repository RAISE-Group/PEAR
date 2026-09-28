def test_append_overlap_raises(self, float_frame):
    msg = 'Indexes have overlapping values'
    with pytest.raises(ValueError, match=msg):
        float_frame.append(float_frame, verify_integrity=True)