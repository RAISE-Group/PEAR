def test_from_codes_neither(self):
    msg = 'Both were None'
    with pytest.raises(ValueError, match=msg):
        Categorical.from_codes([0, 1])