def test_alias_equality(self):
    for k, v in _offset_map.items():
        if v is None:
            continue
        assert k == v.copy()