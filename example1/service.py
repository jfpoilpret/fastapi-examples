from model import Domain, Email, Alias

class EmailService:
    def __init__(self) -> None:
        self.domains: dict[int, Domain] = { 1: Domain(id = 1, domain = 'sans-nom.ch')}
        self.emails: dict[int, Email] = {1: Email(id = 1, domain_id = 1, email = 'kevin.payet@sans-nom.ch', password = 'verylooooongpassword')}
        self.aliases: dict[int, Alias] = {1: Alias(id = 1, domain_id = 1, source = 'kp@sans-nom.ch', destination = 'kevin.payet@sans-nom.ch')}
        print("EmailService()")
        
    def encrypt_password(password: str) -> str:
        #TODO real encryption!
        return password

    def check_domain(self, id: int) -> bool:
        return id in self.domains

    def check_email(self, id: int) -> bool:
        return id in self.emails

    def check_alias(self, id: int) -> bool:
        return id in self.aliases

    def list_email_domains(self) -> list[Domain]:
        return list(self.domains.values())

    def create_email_domain(self, domain: Domain) -> Domain | None:
        domain.id = max([id for id in self.domains.keys()], default = 0) + 1
        self.domains[domain.id] = domain
        return domain

    def delete_email_domain(self, domain_id: int) -> bool:
        if not self.check_domain(domain_id):
            return False
        related_emails = [email for email in self.emails.values() if email.domain_id == domain_id ]
        related_destinations = [email.email for email in related_emails]
        related_aliases = [alias for alias in self.aliases.values() if alias.destination in related_destinations]
        for alias in related_aliases:
            del self.aliases[alias.id]
        for email in related_emails:
            del self.emails[email.id]
        del self.domains[domain_id]
        return True

    def list_emails(self) -> list[Email]:
        return list(self.emails.values())

    def create_email(self, email: Email) -> Email | None:
        if not self.check_domain(email.domain_id):
            return None
        email.id = max([id for id in self.emails.keys()], default = 0) + 1
        email.password = EmailService.encrypt_password(email.password)
        self.emails[email.id] = email
        return email

    def delete_email(self, email_id: int) -> bool:
        #FIXME wrong!
        if not self.check_domain(email_id):
            return False
        email: Email = self.emails[email_id]
        related_aliases = [alias for alias in self.aliases.values() if alias.destination == email.email]
        for alias in related_aliases:
            del self.aliases[alias.id]
        del self.emails[email_id]
        return True

    def list_aliases(self) -> list[Alias]:
        return list(self.aliases.values())

    def create_alias(self, alias: Alias) -> Alias | None:
        if not self.check_domain(alias.domain_id):
            return None
        #TODO check source and destination domains match domain_id!
        #TODO check destination exists in emails!
        alias.id = max([id for id in self.aliases.keys()], default = 0) + 1
        self.aliases[id] = alias
        return alias

    def delete_alias(self, alias_id: int) -> bool:
        #FIXME wrong!
        if self.check_domain(alias_id):
            return False
        del self.aliases[alias_id]
        return True
