"""
---------------------------------------------------------
Proje      : Personel ve Bakım Yönetim Sistemi
Dosya      : repositories/enums.py
Açıklama   : Repository Enum Tanımları
Yazar      : Yunus Durnagöl
Sürüm      : 1.0.0
---------------------------------------------------------
"""

from enum import Enum


class FilterOperator(str, Enum):

    EQ = "eq"

    NOT_EQ = "not_eq"

    GT = "gt"

    GTE = "gte"

    LT = "lt"

    LTE = "lte"

    CONTAINS = "contains"

    STARTS_WITH = "starts_with"

    ENDS_WITH = "ends_with"

    BETWEEN = "between"

    IN = "in"

    IS_NULL = "is_null"

    IS_NOT_NULL = "is_not_null"


class SortDirection(str, Enum):

    ASC = "asc"

    DESC = "desc"