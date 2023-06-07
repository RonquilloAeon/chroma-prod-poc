from uuid import UUID

from ninja import Schema


class DocumentSerializer(Schema):
    account: UUID
    title: str = None
    content: str
