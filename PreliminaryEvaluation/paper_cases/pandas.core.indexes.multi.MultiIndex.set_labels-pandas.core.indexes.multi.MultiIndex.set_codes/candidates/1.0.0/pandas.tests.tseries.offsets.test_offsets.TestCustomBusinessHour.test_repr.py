def test_repr(self):
    assert repr(self.offset1) == '<CustomBusinessHour: CBH=09:00-17:00>'
    assert repr(self.offset2) == '<CustomBusinessHour: CBH=09:00-17:00>'