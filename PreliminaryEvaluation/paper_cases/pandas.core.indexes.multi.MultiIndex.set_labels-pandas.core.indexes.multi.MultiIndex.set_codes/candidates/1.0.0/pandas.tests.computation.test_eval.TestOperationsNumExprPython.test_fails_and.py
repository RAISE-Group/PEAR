def test_fails_and(self):
    df = DataFrame(np.random.randn(5, 3))
    msg = "'BoolOp' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval('df > 2 and df > 3', local_dict={'df': df}, parser=self.parser, engine=self.engine)