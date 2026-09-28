def test_encode_recursion_max(self):

    class O2:
        member = 0
        pass

    class O1:
        member = 0
        pass
    decoded_input = O1()
    decoded_input.member = O2()
    decoded_input.member.member = decoded_input
    with pytest.raises(OverflowError):
        ujson.encode(decoded_input)