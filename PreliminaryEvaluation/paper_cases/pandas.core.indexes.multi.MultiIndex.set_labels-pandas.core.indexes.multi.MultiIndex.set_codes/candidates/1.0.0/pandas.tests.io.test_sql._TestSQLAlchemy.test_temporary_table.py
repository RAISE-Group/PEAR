def test_temporary_table(self):
    test_data = 'Hello, World!'
    expected = DataFrame({'spam': [test_data]})
    Base = declarative.declarative_base()

    class Temporary(Base):
        __tablename__ = 'temp_test'
        __table_args__ = {'prefixes': ['TEMPORARY']}
        id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
        spam = sqlalchemy.Column(sqlalchemy.Unicode(30), nullable=False)
    Session = sa_session.sessionmaker(bind=self.conn)
    session = Session()
    with session.transaction:
        conn = session.connection()
        Temporary.__table__.create(conn)
        session.add(Temporary(spam=test_data))
        session.flush()
        df = sql.read_sql_query(sql=sqlalchemy.select([Temporary.spam]), con=conn)
    tm.assert_frame_equal(df, expected)