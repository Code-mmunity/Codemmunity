"""empty message

Revision ID: a013c95f6e1e
Revises: b5c0951794f7
Create Date: 2023-11-18 08:55:25.984064

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'a013c95f6e1e'
down_revision = 'b5c0951794f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('ip',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.create_unique_constraint(None, ['ip'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('ip',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)

    # ### end Alembic commands ###
