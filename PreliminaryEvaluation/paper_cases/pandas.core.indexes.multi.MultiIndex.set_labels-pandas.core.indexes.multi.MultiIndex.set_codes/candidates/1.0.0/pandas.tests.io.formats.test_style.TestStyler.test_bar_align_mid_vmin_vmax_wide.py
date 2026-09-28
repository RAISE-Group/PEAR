def test_bar_align_mid_vmin_vmax_wide(self):
    df = pd.DataFrame({'A': [0, 1], 'B': [-2, 4]})
    result = df.style.bar(align='mid', axis=None, vmin=-3, vmax=7)._compute().ctx
    expected = {(0, 0): ['width: 10em', ' height: 80%'], (1, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 30.0%, #d65f5f 30.0%, #d65f5f 40.0%, transparent 40.0%)'], (0, 1): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 10.0%, #d65f5f 10.0%, #d65f5f 30.0%, transparent 30.0%)'], (1, 1): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg, transparent 30.0%, #d65f5f 30.0%, #d65f5f 70.0%, transparent 70.0%)']}
    assert result == expected