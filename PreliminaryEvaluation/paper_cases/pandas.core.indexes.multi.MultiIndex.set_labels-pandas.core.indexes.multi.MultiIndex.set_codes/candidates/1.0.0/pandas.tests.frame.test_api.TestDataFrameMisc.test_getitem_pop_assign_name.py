def test_getitem_pop_assign_name(self, float_frame):
    s = float_frame['A']
    assert s.name == 'A'
    s = float_frame.pop('A')
    assert s.name == 'A'
    s = float_frame.loc[:, 'B']
    assert s.name == 'B'
    s2 = s.loc[:]
    assert s2.name == 'B'