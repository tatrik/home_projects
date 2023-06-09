from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.models.auth import UserCreate, Token, User
from src.services.auth import AuthService, get_current_user

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post('/sing-up', response_model=Token)
def sing_up(
    user_data: UserCreate,
    service: AuthService = Depends(),
):
    """
    Creating new user.
    \f
    :param user_data:
    :param service:
    :return:
    """
    return service.register_new_user(user_data)


@router.post('/sing-in', response_model=Token)
def sing_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(),
):
    """
    Logining on service.
    \f
    :param form_data:
    :param service:
    :return:
    """
    return service.authenticate_user(
        form_data.username,
        form_data.password,
    )


@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    """
    Getting user information. For authorized users only.
    \f
    :param user:
    :return:
    """
    return user
