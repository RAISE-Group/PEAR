@td.skip_if_no_mpl
def test_background_gradient_axis(self):
    df = pd.DataFrame([[1, 2], [2, 4]], columns=['A', 'B'])
    low = ['background-color: #f7fbff', 'color: #000000']
    high = ['background-color: #08306b', 'color: #f1f1f1']
    mid = ['background-color: #abd0e6', 'color: #000000']
    result = df.style.background_gradient(cmap='Blues', axis=0)._compute().ctx
    assert result[0, 0] == low
    assert result[0, 1] == low
    assert result[1, 0] == high
    assert result[1, 1] == high
    result = df.style.background_gradient(cmap='Blues', axis=1)._compute().ctx
    assert result[0, 0] == low
    assert result[0, 1] == high
    assert result[1, 0] == low
    assert result[1, 1] == high
    result = df.style.background_gradient(cmap='Blues', axis=None)._compute().ctx
    assert result[0, 0] == low
    assert result[0, 1] == mid
    assert result[1, 0] == mid
    assert result[1, 1] == high