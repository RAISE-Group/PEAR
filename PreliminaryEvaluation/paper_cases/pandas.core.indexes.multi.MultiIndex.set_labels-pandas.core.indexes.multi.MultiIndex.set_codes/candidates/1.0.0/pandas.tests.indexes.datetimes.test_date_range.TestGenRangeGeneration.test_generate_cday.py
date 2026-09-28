def test_generate_cday(self):
    rng1 = list(generate_range(START, END, offset=CDay()))
    rng2 = list(generate_range(START, END, offset='C'))
    assert rng1 == rng2