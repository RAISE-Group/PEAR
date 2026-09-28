def test_frame_default_orient(self):
    assert self.frame.to_json() == self.frame.to_json(orient='columns')