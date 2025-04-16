"""Remove id field from Game model

Revision ID: 5b5621828be0
Revises: acc663edf845
Create Date: 2025-04-16 18:13:17.230249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b5621828be0'
down_revision: Union[str, None] = 'acc663edf845'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
