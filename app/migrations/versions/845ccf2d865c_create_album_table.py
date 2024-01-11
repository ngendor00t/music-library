"""create album table

Revision ID: 845ccf2d865c
Revises: 7f94f1d704ed
Create Date: 2024-01-10 14:57:13.054984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '845ccf2d865c'
down_revision = '7f94f1d704ed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('number_of_songs', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('albums')
    # ### end Alembic commands ###
