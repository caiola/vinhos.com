"""Add table verification

Revision ID: 3a8c3ff24c8f
Revises: fc740c082996
Create Date: 2023-06-19 21:38:53.140719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3a8c3ff24c8f"
down_revision = "fc740c082996"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("account", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "user_id",
                sa.BigInteger(),
                nullable=True,
                comment="Administrator user of the account",
            )
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("account", schema=None) as batch_op:
        batch_op.drop_column("user_id")

    # ### end Alembic commands ###
