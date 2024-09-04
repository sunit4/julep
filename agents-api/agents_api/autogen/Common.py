# generated by datamodel-codegen:
#   filename:  openapi-0.4.0.yaml

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, RootModel


class Limit(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: Annotated[int, Field(ge=1, lt=1000)]
    """
    Limit the number of results
    """


class LogitBias(RootModel[float]):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: Annotated[float, Field(ge=-100.0, le=100.0)]


class Offset(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: Annotated[int, Field(ge=0)]
    """
    Offset to apply to the results
    """


class PyExpression(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: str
    """
    A simple python expression compatible with SimpleEval.
    """


class ResourceCreatedResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: UUID
    """
    ID of created resource
    """
    created_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was created as UTC date-time
    """
    jobs: Annotated[list[UUID], Field([], json_schema_extra={"readOnly": True})]
    """
    IDs (if any) of jobs created as part of this request
    """


class ResourceDeletedResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: UUID
    """
    ID of deleted resource
    """
    deleted_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was deleted as UTC date-time
    """
    jobs: Annotated[list[UUID], Field([], json_schema_extra={"readOnly": True})]
    """
    IDs (if any) of jobs created as part of this request
    """


class ResourceUpdatedResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: UUID
    """
    ID of updated resource
    """
    updated_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was updated as UTC date-time
    """
    jobs: Annotated[list[UUID], Field([], json_schema_extra={"readOnly": True})]
    """
    IDs (if any) of jobs created as part of this request
    """


class Uuid(RootModel[UUID]):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: UUID
