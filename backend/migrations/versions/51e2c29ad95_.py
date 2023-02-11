""" create the User table

Revision ID: 51e2c29ad95
Revises: 4f2e2c180af
Create Date: 2016-10-02 16:00:01.042947

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "51e2c29ad95"
down_revision = "4f2e2c180af"


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("first_name", sa.String(length=50), nullable=False),
        sa.Column("last_name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("users")
