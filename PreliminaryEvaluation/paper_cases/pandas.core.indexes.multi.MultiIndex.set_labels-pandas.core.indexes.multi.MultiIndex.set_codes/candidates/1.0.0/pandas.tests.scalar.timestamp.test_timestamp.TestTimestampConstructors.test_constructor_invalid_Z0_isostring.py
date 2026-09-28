@pytest.mark.parametrize('z', ['Z0', 'Z00'])
def test_constructor_invalid_Z0_isostring(self, z):
    with pytest.raises(ValueError):
        Timestamp('2014-11-02 01:00{}'.format(z))