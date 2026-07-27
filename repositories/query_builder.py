"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/query_builder.py
Açıklama   : Generic SQLAlchemy Query Builder
Yazar      : Yunus Durnagöl
Sürüm      : 2.0.0
---------------------------------------------------------
"""

from __future__ import annotations

from typing import Any
from typing import Generic
from typing import Type
from typing import TypeVar

from sqlalchemy import Select
from sqlalchemy import and_
from sqlalchemy import func
from sqlalchemy import or_
from sqlalchemy import select

from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.orm import joinedload

from orm.base_model import BaseModel

from repositories.enums import FilterOperator
from repositories.enums import SortDirection
from repositories.filters import FilterRule
from repositories.filters import SortRule
from repositories.pagination import PageRequest

T = TypeVar("T", bound=BaseModel)


class QueryBuilder(Generic[T]):
    """
    Generic SQLAlchemy Query Builder

    Bu sınıf;

    - Filtreleme
    - Global Arama
    - Sıralama
    - Pagination
    - Soft Delete
    - Include
    - Count
    - Export

    işlemlerini oluşturur.

    Repository sadece bu sınıfı kullanır.
    """

    # ---------------------------------------------------------
    # Constructor
    # ---------------------------------------------------------

    def __init__(
        self,
        model: Type[T],
        column_map: dict[str, InstrumentedAttribute],
    ) -> None:

        self.model = model

        self.column_map = column_map

        self.statement: Select = select(model)

    # ---------------------------------------------------------
    # Base Query
    # ---------------------------------------------------------

    def base(self) -> "QueryBuilder[T]":

        self.statement = select(self.model)

        return self

    # ---------------------------------------------------------
    # Soft Delete
    # ---------------------------------------------------------

    def apply_soft_delete(
        self,
        include_deleted: bool = False,
    ) -> "QueryBuilder[T]":

        if include_deleted:

            return self

        if hasattr(self.model, "is_deleted"):

            self.statement = self.statement.where(
                self.model.is_deleted.is_(False)
            )

        return self

    # ---------------------------------------------------------
    # Include
    # ---------------------------------------------------------

    def include(
        self,
        relations: list[str] | None,
    ) -> "QueryBuilder[T]":

        if not relations:

            return self

        options = []

        for relation in relations:

            if hasattr(self.model, relation):

                options.append(
                    joinedload(
                        getattr(
                            self.model,
                            relation,
                        )
                    )
                )

        if options:

            self.statement = self.statement.options(
                *options
            )

        return self

    # ---------------------------------------------------------
    # Filters
    # ---------------------------------------------------------

    def add_filters(
        self,
        filters: list[FilterRule] | None,
    ) -> "QueryBuilder[T]":

        if not filters:

            return self

        for rule in filters:

            column = self.column_map.get(
                rule.field
            )

            if column is None:

                raise ValueError(
                    f"Bilinmeyen alan : {rule.field}"
                )

            self._apply_filter(
                column,
                rule,
            )

        return self

    # ---------------------------------------------------------
    # Apply Filter
    # ---------------------------------------------------------

    def _apply_filter(
        self,
        column: InstrumentedAttribute,
        rule: FilterRule,
    ) -> None:

        operator = rule.operator

        value = rule.value

        second = getattr(
            rule,
            "second_value",
            None,
        )

        match operator:

            # ---------------------------------------------
            # =
            # ---------------------------------------------

            case FilterOperator.EQ:

                self.statement = self.statement.where(
                    column == value
                )

            # ---------------------------------------------
            # !=
            # ---------------------------------------------

            case FilterOperator.NOT_EQ:

                self.statement = self.statement.where(
                    column != value
                )

            # ---------------------------------------------
            # >
            # ---------------------------------------------

            case FilterOperator.GT:

                self.statement = self.statement.where(
                    column > value
                )

            # ---------------------------------------------
            # >=
            # ---------------------------------------------

            case FilterOperator.GTE:

                self.statement = self.statement.where(
                    column >= value
                )

            # ---------------------------------------------
            # <
            # ---------------------------------------------

            case FilterOperator.LT:

                self.statement = self.statement.where(
                    column < value
                )

            # ---------------------------------------------
            # <=
            # ---------------------------------------------

            case FilterOperator.LTE:

                self.statement = self.statement.where(
                    column <= value
                )

            # ---------------------------------------------
            # CONTAINS
            # ---------------------------------------------

            case FilterOperator.CONTAINS:

                if value is not None:

                    self.statement = self.statement.where(
                        column.ilike(f"%{value}%")
                    )

            # ---------------------------------------------
            # STARTS WITH
            # ---------------------------------------------

            case FilterOperator.STARTS_WITH:

                if value is not None:

                    self.statement = self.statement.where(
                        column.ilike(f"{value}%")
                    )

            # ---------------------------------------------
            # ENDS WITH
            # ---------------------------------------------

            case FilterOperator.ENDS_WITH:

                if value is not None:

                    self.statement = self.statement.where(
                        column.ilike(f"%{value}")
                    )

            # ---------------------------------------------
            # BETWEEN
            # ---------------------------------------------

            case FilterOperator.BETWEEN:

                if value is not None and second is not None:

                    self.statement = self.statement.where(
                        column.between(value, second)
                    )

            # ---------------------------------------------
            # IN
            # ---------------------------------------------

            case FilterOperator.IN:

                if value:

                    self.statement = self.statement.where(
                        column.in_(value)
                    )

            # ---------------------------------------------
            # NOT IN
            # ---------------------------------------------

            case FilterOperator.NOT_IN:

                if value:

                    self.statement = self.statement.where(
                        ~column.in_(value)
                    )

            # ---------------------------------------------
            # IS NULL
            # ---------------------------------------------

            case FilterOperator.IS_NULL:

                self.statement = self.statement.where(
                    column.is_(None)
                )

            # ---------------------------------------------
            # IS NOT NULL
            # ---------------------------------------------

            case FilterOperator.IS_NOT_NULL:

                self.statement = self.statement.where(
                    column.is_not(None)
                )

            # ---------------------------------------------
            # Varsayılan
            # ---------------------------------------------

            case _:

                raise ValueError(
                    f"Desteklenmeyen filtre operatörü : {operator}"
                )

    # ---------------------------------------------------------
    # Global Search
    # ---------------------------------------------------------

    def add_search(
        self,
        search_text: str | None,
        search_fields: list[str] | None,
    ) -> "QueryBuilder[T]":

        if not search_text:

            return self

        if not search_fields:

            return self

        keywords = [
            word.strip()
            for word in search_text.split()
            if word.strip()
        ]

        if not keywords:

            return self

        keyword_groups = []

        for keyword in keywords:

            keyword_conditions = []

            for field in search_fields:

                column = self.column_map.get(field)

                if column is None:

                    continue

                keyword_conditions.append(
                    column.ilike(f"%{keyword}%")
                )

            if keyword_conditions:

                keyword_groups.append(
                    or_(*keyword_conditions)
                )

        if keyword_groups:

            self.statement = self.statement.where(
                and_(*keyword_groups)
            )

        return self

    # ---------------------------------------------------------
    # Sorting
    # ---------------------------------------------------------

    def add_sort(
        self,
        sorts: list[SortRule] | None,
    ) -> "QueryBuilder[T]":

        if not sorts:

            return self

        for rule in sorts:

            column = self.column_map.get(
                rule.field
            )

            if column is None:

                raise ValueError(
                    f"Bilinmeyen alan : {rule.field}"
                )

            if rule.direction == SortDirection.ASC:

                self.statement = self.statement.order_by(
                    column.asc().nulls_last()
                )

            else:

                self.statement = self.statement.order_by(
                    column.desc().nulls_last()
                )

        return self

    # ---------------------------------------------------------
    # Pagination
    # ---------------------------------------------------------

    def add_pagination(
        self,
        page_request: PageRequest | None,
        max_page_size: int = 500,
    ) -> "QueryBuilder[T]":

        if page_request is None:
            return self

        page_size = max(1, min(page_request.page_size, max_page_size))
        offset = max(0, page_request.offset)

        self.statement = (
            self.statement
            .limit(page_size)
            .offset(offset)
        )

        return self

    # ---------------------------------------------------------
    # DISTINCT
    # ---------------------------------------------------------

    def distinct(
        self,
        enabled: bool = True,
    ) -> "QueryBuilder[T]":

        if enabled:
            self.statement = self.statement.distinct()

        return self

    # ---------------------------------------------------------
    # Reset
    # ---------------------------------------------------------

    def reset(self) -> "QueryBuilder[T]":

        self.statement = select(self.model)

        return self

    # ---------------------------------------------------------
    # Clone
    # ---------------------------------------------------------

    def clone(self) -> "QueryBuilder[T]":

        builder = QueryBuilder(
            model=self.model,
            column_map=self.column_map,
        )

        builder.statement = self.statement

        return builder

    # ---------------------------------------------------------
    # Build
    # ---------------------------------------------------------

    def build(self) -> Select:

        return self.statement

    # ---------------------------------------------------------
    # Build Count
    # ---------------------------------------------------------

    def build_count(self) -> Select:

        count_query = (
            self.statement
            .order_by(None)
            .limit(None)
            .offset(None)
        )

        return (
            select(func.count())
            .select_from(count_query.subquery())
        )

    # ---------------------------------------------------------
    # Build Export
    # ---------------------------------------------------------

    def build_export(self) -> Select:

        return (
            self.statement
            .limit(None)
            .offset(None)
        )

    # ---------------------------------------------------------
    # Debug SQL
    # ---------------------------------------------------------

    def to_sql(self) -> str:

        return str(
            self.statement.compile(
                compile_kwargs={
                    "literal_binds": True
                }
            )
        )

    # ---------------------------------------------------------
    # Representation
    # ---------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(model={self.model.__name__})"
        )