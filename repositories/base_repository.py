"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/base_repository.py
Açıklama   : Generic Base Repository
Yazar      : Yunus Durnagöl
Sürüm      : 3.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from typing import Generic
from typing import Type
from typing import TypeVar

from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy.orm import Session

from orm.base_model import BaseModel

from repositories.enums import FilterOperator
from repositories.filters import FilterRule
from repositories.filters import SortRule
from repositories.pagination import PageRequest
from repositories.query_builder import QueryBuilder
from repositories.result import PagedResult

T = TypeVar("T", bound=BaseModel)


class BaseRepository(Generic[T]):
    """
    Generic Base Repository

    Tüm repository sınıfları bu sınıftan türeyecektir.
    """

    MODEL: Type[T] | None = None

    COLUMN_MAP: dict = {}

    def __init__(
        self,
        session: Session,
    ) -> None:

        if self.MODEL is None:

            raise NotImplementedError(
                "MODEL tanımlanmamış."
            )

        self.session = session

    # ---------------------------------------------------------
    # Query Builder
    # ---------------------------------------------------------

    def query(self) -> QueryBuilder[T]:

        return QueryBuilder(

            model=self.MODEL,

            column_map=self.COLUMN_MAP,

        )

    # ---------------------------------------------------------
    # Add
    # ---------------------------------------------------------

    def add(
        self,
        entity: T,
    ) -> T:

        self.session.add(entity)

        return entity

    # ---------------------------------------------------------
    # Get By Id
    # ---------------------------------------------------------

    def get_by_id(
        self,
        entity_id: int,
        include_deleted: bool = False,
    ) -> T | None:

        query = (

            self.query()

            .apply_soft_delete(
                include_deleted
            )

            .add_filters(

                [

                    FilterRule(

                        field="id",

                        operator=FilterOperator.EQ,

                        value=entity_id,

                    )

                ]

            )

            .build()

        )

        return self.session.scalar(query)

    # ---------------------------------------------------------
    # Get First
    # ---------------------------------------------------------

    def get_first(
        self,
        filters: list[FilterRule] | None = None,
        include_deleted: bool = False,
    ) -> T | None:

        query = (

            self.query()

            .apply_soft_delete(
                include_deleted
            )

            .add_filters(
                filters
            )

            .build()

            .limit(1)

        )

        return self.session.scalar(query)

    # ---------------------------------------------------------
    # Get All
    # ---------------------------------------------------------

    def get_all(
        self,
        include_deleted: bool = False,
    ) -> list[T]:

        query = (

            self.query()

            .apply_soft_delete(
                include_deleted
            )

            .build()

        )

        return list(

            self.session.scalars(query)

        )

    # ---------------------------------------------------------
    # Exists
    # ---------------------------------------------------------

    def exists(
        self,
        entity_id: int,
    ) -> bool:

        return (

            self.get_by_id(
                entity_id
            )

            is not None

        )


    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def search(
        self,
        filters: list[FilterRule] | None = None,
        sorts: list[SortRule] | None = None,
        page_request: PageRequest | None = None,
        search_text: str | None = None,
        search_fields: list[str] | None = None,
        include: list[str] | None = None,
        include_deleted: bool = False,
    ) -> PagedResult[T]:

        builder = (
            self.query()
            .apply_soft_delete(include_deleted)
            .include(include)
            .add_filters(filters)
            .add_search(search_text, search_fields)
            .add_sort(sorts)
        )

        total = self.session.scalar(
            builder.clone().build_count()
        ) or 0

        items = list(
            self.session.scalars(
                builder
                .add_pagination(page_request)
                .build()
            )
        )

        return PagedResult(
            items=items,
            total_count=total,
            page=page_request.page if page_request else 1,
            page_size=page_request.page_size if page_request else total,
        )

    # ---------------------------------------------------------
    # Count
    # ---------------------------------------------------------

    def count(
        self,
        filters: list[FilterRule] | None = None,
        include_deleted: bool = False,
    ) -> int:

        query = (
            self.query()
            .apply_soft_delete(include_deleted)
            .add_filters(filters)
            .build_count()
        )

        return self.session.scalar(query) or 0

    # ---------------------------------------------------------
    # Soft Delete
    # ---------------------------------------------------------

    def delete(
        self,
        entity: T,
    ) -> None:

        if not hasattr(entity, "is_deleted"):

            raise AttributeError(
                f"{self.MODEL.__name__} modelinde "
                "'is_deleted' alanı bulunamadı."
            )

        entity.is_deleted = True

    # ---------------------------------------------------------
    # Restore
    # ---------------------------------------------------------

    def restore(
        self,
        entity: T,
    ) -> None:

        if not hasattr(entity, "is_deleted"):

            raise AttributeError(
                f"{self.MODEL.__name__} modelinde "
                "'is_deleted' alanı bulunamadı."
            )

        entity.is_deleted = False

    # ---------------------------------------------------------
    # Hard Delete
    # ---------------------------------------------------------

    def hard_delete(
        self,
        entity: T,
    ) -> None:

        self.session.delete(entity)

    # ---------------------------------------------------------
    # Refresh
    # ---------------------------------------------------------

    def refresh(
        self,
        entity: T,
    ) -> None:

        self.session.refresh(entity)

    # ---------------------------------------------------------
    # Flush
    # ---------------------------------------------------------

    def flush(self) -> None:

        self.session.flush()

    # ---------------------------------------------------------
    # Expunge (Detach)
    # ---------------------------------------------------------

    def detach(
        self,
        entity: T,
    ) -> None:

        self.session.expunge(entity)
    # ---------------------------------------------------------
    # Commit
    # ---------------------------------------------------------

    def commit(self) -> None:
        """
        Yapılan değişiklikleri veritabanına kaydeder.
        """

        self.session.commit()

    # ---------------------------------------------------------
    # Rollback
    # ---------------------------------------------------------

    def rollback(self) -> None:
        """
        Hata durumunda yapılan değişiklikleri geri alır.
        """

        self.session.rollback()

    # ---------------------------------------------------------
    # Execute
    # ---------------------------------------------------------

    def execute(
        self,
        statement,
    ):
        """
        Generic SQL Execute
        """

        return self.session.execute(statement)

    # ---------------------------------------------------------
    # Scalar
    # ---------------------------------------------------------

    def scalar(
        self,
        statement,
    ):
        """
        Tek değer döndürür.
        """

        return self.session.scalar(statement)

    # ---------------------------------------------------------
    # Scalars
    # ---------------------------------------------------------

    def scalars(
        self,
        statement,
    ):
        """
        Çoklu ORM nesnesi döndürür.
        """

        return self.session.scalars(statement)

    # ---------------------------------------------------------
    # Add All
    # ---------------------------------------------------------

    def add_all(
        self,
        entities: list[T],
    ) -> None:
        """
        Birden fazla nesneyi Session'a ekler.
        """

        self.session.add_all(entities)

    # ---------------------------------------------------------
    # Close Session
    # ---------------------------------------------------------

    def close(self) -> None:
        """
        Session kapatılır.
        """

        self.session.close()

    # ---------------------------------------------------------
    # Context Manager
    # ---------------------------------------------------------

    def __enter__(self):

        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ):

        if exc_type:

            self.rollback()

        else:

            self.commit()

        self.close()
