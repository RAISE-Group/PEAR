def test_bar_align_mid_vmin(self):
    df = pd.DataFrame({'A': [0, 1], 'B': [-2, 4]})
    result = df.style.bar(align='mid', axis=None, vmin=-6)._compute().ctx
    expected = {(0, 0): ['width: 10em', ' height: 80%'], (1, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 60.0%, #d65f5f 60.0%, #d65f5f 70.0%, transparent 70.0%)'], (0, 1): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 40.0%, #d65f5f 40.0%, #d65f5f 60.0%, transparent 60.0%)'], (1, 1): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 60.0%, #d65f5f 60.0%, #d65f5f 100.0%, transparent 100.0%)']}
    assert result == expected