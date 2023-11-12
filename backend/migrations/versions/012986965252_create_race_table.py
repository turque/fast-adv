"""create race table

Revision ID: 012986965252
Revises: 1ac276ff7ed1
Create Date: 2023-11-07 21:15:27.610394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '012986965252'
down_revision: Union[str, None] = '1ac276ff7ed1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('races',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('place', sa.String(), nullable=True),
    sa.Column('race_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('distance', sa.Integer(), nullable=True),
    sa.Column('url_race', sa.String(), nullable=True),
    sa.Column('race_description', sa.String(), nullable=True),
    sa.Column('place_description', sa.String(), nullable=True),
    sa.Column('observations', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_races_id'), 'races', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_races_id'), table_name='races')
    op.drop_table('races')
    # ### end Alembic commands ###