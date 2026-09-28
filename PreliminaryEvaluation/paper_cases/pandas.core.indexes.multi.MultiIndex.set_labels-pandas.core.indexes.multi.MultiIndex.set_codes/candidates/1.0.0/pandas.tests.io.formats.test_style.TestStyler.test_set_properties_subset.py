def test_set_properties_subset(self):
    df = pd.DataFrame({'A': [0, 1]})
    result = df.style.set_properties(subset=pd.IndexSlice[0, 'A'], color='white')._compute().ctx
    expected = {(0, 0): ['color: white']}
    assert result == expected