def test_query_by_select_obj(self):
    iris = self._make_iris_table_metadata()
    name_select = sqlalchemy.select([iris]).where(iris.c.Name == sqlalchemy.bindparam('name'))
    iris_df = sql.read_sql(name_select, self.conn, params={'name': 'Iris-setosa'})
    all_names = set(iris_df['Name'])
    assert all_names == {'Iris-setosa'}