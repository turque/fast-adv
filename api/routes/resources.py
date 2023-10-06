from os import getcwd

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(prefix='/resources', tags=['resources'])


path = getcwd()


@router.get('/img/{filename}')
def get_img(filename: str):
    filepath = path.join(f'{path}/public/img/', path.basename(filename))
    return FileResponse(filepath)
