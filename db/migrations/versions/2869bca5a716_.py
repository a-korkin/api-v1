"""empty message

Revision ID: 2869bca5a716
Revises: 
Create Date: 2021-11-05 10:45:42.709145

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2869bca5a716'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cd_entities',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False, comment='идентификатор'),
    sa.PrimaryKeyConstraint('id'),
    schema='common',
    comment='сущности'
    )
    op.create_table('cd_persons',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False, comment='идентификатор'),
    sa.Column('c_last_name', sa.String(length=500), nullable=False, comment='фамилия'),
    sa.Column('c_first_name', sa.String(length=500), nullable=False, comment='имя'),
    sa.ForeignKeyConstraint(['id'], ['common.cd_entities.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='common',
    comment='физлица'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cd_persons', schema='common')
    op.drop_table('cd_entities', schema='common')
    # ### end Alembic commands ###
