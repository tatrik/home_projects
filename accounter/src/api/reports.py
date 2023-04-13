from fastapi import APIRouter, UploadFile, File, Depends, BackgroundTasks
from fastapi.responses import StreamingResponse

from src.models.auth import User
from src.services.auth import get_current_user
from src.services.reports import ReportsService

router = APIRouter(
    prefix='/reports',
    tags=['reports'],
)


@router.post('/import')
def import_csv(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    reports_service: ReportsService = Depends(),
):
    """
    Import reports from csv files.
    \f
    :param background_tasks:
    :param file:
    :param user:
    :param reports_service:
    :return:
    """
    background_tasks.add_task(
        reports_service.import_csv,
        user.id,
        file.file,
    )


@router.get('/export')
def export_csv(
    user: User = Depends(get_current_user),
    reports_service: ReportsService = Depends(),
):
    """
    Export reports to csv file.
    \f
    :param user:
    :param reports_service:
    :return:
    """
    report = reports_service.export_csv(user.id)
    return StreamingResponse(
        report,
        media_type='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=report.csv'
        }
    )
