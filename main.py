from faker import Faker

class Base_contact():

    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        print(f'Wybieram numer {self.phone_number} i dzwonię do {self.name}')

    def __str__(self):
        return f"{self.name}, {self.phone_number} , {self.email}"

    @property
    def label_length(self):
        return len(self.name)

class Business_contact(Base_contact):
    def __init__(self, name, phone_number, email, company, job, business_phone):
        super().__init__(name, phone_number, email)
        self.company = company
        self.job = job
        self.business_phone = business_phone

    def _contact(self):
        return f'Wybieram numer {self.business_phone} i dzwonię do {self.name}'

x = 0
def create_contacts(business_card_type, quantity):
    business_card = []
    fake = Faker('pl_PL')

    if business_card_type == 'Base_contact':
        for BC in range(quantity):
            Business_card_base = Base_contact(fake.name(), fake.phone_number(), fake.email())
            business_card.append(Business_card_base)
    elif business_card_type == 'Business_contact':
        for BC in range(quantity):
            Business_card_business = Business_contact(fake.name(), fake.phone_number(), fake.email(), fake.company(), fake.job(), fake.phone_number())
            business_card.append(Business_card_business)
    return business_card

business_card = create_contacts('Base_contact', 5)
business_card += create_contacts('Business_contact', 5)

for i in business_card:
    i.contact()
    print(f'Ilość znaków imienia i nazwiska to: {i.label_length -1}')