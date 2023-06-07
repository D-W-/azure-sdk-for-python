# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import abc
from os import PathLike
from pathlib import Path
from typing import Dict, Optional, Union

from azure.ai.ml._schema._flow.flow import FlowSchema
from azure.ai.ml.constants._common import BASE_PATH_CONTEXT_KEY, PARAMS_OVERRIDE_KEY
from azure.ai.ml.entities._util import load_from_dict

# pylint: disable=redefined-builtin, unused-argument, f-string-without-interpolation


class FlowBase(abc.ABC):
    @abc.abstractmethod
    def _to_rest_object(self):
        pass

    @classmethod
    # pylint: disable=unused-argument
    def _resolve_cls_and_type(cls, data, params_override):
        """Resolve the class to use for deserializing the data. Return current class if no override is provided.

        :param data: Data to deserialize.
        :type data: dict
        :param params_override: Parameters to override, defaults to None
        :type params_override: typing.Optional[list]
        :return: Class to use for deserializing the data & its "type". Type will be None if no override is provided.
        :rtype: tuple[class, typing.Optional[str]]
        """
        return cls, "flow"


class Flow(FlowBase):
    def __init__(
        self,
        name: str,
        type: str,
        path: str,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        tags: Optional[Dict] = None,
        properties: Optional[Dict] = None,
        **kwargs,
    ):
        self.name = name
        self.type = type
        self.path = path
        self.description = description
        self.display_name = display_name
        self.tags = tags
        self.properties = properties
        super().__init__()

    def _to_dict(self) -> Dict:
        FlowSchema(context={BASE_PATH_CONTEXT_KEY: "./"}).dump(self)

    def _to_rest_object(self):
        return {}

    @classmethod
    def _load_from_dict(cls, data: Dict, context: Dict, additional_message: str, **kwargs) -> "CommandJob":
        loaded_data = load_from_dict(FlowSchema, data, context, additional_message, **kwargs)
        return Flow(base_path=context[BASE_PATH_CONTEXT_KEY], **loaded_data)

    @classmethod
    def _load(
        cls,
        data: Optional[Dict] = None,
        yaml_path: Optional[Union[PathLike, str]] = None,
        params_override: Optional[list] = None,
        **kwargs,
    ):
        context = {
            BASE_PATH_CONTEXT_KEY: Path(yaml_path).parent if yaml_path else Path("./"),
            PARAMS_OVERRIDE_KEY: params_override,
        }
        return cls._load_from_dict(
            data=data,
            context=context,
            additional_message=f"If you are trying to configure a job that is not of type flow, please specify "
            f"the correct job type in the 'type' property.",
            **kwargs,
        )

    @classmethod
    def _from_rest_object(cls, flow):
        pass
