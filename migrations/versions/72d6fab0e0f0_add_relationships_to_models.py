"""Add relationships to models

Revision ID: 72d6fab0e0f0
Revises: 05ea6cb7b086
Create Date: 2024-09-02 11:30:47.544429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72d6fab0e0f0'
down_revision = '05ea6cb7b086'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('ingredients',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.alter_column('ingredients',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
