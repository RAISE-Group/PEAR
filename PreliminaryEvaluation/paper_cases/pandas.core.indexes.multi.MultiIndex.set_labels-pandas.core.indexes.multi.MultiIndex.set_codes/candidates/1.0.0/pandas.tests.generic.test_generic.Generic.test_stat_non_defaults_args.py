def test_stat_non_defaults_args(self):
    obj = self._construct(5)
    out = np.array([0])
    errmsg = "the 'out' parameter is not supported"
    with pytest.raises(ValueError, match=errmsg):
        obj.max(out=out)
    with pytest.raises(ValueError, match=errmsg):
        obj.var(out=out)
    with pytest.raises(ValueError, match=errmsg):
        obj.sum(out=out)
    with pytest.raises(ValueError, match=errmsg):
        obj.any(out=out)