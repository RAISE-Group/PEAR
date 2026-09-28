def test_bytes_io(self, engine):
    bio = BytesIO()
    df = DataFrame(np.random.randn(10, 2))
    writer = ExcelWriter(bio, engine=engine)
    df.to_excel(writer)
    writer.save()
    bio.seek(0)
    reread_df = pd.read_excel(bio, index_col=0)
    tm.assert_frame_equal(df, reread_df)