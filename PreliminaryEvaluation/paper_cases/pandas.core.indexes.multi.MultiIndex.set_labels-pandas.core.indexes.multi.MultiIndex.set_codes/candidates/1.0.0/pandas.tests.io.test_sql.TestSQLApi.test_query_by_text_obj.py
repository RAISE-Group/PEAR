def test_query_by_text_obj(self):
    name_text = sqlalchemy.text('select * from iris where name=:name')
    iris_df = sql.read_sql(name_text, self.conn, params={'name': 'Iris-versicolor'})
    all_names = set(iris_df['Name'])
    assert all_names == {'Iris-versicolor'}