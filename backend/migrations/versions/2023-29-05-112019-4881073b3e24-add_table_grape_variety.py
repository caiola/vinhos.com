"""Add table grape variety

Revision ID: 4881073b3e24
Revises: f76c9e44ee48
Create Date: 2023-05-29 11:20:19.845568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4881073b3e24"
down_revision = "f76c9e44ee48"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "grape_variety",
        sa.Column(
            "id", sa.BigInteger(), nullable=False, comment="Primary key"
        ),
        sa.Column(
            "grape_variety",
            sa.String(length=50),
            nullable=True,
            comment="Grape variety",
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_general_ci",
        mysql_engine="InnoDB",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("grape_variety")
    # ### end Alembic commands ###