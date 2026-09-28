def test_simple_in_ops(self):
    if self.parser != 'python':
        res = pd.eval('1 in [1, 2]', engine=self.engine, parser=self.parser)
        assert res
        res = pd.eval('2 in (1, 2)', engine=self.engine, parser=self.parser)
        assert res
        res = pd.eval('3 in (1, 2)', engine=self.engine, parser=self.parser)
        assert not res
        res = pd.eval('3 not in (1, 2)', engine=self.engine, parser=self.parser)
        assert res
        res = pd.eval('[3] not in (1, 2)', engine=self.engine, parser=self.parser)
        assert res
        res = pd.eval('[3] in ([3], 2)', engine=self.engine, parser=self.parser)
        assert res
        res = pd.eval('[[3]] in [[[3]], 2]', engine=self.engine, parser=self.parser)
        assert res
        res = pd.eval('(3,) in [(3,), 2]', engine=self.engine, parser=self.parser)
        assert res
        res = pd.eval('(3,) not in [(3,), 2]', engine=self.engine, parser=self.parser)
        assert not res
        res = pd.eval('[(3,)] in [[(3,)], 2]', engine=self.engine, parser=self.parser)
        assert res
    else:
        with pytest.raises(NotImplementedError):
            pd.eval('1 in [1, 2]', engine=self.engine, parser=self.parser)
        with pytest.raises(NotImplementedError):
            pd.eval('2 in (1, 2)', engine=self.engine, parser=self.parser)
        with pytest.raises(NotImplementedError):
            pd.eval('3 in (1, 2)', engine=self.engine, parser=self.parser)
        with pytest.raises(NotImplementedError):
            pd.eval('3 not in (1, 2)', engine=self.engine, parser=self.parser)
        with pytest.raises(NotImplementedError):
            pd.eval('[(3,)] in (1, 2, [(3,)])', engine=self.engine, parser=self.parser)
        with pytest.raises(NotImplementedError):
            pd.eval('[3] not in (1, 2, [[3]])', engine=self.engine, parser=self.parser)