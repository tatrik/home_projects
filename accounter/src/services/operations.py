from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from typing import List, Optional, Type

from .. import tables
from src.database import get_session
from src.models.operations import OperationKind, OperationCreate, OperationUpdate
from ..tables import Operation


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, operation_id: int) -> Type[Operation]:
        operation = (
            self.session
            .query(tables.Operation)
            .filter_by(id=operation_id)
            .first()
        )
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operation

    def get_list(self, kind: Optional[OperationKind] = None) -> List[Type[Operation]]:
        query = self.session.query(tables.Operation)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations

    def get(self, operation_id: int) -> Type[Operation]:
        return self._get(operation_id=operation_id)

    def create(self, operation_data: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, operation_id: int, operation_data: OperationUpdate) -> Type[Operation]:
        operation = self._get(operation_id=operation_id)
        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, operation_id: int) -> None:
        operation = self._get(operation_id=operation_id)
        self.session.delete(operation)
        self.session.commit()
