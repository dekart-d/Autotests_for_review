# Метод для доставки тестовых данных в тесты (в самой первой версии теста все тестовые данные были объявлены в самих тестах)
from random import choice
import data.data_value


class ValueGenerator:

    def __init__(self):
        self.values = self._genetate_data()

    def _genetate_data(self):
        lastname = data.data_value.lastname
        firstname = data.data_value.firstname
        middlename = data.data_value.middlename
        phone = data.data_value.phone
        smsCode = data.data_value.smsCode
        email = data.data_value.email
        birthDate = data.data_value.birthDate
        birthPlace = data.data_value.birthPlace
        passport = data.data_value.passport
        passportCode = data.data_value.passportCode
        passportDateGive = data.data_value.passportDateGive
        passportByGive = data.data_value.passportByGive
        inn = data.data_value.inn
        snils = data.data_value.snils
        registration_address = data.data_value.registration_address
        fact_address = data.data_value.fact_address
        name_organization = data.data_value.name_organization
        position_work = data.data_value.position_work
        monthly_income = data.data_value.monthly_income
        work_phone = data.data_value.work_phone
        additional_income_sum = data.data_value.additional_income_sum
        work_address = data.data_value.work_address
        contact_full_name = data.data_value.contact_full_name
        contact_phone = data.data_value.contact_phone
        sum_get_money = data.data_value.sum_get_money
        get_period = data.data_value.get_period
        promo_code = data.data_value.promo_code
        sms_code_last = data.data_value.sms_code_last
        buzy = data.data_value.buzy

        return {'last_name': choice(lastname), 'first_name': choice(firstname),
                'middlename': choice(middlename), 'phone': choice(phone), 'smsCode': choice(smsCode),
                'email': choice(email), 'birthDate': choice(birthDate), 'birthPlace': choice(birthPlace),
                'passport': choice(passport), 'passportCode': choice(passportCode),
                'passportDateGive': choice(passportDateGive), 'passportByGive': choice(passportByGive),
                'inn': choice(inn), 'snils': choice(snils), 'registration_address': choice(registration_address),
                'fact_address': choice(fact_address), 'buzy': choice(buzy), 'name_organization': choice(name_organization),
                'position_work': choice(position_work), 'monthly_income': choice(monthly_income),
                'work_phone': choice(work_phone), 'additional_income_sum': choice(additional_income_sum),
                'work_address': choice(work_address), 'contact_full_name': choice(contact_full_name),
                'contact_phone': choice(contact_phone), 'sum_get_money': choice(sum_get_money),
                'get_period': choice(get_period), 'promo_code': choice(promo_code),
                'sms_code_last': choice(sms_code_last)}

    def get_last_name(self):
        return self.values['last_name']

    def get_first_name(self):
        return self.values['first_name']

    def get_middle_name(self):
        return self.values['middlename']

    def get_phone(self):
        return self.values['phone']

    def get_sms_code(self):
        return self.values['smsCode']

    def get_email(self):
        return self.values['email']

    def get_birth_date(self):
        return self.values['birthDate']

    def get_birth_place(self):
        return self.values['birthPlace']

    def get_passport(self):
        return self.values['passport']

    def get_passport_code(self):
        return self.values['passportCode']

    def get_passport_date_give(self):
        return self.values['passportDateGive']

    def get_passport_by_give(self):
        return self.values['passportByGive']

    def get_inn(self):
        return self.values['inn']

    def get_snils(self):
        return self.values['snils']

    def get_registration_address(self):
        return self.values['registration_address']

    def get_fact_address(self):
        return self.values['fact_address']

    def get_name_organization(self):
        return self.values['name_organization']

    def get_position_work(self):
        return self.values['position_work']

    def get_monthly_income(self):
        return self.values['monthly_income']

    def get_work_phone(self):
        return self.values['work_phone']

    def get_additional_income_sum(self):
        return self.values['additional_income_sum']

    def get_work_address(self):
        return self.values['work_address']

    def get_contact_full_name(self):
        return self.values['contact_full_name']

    def get_contact_phone(self):
        return self.values['contact_phone']

    def get_sum_get_money(self):
        return self.values['sum_get_money']

    def get_get_period(self):
        return self.values['get_period']

    def get_promo_code(self):
        return self.values['promo_code']

    def get_sms_code_last(self):
        return self.values['sms_code_last']

    def get_buzy(self):
        return self.values['buzy']
