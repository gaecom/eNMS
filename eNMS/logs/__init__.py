from flask import Blueprint

bp = Blueprint(
    'logs_blueprint',
    __name__,
    url_prefix='/logs',
    template_folder='templates',
    static_folder='static'
)

from eNMS.base.classes import classes
from eNMS.logs.models import Log, LogRule

classes.update({'Log': Log, 'LogRule': LogRule})

import eNMS.logs.routes  # noqa: F401
