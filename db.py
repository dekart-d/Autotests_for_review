# Модуль для работы с БД postgresql, подключение к ней, поиск данных сессии по sid через sql запросы, удаление тестовых данных после теста
import psycopg2





class DbConnection:

    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        if self.connection:
            return

        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            connect_timeout=5
        )

    def find_sid_db(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT id, phone, email, first_name, middle_name, last_name, "
                    f"sid FROM public.form WHERE sid = '{sid}';")
        record = cur.fetchone()
        return record


    def delete_test_data_db(self, sid):
        cur = self.connection.cursor()
        cur.execute(f"DELETE FROM public.form WHERE sid = '{sid}';")
        self.connection.commit()

    def find_lastname(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT last_name FROM public.form WHERE sid = '{sid}';")
        lastname_db = cur.fetchone()
        return lastname_db[0]

    def find_firstname(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT first_name FROM public.form WHERE sid = '{sid}';")
        firstname_db = cur.fetchone()
        return firstname_db[0]

    def find_middlename(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT middle_name FROM public.form WHERE sid = '{sid}';")
        middlename_db = cur.fetchone()
        return middlename_db[0]

    def find_phone(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT phone FROM public.form WHERE sid = '{sid}';")
        phone_db = cur.fetchone()
        return phone_db[0]

    def find_email(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT email FROM public.form WHERE sid = '{sid}';")
        email_db = cur.fetchone()
        return email_db[0]

    def find_birth_place(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT birth_place FROM public.form WHERE sid = '{sid}';")
        birth_place_db = cur.fetchone()
        return birth_place_db[0]

    def find_passport(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT passport_number FROM public.form WHERE sid = '{sid}';")
        passport_db = cur.fetchone()
        return passport_db[0]

    def find_birth_date(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT birth_date FROM public.form WHERE sid = '{sid}';")
        birth_date_db = cur.fetchone()
        return birth_date_db[0]

    def find_passport_code(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT passport_code FROM public.form WHERE sid = '{sid}';")
        passport_code_db = cur.fetchone()
        return passport_code_db[0]

    def find_passport_date_give(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT passport_date FROM public.form WHERE sid = '{sid}';")
        passport_date_give_db = cur.fetchone()
        return passport_date_give_db[0]

    def find_passport_by_give(self, sid):
        cur = self.connection.cursor()

        cur.execute(f"SELECT passport_issuer FROM public.form WHERE sid = '{sid}';")
        passport_by_give_db = cur.fetchone()
        return passport_by_give_db[0]














