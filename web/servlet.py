""" Web server views/load description (high-level package) """

import asyncio
import logging
import os
import traceback

from typing import Callable, Awaitable, Any

import aiohttp_jinja2
import jinja2

from aiohttp import web

from .views import builder, landing


logging.basicConfig(filename='gramBuilder.log', level=40)
STATIC_STR_PATH = os.path.join(os.path.dirname(__file__), 'static')


async def _register_uri(app_: web.Application) -> None:
    """ Use correct URI with proper handlers """
    app_.add_routes([
        web.get('/', landing),
        web.post('/build/', builder),
    ])


@web.middleware
async def log_unexpected(
        request: web.Request,
        handler: Callable[[web.Request], Awaitable[web.Response]]
) -> web.Response:
    """ Log any 500 to log file """
    try:
        response = await handler(request)
    except web.HTTPError as http_err:
        raise http_err
    except Exception:
        tb = traceback.format_exc()
        logging.critical(f'Unexpected error handled - {tb}')
        response = web.Response(status=500)
    return response


async def app(*_args: Any) -> web.Application:
    """ Short-hand alias for gunicorn serving purposes

    Notes:
        on_startup hook runs ONCE the app is being loaded. It prepares app
        configuration. Check app_setup hook for introspection

    """
    _app = web.Application(
        middlewares=[log_unexpected],
        loop=asyncio.get_event_loop()
    )
    aiohttp_jinja2.setup(_app, loader=jinja2.FileSystemLoader(STATIC_STR_PATH))
    _app.on_startup.extend([_register_uri])
    return _app
