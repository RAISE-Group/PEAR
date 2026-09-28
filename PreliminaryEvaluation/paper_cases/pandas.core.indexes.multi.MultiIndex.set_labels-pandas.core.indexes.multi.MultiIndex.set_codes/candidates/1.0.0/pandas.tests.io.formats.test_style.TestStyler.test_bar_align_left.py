def test_bar_align_left(self):
    df = pd.DataFrame({'A': [0, 1, 2]})
    result = df.style.bar()._compute().ctx
    expected = {(0, 0): ['width: 10em', ' height: 80%'], (1, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,#d65f5f 50.0%, transparent 50.0%)'], (2, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,#d65f5f 100.0%, transparent 100.0%)']}
    assert result == expected
    result = df.style.bar(color='red', width=50)._compute().ctx
    expected = {(0, 0): ['width: 10em', ' height: 80%'], (1, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,red 25.0%, transparent 25.0%)'], (2, 0): ['width: 10em', ' height: 80%', 'background: linear-gradient(90deg,red 50.0%, transparent 50.0%)']}
    assert result == expected
    df['C'] = ['a'] * len(df)
    result = df.style.bar(color='red', width=50)._compute().ctx
    assert result == expected
    df['C'] = df['C'].astype('category')
    result = df.style.bar(color='red', width=50)._compute().ctx
    assert result == expected