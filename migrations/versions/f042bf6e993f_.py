from alembic import op
import sqlalchemy as sa


revision = 'f042bf6e993f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('goal', sa.String(length=15), nullable=False),
    sa.Column('time', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('about', sa.Text(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('picture', sa.String(length=80), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('_goals', sa.String(), nullable=False),
    sa.Column('_free', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('picture')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('day', sa.String(length=15), nullable=False),
    sa.Column('hour', sa.String(length=15), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('bookings')
    op.drop_table('teachers')
    op.drop_table('requests')
