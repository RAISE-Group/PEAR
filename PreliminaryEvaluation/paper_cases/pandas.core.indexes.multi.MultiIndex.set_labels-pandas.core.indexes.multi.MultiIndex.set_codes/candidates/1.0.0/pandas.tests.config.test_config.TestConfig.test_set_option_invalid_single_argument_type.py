def test_set_option_invalid_single_argument_type(self):
    msg = 'Must provide an even number of non-keyword arguments'
    with pytest.raises(ValueError, match=msg):
        self.cf.set_option(2)