"""empty message

Revision ID: 995d7400adfa
Revises: 1af91f03bdae
Create Date: 2020-10-10 14:47:52.739655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '995d7400adfa'
down_revision = '1af91f03bdae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('profile_picture', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'profile_picture')
    # ### end Alembic commands ###
