""" Views for GramBuilder web API """
from typing import Mapping, Any

import aiohttp_jinja2
from aiohttp import web
from multidict import MultiDict

from builder import web as web_api


@aiohttp_jinja2.template('templates/base.html')
def landing(_request: web.Request) -> Mapping[str, str]:
    """ GramBuilder landing handler """
    return {}


async def builder(request: web.Request) -> web.Response:
    """ GramBuilder API handler """
    data: Any = await request.post()
    text = data['file'].file.read().decode('utf-8')
    grammar = await web_api(text)
    full_name = f'{data["name"]}.grxml'
    return web.Response(
        status=200,
        reason='OK',
        body=grammar,
        headers=MultiDict({
            'Content-Type': 'application/xml',
            'CONTENT-DISPOSITION': f'attachment; filename="{full_name}"'
        })
    )
