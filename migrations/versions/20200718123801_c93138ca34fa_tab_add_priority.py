"""tab_add_priority

Revision ID: c93138ca34fa
Revises: f61d6e89f97d
Create Date: 2020-07-18 12:38:01.676833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c93138ca34fa'
down_revision = 'f61d6e89f97d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tabs', sa.Column('priority', sa.Integer(), nullable=False, comment='权重，用来标识展示顺序'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tabs', 'priority')
    # ### end Alembic commands ###
