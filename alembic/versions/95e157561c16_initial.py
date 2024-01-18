"""initial

Revision ID: 95e157561c16
Revises: 
Create Date: 2024-01-12 15:20:13.624082

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95e157561c16'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dnm',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('dnmh_id', sa.Integer(), nullable=True),
    sa.Column('marker_id', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dnm_id'), 'dnm', ['id'], unique=False)
    op.create_table('markers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_markers_id'), 'markers', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_markers_id'), table_name='markers')
    op.drop_table('markers')
    op.drop_index(op.f('ix_dnm_id'), table_name='dnm')
    op.drop_table('dnm')
    # ### end Alembic commands ###
