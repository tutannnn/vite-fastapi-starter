"""create todos table

Revision ID: 9f27c1c59aad
Revises:
Create Date: 2025-09-17 23:54:16.087181

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "9f27c1c59aad"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
