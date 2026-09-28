def _make_iris_table_metadata(self):
    sa = sqlalchemy
    metadata = sa.MetaData()
    iris = sa.Table('iris', metadata, sa.Column('SepalLength', sa.REAL), sa.Column('SepalWidth', sa.REAL), sa.Column('PetalLength', sa.REAL), sa.Column('PetalWidth', sa.REAL), sa.Column('Name', sa.TEXT))
    return iris