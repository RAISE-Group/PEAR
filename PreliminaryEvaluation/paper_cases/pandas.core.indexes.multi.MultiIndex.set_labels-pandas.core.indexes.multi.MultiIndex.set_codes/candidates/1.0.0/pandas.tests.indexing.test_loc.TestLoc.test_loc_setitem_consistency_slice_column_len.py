def test_loc_setitem_consistency_slice_column_len(self):
    data = 'Level_0,,,Respondent,Respondent,Respondent,OtherCat,OtherCat\nLevel_1,,,Something,StartDate,EndDate,Yes/No,SomethingElse\nRegion,Site,RespondentID,,,,,\nRegion_1,Site_1,3987227376,A,5/25/2015 10:59,5/25/2015 11:22,Yes,\nRegion_1,Site_1,3980680971,A,5/21/2015 9:40,5/21/2015 9:52,Yes,Yes\nRegion_1,Site_2,3977723249,A,5/20/2015 8:27,5/20/2015 8:41,Yes,\nRegion_1,Site_2,3977723089,A,5/20/2015 8:33,5/20/2015 9:09,Yes,No'
    df = pd.read_csv(StringIO(data), header=[0, 1], index_col=[0, 1, 2])
    df.loc[:, ('Respondent', 'StartDate')] = pd.to_datetime(df.loc[:, ('Respondent', 'StartDate')])
    df.loc[:, ('Respondent', 'EndDate')] = pd.to_datetime(df.loc[:, ('Respondent', 'EndDate')])
    df.loc[:, ('Respondent', 'Duration')] = df.loc[:, ('Respondent', 'EndDate')] - df.loc[:, ('Respondent', 'StartDate')]
    df.loc[:, ('Respondent', 'Duration')] = df.loc[:, ('Respondent', 'Duration')].astype('timedelta64[s]')
    expected = Series([1380, 720, 840, 2160.0], index=df.index, name=('Respondent', 'Duration'))
    tm.assert_series_equal(df['Respondent', 'Duration'], expected)