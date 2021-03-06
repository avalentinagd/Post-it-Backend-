"""empty message

Revision ID: aefe61a9bbe0
Revises: 
Create Date: 2020-09-10 13:40:33.560046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aefe61a9bbe0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('social',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('social_name', sa.Enum('instagram', 'facebook', 'twitter', 'google'), nullable=False),
    sa.Column('photo', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('id_social', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id_social'], ['social.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('multimedia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('multimedia_type', sa.Enum('img', 'video'), nullable=False),
    sa.Column('multimedia_url', sa.Text(), nullable=False),
    sa.Column('id_post', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id_post'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('multimedia')
    op.drop_table('post')
    op.drop_table('social')
    op.drop_table('user')
    # ### end Alembic commands ###
