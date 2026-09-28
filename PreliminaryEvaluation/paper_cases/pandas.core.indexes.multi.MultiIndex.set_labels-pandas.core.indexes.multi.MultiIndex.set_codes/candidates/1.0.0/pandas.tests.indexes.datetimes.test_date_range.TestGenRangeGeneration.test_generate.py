def test_generate(self):
    rng1 = list(generate_range(START, END, offset=BDay()))
    rng2 = list(generate_range(START, END, offset='B'))
    assert rng1 == rng2