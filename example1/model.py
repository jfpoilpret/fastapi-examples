from pydantic import BaseModel, EmailStr, Field

class Domain(BaseModel):
    id: int | None = Field(title = "Internal identifier for domain")
    domain: str = Field(title = "Domain name", max_length = 63, regex = r"^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}$")

class Email(BaseModel):
    id: int | None = Field(title = "Internal identifier for email")
    domain_id: int = Field(title = "Internal identifier of email domain")
    email: EmailStr = Field(title = "Email, including domain")
    password: str = Field(title = "Mandatory password", min_length = 20, max_length = 100)

class Alias(BaseModel):
    id: int | None = Field(title = "Internal identifier for alias")
    domain_id: int = Field(title = "Internal identifier of alias domain")
    source: EmailStr = Field(title = "Email alias")
    destination: EmailStr = Field(title = "Actual email the alias points to")

