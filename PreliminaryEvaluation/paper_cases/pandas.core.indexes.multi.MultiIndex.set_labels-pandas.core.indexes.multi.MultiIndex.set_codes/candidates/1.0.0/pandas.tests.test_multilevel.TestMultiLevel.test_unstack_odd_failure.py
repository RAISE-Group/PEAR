def test_unstack_odd_failure(self):
    data = 'day,time,smoker,sum,len\nFri,Dinner,No,8.25,3.\nFri,Dinner,Yes,27.03,9\nFri,Lunch,No,3.0,1\nFri,Lunch,Yes,13.68,6\nSat,Dinner,No,139.63,45\nSat,Dinner,Yes,120.77,42\nSun,Dinner,No,180.57,57\nSun,Dinner,Yes,66.82,19\nThur,Dinner,No,3.0,1\nThur,Lunch,No,117.32,44\nThur,Lunch,Yes,51.51,17'
    df = pd.read_csv(StringIO(data)).set_index(['day', 'time', 'smoker'])
    result = df.unstack(2)
    recons = result.stack()
    tm.assert_frame_equal(recons, df)