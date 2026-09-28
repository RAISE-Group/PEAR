def test_repr_summary(self):
    with cf.option_context('display.max_seq_items', 10):
        result = repr(pd.Index(np.arange(1000)))
        assert len(result) < 200
        assert '...' in result