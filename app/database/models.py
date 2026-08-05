from datetime import datetime
from uuid import UUID, uuid4

from httpx import post
from sqlalchemy import Column
from sqlmodel import Field, SQLModel
from sqlalchemy.dialects import postgresql


class Apis(SQLModel, table=True):
    __tablename__ = "apis"
    id: UUID = Field(
        sa_column=Column(
            postgresql.UUID,
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


class Urls(SQLModel, table=True):
    __tablename__ = "urls"
    url: str = Field(
        primary_key=True
    )
    api_id: UUID = Field(
        foreign_key="apis.id",
    )
    created_at: datetime = Field(
        sa_column=Column(
            postgresql.TIMESTAMP,
            default=datetime.now
        )
    )


class Monitors(SQLModel, table=True):
    __tablename__ = "monitors"
    id: UUID = Field(
        sa_column=Column(
            postgresql.UUID,
            default=uuid4,
            primary_key=True
        )
    )
    url_id: str = Field(
        foreign_key="urls.url"
    )
    interval: float
    is_active: bool
    created_at: datetime = Field(
        sa_column=Column(
            postgresql.TIMESTAMP,
            default=datetime.now
        )
    )
    last_pinged_at: datetime = Field(
        sa_column=Column(
            postgresql.TIMESTAMP,
            default=datetime.now
        )
    )


class Pings(SQLModel, table=True):
    __tablename__ = "pings"
    id: UUID = Field(
        sa_column=Column(
            postgresql.UUID,
            default=uuid4,
            primary_key=True
        )
    )
    monitor_id: UUID = Field(
        foreign_key="monitors.id"
    )
    status_code: int
    response_time: float
    is_up: bool
    created_at: datetime = Field(
        sa_column=Column(
            postgresql.TIMESTAMP,
            default=datetime.now
        )
    )
