"""create users

Revision ID: f6af05d78e3e
Revises: 
Create Date: 2022-07-15 00:37:22.598961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6af05d78e3e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('full_name', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
