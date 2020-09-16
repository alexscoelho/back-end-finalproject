"""empty message

Revision ID: 96006b827e5f
Revises: 5ac2cba24eb2
Create Date: 2020-09-12 18:26:19.651664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96006b827e5f'
down_revision = '5ac2cba24eb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('instrument', sa.String(length=120), nullable=False),
    sa.Column('type_file', sa.String(length=120), nullable=False),
    sa.Column('level', sa.String(length=120), nullable=False),
    sa.Column('language', sa.String(length=120), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('files')
    # ### end Alembic commands ###
