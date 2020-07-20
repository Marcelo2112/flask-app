"""empty message

Revision ID: 80356f425bb2
Revises: 84c66b222208
Create Date: 2020-07-14 18:37:09.554913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80356f425bb2'
down_revision = '84c66b222208'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('direccion', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'direccion')
    # ### end Alembic commands ###
