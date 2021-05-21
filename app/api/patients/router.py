from fastapi import APIRouter
from .actions import (
    get_patient,
    get_patients,
    post_patient,
    put_patient,
    delete_patient
)
from .schemas import (
    Patients, Patient
)


router = APIRouter(
    prefix='/patients',
    tags=['patients']
)
router.add_api_route(
    path='',
    endpoint=get_patients,
    response_model=Patients,
    methods=['GET']
)
router.add_api_route(
    path='',
    endpoint=post_patient,
    response_model=Patient,
    methods=['POST']
)
router.add_api_route(
    path='/{id}',
    endpoint=get_patient,
    response_model=Patient,
    methods=['GET']
)
router.add_api_route(
    path='/{id}',
    endpoint=put_patient,
    response_model=Patient,
    methods=['PUT']
)
router.add_api_route(
    path='/{id}',
    endpoint=delete_patient,
    methods=['DELETE']
)
