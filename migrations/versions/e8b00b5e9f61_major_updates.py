"""major updates

Revision ID: e8b00b5e9f61
Revises: b12a51cbcb6e
Create Date: 2022-08-02 13:13:26.506701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8b00b5e9f61'
down_revision = 'b12a51cbcb6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'movie_cast', type_='foreignkey')
    op.drop_column('movie_cast', 'movie_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie_cast', sa.Column('movie_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'movie_cast', 'movies_database', ['movie_id'], ['id'])
    # ### end Alembic commands ###