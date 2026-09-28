def test_bar_align_mid_vmin_vmax_clipping(self):
    df = pd.DataFrame({'A': [0, 1], 'B': [-2, 4]})
    result = df.style.bar(align='mid', axis=None, vmin=-1, vmax=3)._compute().ctx
    expected = {(0, 0): ['width: 10em', ' height: 80%'], (1, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 25.0%, #d65f5f 25.0%, #d65f5f 50.0%, transparent 50.0%)'], (0, 1): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,#d65f5f 25.0%, transparent 25.0%)'], (1, 1): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 25.0%, #d65f5f 25.0%, #d65f5f 100.0%, transparent 100.0%)']}
    assert result == expected