@pytest.mark.slow
def test_banklist_header(self, datapath):
    from pandas.io.html import _remove_whitespace

    def try_remove_ws(x):
        try:
            return _remove_whitespace(x)
        except AttributeError:
            return x
    df = self.read_html(self.banklist_data, 'Metcalf', attrs={'id': 'table'})[0]
    ground_truth = read_csv(datapath('io', 'data', 'csv', 'banklist.csv'), converters={'Updated Date': Timestamp, 'Closing Date': Timestamp})
    assert df.shape == ground_truth.shape
    old = ['First Vietnamese American BankIn Vietnamese', 'Westernbank Puerto RicoEn Espanol', 'R-G Premier Bank of Puerto RicoEn Espanol', 'EurobankEn Espanol', 'Sanderson State BankEn Espanol', 'Washington Mutual Bank(Including its subsidiary Washington Mutual Bank FSB)', 'Silver State BankEn Espanol', 'AmTrade International BankEn Espanol', 'Hamilton Bank, NAEn Espanol', 'The Citizens Savings BankPioneer Community Bank, Inc.']
    new = ['First Vietnamese American Bank', 'Westernbank Puerto Rico', 'R-G Premier Bank of Puerto Rico', 'Eurobank', 'Sanderson State Bank', 'Washington Mutual Bank', 'Silver State Bank', 'AmTrade International Bank', 'Hamilton Bank, NA', 'The Citizens Savings Bank']
    dfnew = df.applymap(try_remove_ws).replace(old, new)
    gtnew = ground_truth.applymap(try_remove_ws)
    converted = dfnew._convert(datetime=True, numeric=True)
    date_cols = ['Closing Date', 'Updated Date']
    converted[date_cols] = converted[date_cols]._convert(datetime=True, coerce=True)
    tm.assert_frame_equal(converted, gtnew)