@pytest.mark.parametrize('enc', ['UTF-8', 'utf-8', 'utf8'])
def test_round_trip_valid_encodings(self, enc, df):
    self.check_round_trip_frame(df, encoding=enc)