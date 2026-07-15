from pydantic import BaseModel, HttpUrl, Field


class DocumentSchema(BaseModel):
    """Описание структуры документа"""

    url: HttpUrl = Field(min_length=1, max_length=2083)
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """Описание структуры ответа на запрос документа тарифа по счету"""

    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """Описание структуры ответа на запрос документа контракта по счету"""

    contract: DocumentSchema
