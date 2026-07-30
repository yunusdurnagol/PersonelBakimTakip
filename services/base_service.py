"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : services/base_service.py
Açıklama   : Generic Base Service
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from typing import Any
from typing import Generic
from typing import Sequence
from typing import TypeVar

from repositories.base_repository import BaseRepository
from repositories.page_request import PageRequest
from repositories.result import PagedResult

T = TypeVar("T")
 

class BaseService(Generic[T]):
    """
    Generic Base Service

    Tüm servis sınıfları bu sınıftan türetilir.
    """

    def __init__(
        self,
        repository: BaseRepository[T],
    ) -> None:

        self.repository = repository

    # =====================================================
    # CREATE
    # =====================================================

    def create(
        self,
        entity: T,
        *,
        commit: bool = True,
    ) -> T:

        return self.repository.create(
            entity,
            commit=commit,
        )

    def create_many(
        self,
        entities: Sequence[T],
        *,
        commit: bool = True,
    ) -> list[T]:

        return self.repository.create_many(
            entities,
            commit=commit,
        )

    def save(
        self,
        entity: T,
    ) -> T:

        return self.repository.save(entity)

    # =====================================================
    # READ
    # =====================================================

    def get_by_id(
        self,
        entity_id: int,
        *,
        include_deleted: bool = False,
    ) -> T | None:

        return self.repository.get_by_id(
            entity_id,
            include_deleted=include_deleted,
        )

    def get(
        self,
        **filters: Any,
    ) -> T | None:

        return self.repository.get(
            **filters,
        )

    def get_all(
        self,
        *,
        include_deleted: bool = False,
    ) -> list[T]:

        return self.repository.get_all(
            include_deleted=include_deleted,
        )

    def get_active(self) -> list[T]:

        return self.repository.get_active()

    def get_deleted(
        self,
        **filters,
    ):

        return self.repository.get_deleted(
            **filters,
        )

    # =====================================================
    # EXISTS
    # =====================================================

    def exists(
        self,
        *criteria: Any,
    ) -> bool:

        return self.repository.exists(
            *criteria,
        )

    # =====================================================
    # COUNT
    # =====================================================

    def count(
        self,
        *criteria: Any,
    ) -> int:

        return self.repository.count(
            *criteria,
        )

    # =====================================================
    # FIRST / LAST
    # =====================================================

    def first(
        self,
        stmt=None,
    ):

        return self.repository.first(stmt)

    def last(self):

        return self.repository.last()

    # =====================================================
    # FILTER
    # =====================================================

    def filter(
        self,
        *criteria: Any,
    ) -> list[T]:

        return self.repository.filter(
            *criteria,
        )

    def filter_by(
        self,
        **filters: Any,
    ) -> list[T]:

        return self.repository.filter_by(
            **filters,
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search(
        self,
        column,
        value: str,
    ) -> list[T]:

        return self.repository.search(
            column,
            value,
        )

    # =====================================================
    # ORDER BY
    # =====================================================

    def order_by(
        self,
        column,
        *,
        descending: bool = False,
    ) -> list[T]:

        return self.repository.order_by(
            column,
            descending=descending,
        )

    # =====================================================
    # PAGINATION
    # =====================================================

    def paginate(
        self,
        stmt,
        page_request: PageRequest,
    ) -> PagedResult[T]:

        return self.repository.paginate(
            stmt,
            page_request,
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

        return self.repository.update(
            entity,
            commit=commit,
        )

    def update_fields(
        self,
        entity: T,
        values: dict[str, Any],
        *,
        commit: bool = True,
    ) -> T:

        return self.repository.update_fields(
            entity,
            values,
            commit=commit,
        )

    # =====================================================
    # DELETE
    # =====================================================

    def delete(
        self,
        entity: T,
        *,
        commit: bool = True,
    ) -> None:

        self.repository.delete(
            entity,
            commit=commit,
        )

    def delete_by_id(
        self,
        entity_id: int,
        *,
        commit: bool = True,
    ) -> bool:

        return self.repository.delete_by_id(
            entity_id,
            commit=commit,
        )

    def hard_delete(
        self,
        entity: T,
        *,
        commit: bool = True,
    ) -> None:

        self.repository.hard_delete(
            entity,
            commit=commit,
        )

    # =====================================================
    # SOFT DELETE
    # =====================================================

    def soft_delete(
        self,
        entity: T,
        *,
        commit: bool = True,
    ) -> T:

        return self.repository.soft_delete(
            entity,
            commit=commit,
        )

    def soft_delete_by_id(
        self,
        entity_id: int,
        *,
        commit: bool = True,
    ) -> bool:

        return self.repository.soft_delete_by_id(
            entity_id,
            commit=commit,
        )

    # =====================================================
    # RESTORE
    # =====================================================

    def restore(
        self,
        entity: T,
        *,
        commit: bool = True,
    ) -> T:

        return self.repository.restore(
            entity,
            commit=commit,
        )

    # =====================================================
    # BULK
    # =====================================================

    def bulk_insert(
        self,
        entities: Sequence[T],
        *,
        commit: bool = True,
    ) -> list[T]:

        return self.repository.bulk_insert(
            entities,
            commit=commit,
        )

    def bulk_update(
        self,
        entities: Sequence[T],
        *,
        commit: bool = True,
    ) -> list[T]:

        return self.repository.bulk_update(
            entities,
            commit=commit,
        )

    def bulk_delete(
        self,
        entities: Sequence[T],
        *,
        commit: bool = True,
    ) -> None:

        self.repository.bulk_delete(
            entities,
            commit=commit,
        )

    # =====================================================
    # SESSION
    # =====================================================

    def commit(self) -> None:

        self.repository.commit()

    def rollback(self) -> None:

        self.repository.rollback()

    def flush(self) -> None:

        self.repository.flush()

    def refresh(
        self,
        entity: T,
    ) -> None:

        self.repository.refresh(entity)

    # =====================================================
    # EXECUTE
    # =====================================================

    def execute(
        self,
        stmt,
    ):

        return self.repository.execute(stmt)

    def scalar(
        self,
        stmt,
    ):

        return self.repository.scalar(stmt)

    def all(
        self,
        stmt,
    ):

        return self.repository.all(stmt)

    def one(
        self,
        stmt,
    ):

        return self.repository.one(stmt)

    def stmt(self):

        return self.repository.stmt()

    def active_stmt(self):

        return self.repository.active_stmt()

    def count_stmt(
        self,
        stmt,
    ) -> int:

        return self.repository.count_stmt(stmt)