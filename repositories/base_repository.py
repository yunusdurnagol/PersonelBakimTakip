"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/base_repository.py
Açıklama   : Generic Base Repository
Yazar      : Yunus Durnagöl
Sürüm      : 2.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime
from typing import Any
from typing import Generic
from typing import Iterator
from typing import Sequence
from typing import Type
from typing import TypeVar

from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import Base
from repositories.page_request import PageRequest
from repositories.result import PagedResult
from sqlalchemy import Select, select
T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T]):
    """
    Generic Repository

    Tüm repository sınıfları bu sınıftan türetilir.
    """

    def __init__(
        self,
        session: Session,
        model: Type[T],
    ) -> None:

        self.session = session
        self.model = model

    # =====================================================
    # TRANSACTION
    # =====================================================

    @contextmanager
    def transaction(self) -> Iterator[None]:

        try:

            yield

            self.session.commit()

        except Exception:

            self.session.rollback()

            raise

    # =====================================================
    # CREATE
    # =====================================================

    def create(
        self,
        entity: T,
        *,
        commit: bool = True,
    ) -> T:

        self.session.add(entity)

        if commit:

            self.session.commit()

            self.session.refresh(entity)

        return entity

    def create_many(
        self,
        entities: Sequence[T],
        *,
        commit: bool = True,
    ) -> list[T]:

        self.session.add_all(entities)

        if commit:

            self.session.commit()

            for entity in entities:

                self.session.refresh(entity)

        return list(entities)

    def save(
        self,
        entity: T,
    ) -> T:

        self.session.add(entity)

        self.session.commit()

        self.session.refresh(entity)

        return entity

    # =====================================================
    # READ
    # =====================================================

    def get_by_id(
        self,
        entity_id: int,
        *,
        include_deleted: bool = False,
    ) -> T | None:

        stmt = (
            select(self.model)
            .where(self.model.id == entity_id)
        )

        if (
            hasattr(self.model, "is_deleted")
            and not include_deleted
        ):

            stmt = stmt.where(
                self.model.is_deleted.is_(False)
            )

        return self.session.scalar(stmt)

    def get(
        self,
        **filters: Any,
    ) -> T | None:

        stmt = (
            select(self.model)
            .filter_by(**filters)
        )

        if hasattr(self.model, "is_deleted"):

            stmt = stmt.where(
                self.model.is_deleted.is_(False)
            )

        return self.session.scalar(stmt)

    def get_all(
        self,
        *,
        include_deleted: bool = False,
    ) -> list[T]:

        stmt = select(self.model)

        if (
            hasattr(self.model, "is_deleted")
            and not include_deleted
        ):

            stmt = stmt.where(
                self.model.is_deleted.is_(False)
            )

        stmt = stmt.order_by(self.model.id)

        return list(
            self.session.scalars(stmt).all()
        )
        # =====================================================
    # ACTIVE / DELETED
    # =====================================================

    def get_active(self) -> list[T]:

        if not hasattr(self.model, "is_deleted"):
            return self.get_all()

        stmt = (
            select(self.model)
            .where(self.model.is_deleted.is_(False))
            .order_by(self.model.id)
        )

        return list(self.session.scalars(stmt).all())

    def get_deleted(self) -> list[T]:

        if not hasattr(self.model, "is_deleted"):
            return []

        stmt = (
            select(self.model)
            .where(self.model.is_deleted.is_(True))
            .order_by(self.model.id)
        )

        return list(self.session.scalars(stmt).all())

    # =====================================================
    # EXISTS
    # =====================================================

    def exists(
        self,
        *criteria: Any,
    ) -> bool:

        stmt = select(self.model)

        if criteria:
            stmt = stmt.where(*criteria)

        if hasattr(self.model, "is_deleted"):
            stmt = stmt.where(
                self.model.is_deleted.is_(False)
            )

        return self.session.scalar(stmt) is not None

    # =====================================================
    # COUNT
    # =====================================================

    def count(
        self,
        *criteria: Any,
    ) -> int:

        stmt = (
            select(func.count())
            .select_from(self.model)
        )

        if criteria:
            stmt = stmt.where(*criteria)

        if hasattr(self.model, "is_deleted"):
            stmt = stmt.where(
                self.model.is_deleted.is_(False)
            )

        return int(self.session.scalar(stmt) or 0)

    # =====================================================
    # FIRST / LAST
    # =====================================================

    def first(
        self,
        stmt: Select | None = None,
    ) -> T | None:

        if stmt is None:

            stmt = select(self.model)

            if hasattr(self.model, "is_deleted"):
                stmt = stmt.where(
                    self.model.is_deleted.is_(False)
                )

            stmt = stmt.order_by(self.model.id.asc()).limit(1)

        return self.session.scalar(stmt)

    def last(self) -> T | None:

        stmt = select(self.model)

        if hasattr(self.model, "is_deleted"):
            stmt = stmt.where(
                self.model.is_deleted.is_(False)
            )

        stmt = stmt.order_by(self.model.id.desc()).limit(1)

        return self.session.scalar(stmt)

    # =====================================================
    # FILTER
    # =====================================================

    def filter(
        self,
        *criteria: Any,
    ) -> list[T]:

        stmt = select(self.model)

        if criteria:
            stmt = stmt.where(*criteria)

        if hasattr(self.model, "is_deleted"):
            stmt = stmt.where(
                self.model.is_deleted.is_(False)
            )

        return list(self.session.scalars(stmt).all())

    def filter_by(
        self,
        **filters: Any,
    ) -> list[T]:

        stmt = (
            select(self.model)
            .filter_by(**filters)
        )

        if hasattr(self.model, "is_deleted"):
            stmt = stmt.where(
                self.model.is_deleted.is_(False)
            )

        return list(self.session.scalars(stmt).all())

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        column: Any,
        value: str,
    ) -> list[T]:

        stmt = (
            select(self.model)
            .where(column.ilike(f"%{value}%"))
        )

        if hasattr(self.model, "is_deleted"):
            stmt = stmt.where(
                self.model.is_deleted.is_(False)
            )

        return list(self.session.scalars(stmt).all())

    # =====================================================
    # ORDER BY
    # =====================================================

    def order_by(
        self,
        column: Any,
        *,
        descending: bool = False,
    ) -> list[T]:

        stmt = select(self.model)

        if hasattr(self.model, "is_deleted"):
            stmt = stmt.where(
                self.model.is_deleted.is_(False)
            )

        if descending:
            stmt = stmt.order_by(column.desc())
        else:
            stmt = stmt.order_by(column.asc())

        return list(
            self.session.scalars(stmt).all()
        )

    # =====================================================
    # PAGINATION
    # =====================================================

    def paginate(
        self,
        stmt: Any,
        page_request: PageRequest,
    ) -> PagedResult[T]:

        total_stmt = (
            stmt.with_only_columns(func.count())
            .order_by(None)
        )

        total_count = int(
            self.session.scalar(total_stmt) or 0
        )

        stmt = (
            stmt.offset(page_request.offset)
            .limit(page_request.page_size)
        )

        items = list(
            self.session.scalars(stmt).all()
        )

        return PagedResult(
            items=items,
            total_count=total_count,
            page=page_request.page,
            page_size=page_request.page_size,
        )

    # =====================================================
    # UPDATE
    # =====================================================

    def update(
        self,
        entity: T,
        *,
        commit: bool = True,
    ) -> T:

        if commit:
            self.session.commit()
            self.session.refresh(entity)

        return entity

    def update_fields(
        self,
        entity: T,
        values: dict[str, Any],
        *,
        commit: bool = True,
    ) -> T:

        for key, value in values.items():

            if hasattr(entity, key):
                setattr(entity, key, value)

        if commit:
            self.session.commit()
            self.session.refresh(entity)

        return entity

    # =====================================================
    # DELETE
    # =====================================================

    def delete(
        self,
        entity: T,
        *,
        commit: bool = True,
    ) -> None:

        self.session.delete(entity)

        if commit:
            self.session.commit()

    def delete_by_id(
        self,
        entity_id: int,
        *,
        commit: bool = True,
    ) -> bool:

        entity = self.get_by_id(
            entity_id,
            include_deleted=True,
        )

        if entity is None:
            return False

        self.session.delete(entity)

        if commit:
            self.session.commit()

        return True

    def get_deleted(
        self,
        **filters,
    ) -> T | None:

        stmt = (
            select(self.model)
            .where(self.model.is_deleted.is_(True))
        )

        for key, value in filters.items():
            stmt = stmt.where(
                getattr(self.model, key) == value
            )

        return self.first(stmt)

    # =====================================================
    # SOFT DELETE
    # =====================================================

    def soft_delete(
        self,
        entity: T,
        *,
        commit: bool = True,
    ) -> T:

        if hasattr(entity, "is_deleted"):
            entity.is_deleted = True

        if hasattr(entity, "deleted_at"):
            entity.deleted_at = datetime.now()

        if commit:
            self.session.commit()
            self.session.refresh(entity)

        return entity

    def soft_delete_by_id(
        self,
        entity_id: int,
        *,
        commit: bool = True,
    ) -> bool:

        entity = self.get_by_id(
            entity_id,
            include_deleted=True,
        )

        if entity is None:
            return False

        self.soft_delete(
            entity,
            commit=commit,
        )

        return True
    def hard_delete(
    self,
    entity: T,
    *,
    commit: bool = True,
        ) -> None:
        """
        Kaydı veritabanından tamamen siler.
        """

        self.session.delete(entity)

        if commit:
            self.session.commit()
    # =====================================================
    # RESTORE
    # =====================================================

    def restore(
        self,
        entity: T,
        *,
        commit: bool = True,
    ) -> T:

        if hasattr(entity, "is_deleted"):
            entity.is_deleted = False

        if hasattr(entity, "deleted_at"):
            entity.deleted_at = None

        if commit:
            self.session.commit()
            self.session.refresh(entity)

        return entity

    # =====================================================
    # BULK
    # =====================================================

    def bulk_insert(
        self,
        entities: Sequence[T],
        *,
        commit: bool = True,
    ) -> list[T]:

        self.session.add_all(entities)

        if commit:
            self.session.commit()

        return list(entities)

    def bulk_update(
        self,
        entities: Sequence[T],
        *,
        commit: bool = True,
    ) -> list[T]:

        if commit:
            self.session.commit()

        return list(entities)

    def bulk_delete(
        self,
        entities: Sequence[T],
        *,
        commit: bool = True,
    ) -> None:

        for entity in entities:
            self.session.delete(entity)

        if commit:
            self.session.commit()

    # =====================================================
    # SESSION
    # =====================================================

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def flush(self) -> None:
        self.session.flush()

    def refresh(
        self,
        entity: T,
    ) -> None:
        self.session.refresh(entity)

    # =====================================================
    # EXECUTE
    # =====================================================

    def execute(
        self,
        stmt: Any,
    ) -> Any:

        return self.session.execute(stmt)

    def scalar(
        self,
        stmt: Any,
    ) -> Any:

        return self.session.scalar(stmt)

    def all(self, stmt):
        return list(self.session.scalars(stmt).all())

    def one(self, stmt):
        return self.session.scalar(stmt)
    
    def stmt(self):
        return select(self.model)
    def active_stmt(self):
        return (
        select(self.model)
        .where(self.model.is_deleted.is_(False))
        )
    
    def count_stmt(
    self,
    stmt,
) -> int:

        stmt = stmt.with_only_columns(func.count()).order_by(None)

        return int(self.session.scalar(stmt) or 0)