def test_repr_obeys_max_seq_limit(self):
    with option_context('display.max_seq_items', 2000):
        assert len(printing.pprint_thing(list(range(1000)))) > 1000
    with option_context('display.max_seq_items', 5):
        assert len(printing.pprint_thing(list(range(1000)))) < 100