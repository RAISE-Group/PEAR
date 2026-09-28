def test_bar_align_mid_vmax(self):
    df = pd.DataFrame({'A': [0, 1], 'B': [-2, 4]})
    result = df.style.bar(align='mid', axis=None, vmax=8)._compute().ctx
    expected = {(0, 0): ['width: 10em', ' height: 80%'], (1, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 20.0%, #d65f5f 20.0%, #d65f5f 30.0%, transparent 30.0%)'], (0, 1): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,#d65f5f 20.0%, transparent 20.0%)'], (1, 1): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 20.0%, #d65f5f 20.0%, #d65f5f 60.0%, transparent 60.0%)']}
    assert result == expected