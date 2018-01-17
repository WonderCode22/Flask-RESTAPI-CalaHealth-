"""empty message

Revision ID: 5f64cda8dcaa
Revises: fcab79245669
Create Date: 2018-01-11 08:51:39.517199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f64cda8dcaa'
down_revision = 'fcab79245669'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'username')
    # ### end Alembic commands ###