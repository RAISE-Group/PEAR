@tm.network
@pytest.mark.single
def test_round_trip_exception_(self):
    csv = 'https://raw.github.com/hayd/lahman2012/master/csvs/Teams.csv'
    df = pd.read_csv(csv)
    s = df.to_json()
    result = pd.read_json(s)
    tm.assert_frame_equal(result.reindex(index=df.index, columns=df.columns), df)