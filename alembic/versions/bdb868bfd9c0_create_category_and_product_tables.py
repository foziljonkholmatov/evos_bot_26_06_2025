"""Create category and product tables

Revision ID: bdb868bfd9c0
Revises: abce90031b82
Create Date: 2025-07-13 15:56:06.213904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdb868bfd9c0'
down_revision: Union[str, Sequence[str], None] = 'abce90031b82'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
