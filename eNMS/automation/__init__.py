from flask import Blueprint
from importlib import reload
from importlib.abc import Loader
from importlib.util import spec_from_file_location, module_from_spec
from os import environ
from pathlib import Path
from sqlalchemy import Boolean, Float, Integer, PickleType

bp = Blueprint(
    "automation_blueprint",
    __name__,
    url_prefix="/automation",
    template_folder="templates",
    static_folder="static",
)

from eNMS.base.classes import classes, service_classes
from eNMS.base.functions import add_classes
from eNMS.base.properties import (
    cls_to_properties,
    property_types,
    boolean_properties,
    service_import_properties,
)
from eNMS.automation.models import Job, Service, Workflow, WorkflowEdge

add_classes(Job, Service, Workflow, WorkflowEdge)
modules = []


def create_service_classes(reload_module=False) -> None:
    path_services = [Path.cwd() / "eNMS" / "automation" / "services"]
    custom_services_path = environ.get("CUSTOM_SERVICES_PATH")
    if custom_services_path:
        path_services.append(Path(custom_services_path))
    dont_create_examples = not int(environ.get("CREATE_EXAMPLES", True))
    for path in path_services:
        for file in path.glob("**/*.py"):
            if "init" in str(file):
                continue
            if dont_create_examples and "examples" in str(file):
                continue
            name = str(file).split("/")[-1][:-3]
            spec = spec_from_file_location(name, str(file))
            assert isinstance(spec.loader, Loader)
            module = module_from_spec(spec)
            modules.append(module)
            spec.loader.exec_module(module)  # type: ignore
    for cls_name, cls in service_classes.items():
        cls_to_properties[cls_name] = list(cls_to_properties["Service"])
        for col in cls.__table__.columns:
            cls_to_properties[cls_name].append(col.key)
            service_import_properties.append(col.key)
            if type(col.type) == Boolean:
                boolean_properties.append(col.key)
            if type(col.type) == PickleType and hasattr(cls, f"{col.key}_values"):
                property_types[col.key] = "list"
            else:
                property_types[col.key] = {
                    Boolean: "bool",
                    Integer: "int",
                    Float: "float",
                    PickleType: "dict",
                }.get(type(col.type), "str")


create_service_classes()
classes.update(service_classes)

import eNMS.automation.routes  # noqa: F401
