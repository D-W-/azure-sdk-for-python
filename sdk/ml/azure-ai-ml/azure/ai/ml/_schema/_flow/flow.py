# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import logging

from marshmallow import fields

from azure.ai.ml._schema import YamlFileSchema
from azure.ai.ml._schema.core.fields import CodeField

module_logger = logging.getLogger(__name__)


class FlowSchema(YamlFileSchema):
    name = fields.Str(attribute="name")
    id = fields.Str(attribute="id")
    description = fields.Str(attribute="description")
    tags = fields.Dict(keys=fields.Str, attribute="tags")
    path = CodeField()
    display_name = fields.Str(attribute="display_name")
    type = fields.Str(attribute="type")
    properties = fields.Dict(keys=fields.Str, attribute="properties")
