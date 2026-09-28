@pytest.mark.parametrize('string', [0, 3.14, ('a', 'b'), None])
def test_construction_from_string_errors(self, string):
    msg = 'a string needs to be passed, got type'
    with pytest.raises(TypeError, match=msg):
        IntervalDtype.construct_from_string(string)