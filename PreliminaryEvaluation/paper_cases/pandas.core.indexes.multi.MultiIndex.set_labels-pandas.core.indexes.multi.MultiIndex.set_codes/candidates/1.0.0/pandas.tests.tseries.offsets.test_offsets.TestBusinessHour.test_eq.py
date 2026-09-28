@pytest.mark.parametrize('offset1,offset2', [(BusinessHour(start='09:00'), BusinessHour()), (BusinessHour(start=['23:00', '13:00'], end=['12:00', '17:00']), BusinessHour(start=['13:00', '23:00'], end=['17:00', '12:00']))])
def test_eq(self, offset1, offset2):
    assert offset1 == offset2