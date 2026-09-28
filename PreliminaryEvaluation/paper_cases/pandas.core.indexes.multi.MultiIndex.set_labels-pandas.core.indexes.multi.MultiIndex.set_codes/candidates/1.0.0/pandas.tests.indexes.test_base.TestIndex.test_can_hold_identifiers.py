def test_can_hold_identifiers(self):
    index = self.create_index()
    key = index[0]
    assert index._can_hold_identifiers_and_holds_name(key) is True