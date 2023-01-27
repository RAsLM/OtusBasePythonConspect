"""Added new table Tags

Revision ID: 2099cb57217e
Revises: b2870ee7b012
Create Date: 2023-01-10 05:48:29.330868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2099cb57217e'
down_revision = 'b2870ee7b012'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_app__tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_app__tags')
    # ### end Alembic commands ###