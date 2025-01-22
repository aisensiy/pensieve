"""Add index for entity file_type_group and file_created_at

Revision ID: d10c55fbb7d2
Revises: 31a1ad0e10b3
Create Date: 2025-01-20 23:59:42.021204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd10c55fbb7d2'
down_revision: Union[str, None] = '31a1ad0e10b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index("idx_file_type_group", "entities", ["file_type_group"]) 
    op.create_index("idx_file_created_at", "entities", ["file_created_at"])


def downgrade() -> None:
    op.drop_index("idx_file_type_group", "entities")
    op.drop_index("idx_file_created_at", "entities")

