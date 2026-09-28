def test_repr_mixed(self, float_string_frame):
    buf = StringIO()
    repr(float_string_frame)
    float_string_frame.info(verbose=False, buf=buf)