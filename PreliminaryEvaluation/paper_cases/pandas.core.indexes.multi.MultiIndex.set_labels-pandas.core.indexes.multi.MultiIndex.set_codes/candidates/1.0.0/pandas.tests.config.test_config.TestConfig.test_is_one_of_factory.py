def test_is_one_of_factory(self):
    v = self.cf.is_one_of_factory([None, 12])
    v(12)
    v(None)
    msg = 'Value must be one of None\\|12'
    with pytest.raises(ValueError, match=msg):
        v(1.1)