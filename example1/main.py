#TODO       Push to github ASAP!

#FIXME      debug Depends() create new EmailService every time!

#TODO 1h    [PUT?] / [PATCH?] for 3 entities
#TODO 1h    How to remove id (auto increment) from POST?
#TODO 30'   Hide password

#FIXME ??   length constraint on EmailStr?

#TODO 1h+   Use better (common) injection for better modularity?

#TODO 1h+   Better doc: status code (raised from HTTPException)
#TODO 1h    Add authentication

#TODO 2h+   Add persistence or DB
#TODO 1h+   Async or not async, that is the question.

#TODO 30'   deploy uvicorn as service
#TODO 1h+   [OVH-VPS] setup nginx properly (security)

from fastapi import FastAPI, HTTPException, Depends
from starlette import status

from model import Domain, Email, Alias
from service import EmailService

app = FastAPI()

def encrypt_password(password: str) -> str:
    #TODO real encryption!
    return password

def check_domain(service: EmailService, id: int):
    if not service.check_domain(id):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"No domain with id {id}")

def check_email(service: EmailService, id: int):
    if not service.check_email(id):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"No email with id {id}")

def check_alias(service: EmailService, id: int):
    if not service.check_alias(id):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"No alias with id {id}")

@app.get("/domain", tags = ["domain"])
def list_email_domains(service: EmailService = Depends()):
    return service.list_email_domains()

@app.post("/domain", status_code = status.HTTP_201_CREATED, tags = ["domain"])
def create_email_domain(domain: Domain, service: EmailService = Depends()):
    return service.create_email_domain(domain)

@app.delete("/domain/{domain_id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["domain"])
def delete_domain(domain_id: int, service: EmailService = Depends()):
    check_domain(service, domain_id)
    service.delete_email_domain(domain_id)

@app.get("/email", tags = ["email"])
def list_emails(service: EmailService = Depends()):
    return service.list_emails()

@app.post("/email", status_code = status.HTTP_201_CREATED, tags = ["email"])
def create_email(email: Email, service: EmailService = Depends()):
    check_domain(service, email.domain_id)
    return service.create_email(email)

@app.delete("/email/{email_id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["email"])
def delete_email(email_id: int, service: EmailService = Depends()):
    check_email(service, email_id)
    service.delete_email(email_id)

@app.get("/alias", tags = ["alias"])
def list_aliases(service: EmailService = Depends()):
    return service.list_aliases()

@app.post("/alias", status_code = status.HTTP_201_CREATED, tags = ["alias"])
def create_alias(alias: Alias, service: EmailService = Depends()):
    check_domain(service, alias.domain_id)
    return service.create_alias(alias)

@app.delete("/alias/{alias_id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["alias"])
def delete_alias(alias_id: int, service: EmailService = Depends()):
    check_alias(service, alias_id)
    service.delete_alias(alias_id)
