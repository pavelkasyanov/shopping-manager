"""add models

Revision ID: 5a420687f118
Revises: e952aca6d194
Create Date: 2022-12-23 14:17:13.563760

"""
from uuid import uuid4

import sqlalchemy as sa
from alembic import op
from sqlalchemy import ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "5a420687f118"
down_revision = "e952aca6d194"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "product_types",
        sa.Column(
            "id",
            UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid4,
            server_default=text("gen_random_uuid()"),
        ),
        sa.Column("name", sa.VARCHAR(), nullable=False),
        sa.Column("remark", sa.VARCHAR(), nullable=True),
    )

    op.create_table(
        "product_sub_types",
        sa.Column(
            "id",
            UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid4,
            server_default=text("gen_random_uuid()"),
        ),
        sa.Column("name", sa.VARCHAR(), nullable=False),
        sa.Column("remark", sa.VARCHAR(), nullable=True),
        sa.Column(
            "product_type_id",
            UUID(as_uuid=True),
            ForeignKey("product_types.id"),
            nullable=False,
        ),
    )

    op.create_table(
        "products",
        sa.Column(
            "id",
            UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid4,
            server_default=text("gen_random_uuid()"),
        ),
        sa.Column("name", sa.VARCHAR(), nullable=False),
        sa.Column("remark", sa.VARCHAR(), nullable=True),
        sa.Column("archived", sa.BOOLEAN(), nullable=False, server_default="f"),
        sa.Column(
            "type_id",
            UUID(as_uuid=True),
            ForeignKey("product_types.id"),
            nullable=False,
        ),
        sa.Column(
            "subtype_id",
            UUID(as_uuid=True),
            ForeignKey("product_sub_types.id"),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table("products")
    op.drop_table("product_sub_types")
    op.drop_table("product_types")
