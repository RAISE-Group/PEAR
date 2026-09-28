@pytest.mark.xfail(reason="astype doesn't recognize data.dtype")
def test_loc_iloc_frame_single_dtype(self, data):
    super().test_loc_iloc_frame_single_dtype(data)