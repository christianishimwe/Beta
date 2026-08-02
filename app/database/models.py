from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Column
from sqlmodel import Field, SQLModel
from sqlalchemy.dialects import postgresql


class apis(SQLModel, table=True):
    __tablename__ = "users"
    id: UUID = Field(
        sa_column=Column(
            type=postgresql.UUID,
            default=uuid4,
            primary_key=True,
        )
    )
    name: str
    created_at: datetime = Field(
        sa_column=Column(
            postgresql.TIMESTAMP,
            default=datetime.now,
        )
    )
