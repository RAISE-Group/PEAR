@pytest.mark.parametrize('x,y,lbl', [(['B', 'C'], 'A', 'a'), (['A'], ['B', 'C'], ['b', 'c']), ('A', ['B', 'C'], 'badlabel')])
def test_invalid_xy_args(self, x, y, lbl):
    df = DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
    with pytest.raises(ValueError):
        df.plot(x=x, y=y, label=lbl)