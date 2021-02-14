"""Add new table for emotes.

Revision ID: 061e179dc139
Revises: ff462a1bd816
Create Date: 2021-02-14 19:17:28.815261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '061e179dc139'
down_revision = 'ff462a1bd816'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emotes',
    sa.Column('alias', sa.String(length=64), nullable=False),
    sa.Column('uri', sa.String(length=512), nullable=False),
    sa.UniqueConstraint('alias')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emotes')
    # ### end Alembic commands ###
