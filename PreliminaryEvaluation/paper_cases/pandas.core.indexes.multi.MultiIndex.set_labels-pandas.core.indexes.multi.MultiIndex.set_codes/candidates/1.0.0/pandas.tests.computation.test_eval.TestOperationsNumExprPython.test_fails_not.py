def test_fails_not(self):
    df = DataFrame(np.random.randn(5, 3))
    msg = "'Not' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval('not df > 2', local_dict={'df': df}, parser=self.parser, engine=self.engine)