def test_can_hold_identifiers(self):
    idx = self.create_index()
    key = idx[0]
    assert idx._can_hold_identifiers_and_holds_name(key) is False