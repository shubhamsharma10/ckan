"""
This type stub file was generated by pyright.
"""

from typing import Any, Callable, Optional
from flask.wrappers import Response
import six
import ckan.model as model
import ckan.lib.api_token as api_token
import ckan.plugins as p
import logging
from sqlalchemy import inspect
from ckan.common import asbool, config, g, request, session
from six import text_type
from six.moves.urllib.parse import quote
from werkzeug.utils import cached_property, import_string
from ckan.lib.helpers import redirect_to as redirect
from ckan.lib.i18n import get_locales_from_config

APIKEY_HEADER_NAME_KEY: str
APIKEY_HEADER_NAME_DEFAULT: str

class LazyView(object):
    def __init__(
        self, import_name: str, view_name: Optional[str] = ...
    ) -> None: ...
    @cached_property
    def view(self) -> Callable: ...

def check_session_cookie(response: Response) -> Response: ...
def set_cors_headers_for_response(response: Response) -> Response: ...
def set_cache_control_headers_for_response(response: Response) -> Response: ...
def identify_user() -> Optional[Response]: ...
def set_controller_and_action() -> None: ...
def handle_i18n(environ: Optional[Any] = ...) -> None: ...
def set_ckan_current_url(environ: Any) -> None: ...