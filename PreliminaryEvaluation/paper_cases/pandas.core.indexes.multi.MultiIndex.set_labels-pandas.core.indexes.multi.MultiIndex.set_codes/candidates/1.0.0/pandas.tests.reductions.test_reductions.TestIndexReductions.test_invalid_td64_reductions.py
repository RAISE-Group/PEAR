@pytest.mark.parametrize('opname', ['skew', 'kurt', 'sem', 'prod', 'var'])
def test_invalid_td64_reductions(self, opname):
    s = Series([Timestamp('20130101') + timedelta(seconds=i * i) for i in range(10)])
    td = s.diff()
    msg = "reduction operation '{op}' not allowed for this dtype"
    msg = msg.format(op=opname)
    with pytest.raises(TypeError, match=msg):
        getattr(td, opname)()
    with pytest.raises(TypeError, match=msg):
        getattr(td.to_frame(), opname)(numeric_only=False)