from typing import Annotated
from fastapi import APIRouter, Depends, Query

from src.currency.services import convert

router = APIRouter(prefix='/api')


async def common_parameters(
        from_currency: Annotated[str, Query(alias='from', min_length=3, max_length=3)],
        to_currency: Annotated[str, Query(alias='to', min_length=3, max_length=3)],
        value: int = 1
):
    return {"from_currency": from_currency, "to_currency": to_currency, "value": value}


@router.get('/rates/')
def cur_convert(common=Depends(common_parameters)):
    result = convert(**common)
    return result
