from faker import Faker

class Base_contact():

    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def contact(self):
        print(f'Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}')

    def __str__(self):
        return f"{self.name}, {self.phone} , {self.email}"

    @property
    def label_length(self):
        return len(self.name + " " + self.surname)

class Business_contact(Base_contact):
    def __init__(self, name, surname, phone, email, company_name, position, work_phone):
        super().__init__(name, surname, phone, email)
        self.company_name = company_name
        self.position = position
        self.work_phone = work_phone

    def _contact(self):
        return f'Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}'


def create_contacts(business_card_type, quantity):
    business_card = []
    fake = Faker('pl_PL')

    if business_card_type == 'Base_contact':
        for BC in range(quantity):
            Business_card_base = Base_contact(fake.name(), fake.surname(), fake.phone(), fake.email())
            business_card.append(Business_card_base)
    elif business_card_type == 'Business_contact':
        for BC in range(quantity):
            Business_card_business = Business_contact(fake.name(), fake.surname(), fake.phone(), fake.email(), fake.company_name, fake.position, fake.work_phone)
            business_card.append(Business_card_business)
    return business_card

business_card = create_contacts('Base_contact', 5)
business_card = create_contacts('Business_contact', 5)