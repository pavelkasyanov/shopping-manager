"""add users table

Revision ID: e952aca6d194
Revises:
Create Date: 2021-06-26 20:18:26.989498

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "e952aca6d194"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column(
            "user_id",
            sa.BigInteger(),
            server_default=sa.text("nextval('\"user base_id_seq\"'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("email", sa.VARCHAR(), nullable=False),
        sa.Column("nickname", sa.VARCHAR(), nullable=False),
        sa.Column("password", sa.VARCHAR(), nullable=False),
        sa.Column("is_banned", sa.BOOLEAN(), nullable=True),
        sa.Column("is_superuser", sa.BOOLEAN(), nullable=True),
        sa.Column(
            "created_date",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("user_id"),
    )


def downgrade():
    op.drop_table("users")
