def test_fillna_empty(self):
    df = DataFrame(columns=['x'])
    for m in ['pad', 'backfill']:
        df.x.fillna(method=m, inplace=True)
        df.x.fillna(method=m)