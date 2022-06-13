import asyncio

import pytest
from aiohttp import ClientSession

from aiopywttr import Wttr


@pytest.mark.asyncio()
async def test_validation() -> None:
    async with ClientSession() as session:
        wttr = Wttr("Paris", session=session)
        await asyncio.gather(
            wttr.af(),
            wttr.am(),
            wttr.ar(),
            wttr.be(),
            wttr.bn(),
            wttr.ca(),
            wttr.da(),
            wttr.de(),
            wttr.el(),
            wttr.et(),
            wttr.fa(),
            wttr.fr(),
            wttr.hi(),
            wttr.hu(),
            wttr.ia(),
            wttr.id(),
            wttr.it(),
            wttr.lt(),
            wttr.mg(),
            wttr.nb(),
            wttr.nl(),
            wttr.oc(),
            wttr.pl(),
            wttr.pt_br(),
            wttr.ro(),
            wttr.ru(),
            wttr.ta(),
            wttr.th(),
            wttr.tr(),
            wttr.uk(),
            wttr.vi(),
            wttr.zh_cn(),
            wttr.zh_tw(),
        )
