"""Проверять общую metadata моделей SQLAlchemy."""

from sqlalchemy import (
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)
from src.database.base import NAMING_CONVENTION


class TestNamingConvention:
    """Проверять стабильные имена объектов схемы базы данных."""

    def test_generates_names_for_constraints_and_indexes(self):
        """Сформировать предсказуемые имена для всех объектов схемы."""
        metadata = MetaData(naming_convention=NAMING_CONVENTION)
        parent = Table(
            'parent',
            metadata,
            Column('id', Integer, primary_key=True),
            Column('slug', String, unique=True),
            Column('title', String, index=True),
        )
        child = Table(
            'child',
            metadata,
            Column('id', Integer, primary_key=True),
            Column('parent_id', ForeignKey('parent.id')),
            Column('quantity', Integer),
        )
        check_constraint = CheckConstraint(child.c.quantity > 0)
        child.append_constraint(check_constraint)

        assert parent.primary_key.name == 'pk_parent'
        assert child.primary_key.name == 'pk_child'
        assert {constraint.name for constraint in parent.constraints} >= {
            'pk_parent',
            'uq_parent_slug',
        }
        assert {constraint.name for constraint in child.constraints} >= {
            'pk_child',
            'fk_child_parent_id_parent',
            'ck_child_quantity',
        }
        assert {index.name for index in parent.indexes} == {'ix_parent_title'}
