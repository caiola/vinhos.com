"""empty message

Revision ID: 6ecca4fcf65f
Revises: 51e2c29ad95
Create Date: 2023-01-15 13:19:39.252497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6ecca4fcf65f"
down_revision = "51e2c29ad95"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "ads",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("uuid", sa.String(length=32), nullable=True),
        sa.Column("title", sa.String(length=100), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("ads")
    # ### end Alembic commands ###
