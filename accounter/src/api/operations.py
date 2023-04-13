from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response, status

from src.models.auth import User
from src.models.operations import Operation, OperationKind, OperationCreate, OperationUpdate
from src.services.auth import get_current_user
from src.services.operations import OperationsService

router = APIRouter(
    prefix='/operations',
    tags=['operations'],
)


@router.get('/', response_model=List[Operation])
def get_operations(
    kind: Optional[OperationKind] = None,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends()
):
    """
    Getting operations' list.
    - **kind**: filter by operations' kind.
    \f
    :param kind:
    :param user:
    :param service:
    :return:
    """
    return service.get_list(user_id=user.id, kind=kind)


@router.post('/', response_model=Operation)
def create_operation(
    operation_data: OperationCreate,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    """
    Creating new operation.
    \f
    :param operation_data:
    :param user:
    :param service:
    :return:
    """
    return service.create(user_id=user.id, operation_data=operation_data)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    """
    Getting an operation on its id.
    \f
    :param operation_id:
    :param user:
    :param service:
    :return:
    """
    return service.get(user_id=user.id, operation_id=operation_id)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    """
    Changing operation data.
    \f
    :param operation_id:
    :param operation_data:
    :param user:
    :param service:
    :return:
    """
    return service.update(user_id=user.id, operation_id=operation_id, operation_data=operation_data)


@router.delete('/{operation_id}')
def delete_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    """
    Removing an operation.
    \f
    :param operation_id:
    :param user:
    :param service:
    :return:
    """
    service.delete(user_id=user.id, operation_id=operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
