from uuid import uuid4


class Contact:
    
    def __init__(self, name: str, phone: str, email: str, contact_id: str | None = None):
        self.contact_id = contact_id or str(uuid4())
        self.name       = name
        self.phone      = phone
        self.email      = email

    def to_dict(self) -> dict:
        return {
            'id': self.contact_id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data['name'],
            phone=data['phone'],
            email=data['email'],
            contact_id=data['id']
        )
