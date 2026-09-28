def test_too_long(self):
    with pd.option_context('display.precision', 4):
        df = pd.DataFrame(dict(x=[12345.6789]))
        assert str(df) == '            x\n0  12345.6789'
        df = pd.DataFrame(dict(x=[2000000.0]))
        assert str(df) == '           x\n0  2000000.0'
        df = pd.DataFrame(dict(x=[12345.6789, 2000000.0]))
        assert str(df) == '            x\n0  1.2346e+04\n1  2.0000e+06'