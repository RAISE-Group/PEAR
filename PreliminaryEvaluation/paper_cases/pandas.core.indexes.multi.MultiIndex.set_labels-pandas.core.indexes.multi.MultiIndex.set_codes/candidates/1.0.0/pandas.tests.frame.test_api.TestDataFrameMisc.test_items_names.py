def test_items_names(self, float_string_frame):
    for k, v in float_string_frame.items():
        assert v.name == k