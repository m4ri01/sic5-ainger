"""change year in book

Revision ID: 7ebdba39f532
Revises: 35964710e4b0
Create Date: 2024-07-15 19:43:27.936275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ebdba39f532'
down_revision = '35964710e4b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.alter_column('year',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=10),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.alter_column('year',
               existing_type=sa.String(length=10),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
