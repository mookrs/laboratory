"""empty message

Revision ID: f4fb3aa6b327
Revises: 31c23c79d0b6
Create Date: 2016-08-18 23:44:08.168904

"""

# revision identifiers, used by Alembic.
revision = 'f4fb3aa6b327'
down_revision = '31c23c79d0b6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###
