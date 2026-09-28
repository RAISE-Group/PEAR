def test_display_format(self):
    df = pd.DataFrame(np.random.random(size=(2, 2)))
    ctx = df.style.format('{:0.1f}')._translate()
    assert all((['display_value' in c for c in row] for row in ctx['body']))
    assert all(([len(c['display_value']) <= 3 for c in row[1:]] for row in ctx['body']))
    assert len(ctx['body'][0][1]['display_value'].lstrip('-')) <= 3