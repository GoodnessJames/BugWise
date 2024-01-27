"""Add audio_data to Post model

Revision ID: 1f31cfb21e47
Revises: 
Create Date: 2024-01-24 15:05:31.059984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f31cfb21e47'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('audio_data', sa.String(length=255), nullable=True))
        batch_op.drop_column('audio_file')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('audio_file', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_column('audio_data')

    # ### end Alembic commands ###
