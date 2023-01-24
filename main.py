import psycopg2


def delete_db(cursor):
    """ Функция, удаляющая базу данных 'Hogwarts_database'. """
    cursor.execute("DROP TABLE IF EXISTS Hogwarts_staff, Telephone_number CASCADE;")
    conn.commit()
    print('База данных \'Hogwarts_database\' была полностью удалена.')


def check_staff_by_id(cursor, staff_id):
    """ Функция, проверяющая есть ли уже преподаватель с указанным id в базе данных. """
    cursor.execute("""
        SELECT * FROM Hogwarts_staff
        WHERE staff_id = %s
    """, (staff_id, ))
    return cursor.fetchone()


def check_staff_by_email(cursor, email):
    """ Функция, проверяющая есть ли email в базе данных. """
    cursor.execute("""
        SELECT * FROM Hogwarts_staff
        WHERE email = %s
    """, (email, ))
    return cursor.fetchone()


def check_staff_by_phone(cursor, phone_number):
    """ Функция, проверяющая есть ли номер телефона в базе данных. """
    cursor.execute("""
        SELECT * FROM Telephone_number
        WHERE phone_number = %s
    """, (phone_number, ))
    return cursor.fetchone()


def create_db(cursor):
    """ 1. Функция, создающая базу данных 'Hogwarts_database'. """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Hogwarts_staff (
            staff_id SERIAL PRIMARY KEY,
            first_name VARCHAR(30) NOT NULL,
            last_name VARCHAR(30) NOT NULL,
            email VARCHAR(80) UNIQUE NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Telephone_number (
            staff_id INTEGER REFERENCES Hogwarts_staff(staff_id),
            phone_number BIGINT UNIQUE NOT NULL  
        );
    """)
    conn.commit()
    print('База данных \'Hogwarts_database\' создана.')


def add_staff(cursor, first_name, last_name, email, phone_number=None):
    """ 2. Функция, добавляющая нового преподавателя в базу данных 'Hogwarts_database'. """
    if not check_staff_by_email(cursor, email):
        cursor.execute("""
            INSERT INTO Hogwarts_staff (first_name, last_name, email)
            VALUES (%s, %s, %s) RETURNING staff_id, first_name, last_name, email;
        """, (first_name, last_name, email))
        result = cursor.fetchone()
        if phone_number is not None:
            if not check_staff_by_phone(cursor, phone_number):
                cursor.execute("""
                    INSERT INTO Telephone_number (staff_id, phone_number)
                    VALUES (%s, %s) RETURNING phone_number;
                """, (result[0], phone_number))
                result += cursor.fetchone()
            else:
                print(f'Телефон \'{phone_number}\' уже имеется в базе данных. Добавить телефон не получится.')
        print(f'Мы добавили информацию о новом преподавателе: {result}.')
    else:
        print(f'Преподаватель с email = \'{email}\' уже существует. Добавить преподавателя не получится.')


def add_phone(cursor, staff_id, phone_number):
    """ 3. Функция, позволяющая добавить телефон для существующего преподавателя. """
    if check_staff_by_id(cursor, staff_id):
        if not check_staff_by_phone(cursor, phone_number):
            cursor.execute("""
                INSERT INTO Telephone_number (staff_id, phone_number)
                VALUES (%s, %s) RETURNING staff_id, phone_number;
            """, (staff_id, phone_number))
            result = cursor.fetchone()
            print(f'Для преподавателя с id = \'{result[0]}\' был добавлен номер телефона: \'{result[1]}\'.')
        else:
            print(f'Номер телефона \'{phone_number}\' уже есть в базе данных. Добавить телефон не получится.')
    else:
        print(f'Преподаватель с id = \'{staff_id}\' не найден. Добавить телефон не получится.')


def change_staff(cursor, staff_id, first_name=None, last_name=None, email=None, phone_number=None):
    """ 4. Функция, позволяющая изменить данные о преподавателе. """
    if check_staff_by_id(cursor, staff_id):
        if first_name:
            cursor.execute("""
                UPDATE Hogwarts_staff SET first_name=%s
                WHERE staff_id=%s;
            """, (first_name, staff_id))
            conn.commit()
            print(f'Имя преподавателя с id = \'{staff_id}\' было изменен на = \'{first_name}\'.')

        if last_name:
            cursor.execute("""
                UPDATE Hogwarts_staff SET last_name=%s
                WHERE staff_id=%s;
            """, (last_name, staff_id))
            conn.commit()
            print(f'Фамилия преподавателя с id = \'{staff_id}\' была изменена на = \'{last_name}\'.')

        if email:
            if not check_staff_by_email(cursor, email):
                cursor.execute("""
                    UPDATE Hogwarts_staff SET email=%s
                    WHERE staff_id=%s;
                """, (email, staff_id))
                conn.commit()
                print(f'Email преподавателя с id = \'{staff_id}\' был изменен на = \'{email}\'.')
            else:
                print(f'Преподаватель с email = \'{email}\' уже существует. Изменить email не получится.')

        if phone_number:
            if not check_staff_by_phone(cursor, phone_number):
                cursor.execute("""
                    UPDATE Telephone_number SET phone_number=%s
                    WHERE staff_id=%s;
                """, (phone_number, staff_id))
                conn.commit()
                print(f'Телефон преподавателя с id = \'{staff_id}\' был изменен на = \'{phone_number}\'.')
            else:
                print(f'Номер телефона \'{phone_number}\' уже есть в базе данных. Изменить телефон не получится.')
    else:
        print(f'Преподаватель с id = \'{staff_id}\' не найден в базе данных. Изменить данные не получится.')


def delete_phone(cursor, phone_number):
    """ 5. Функция, позволяющая удалить телефон для существующего преподавателя. """
    if check_staff_by_phone(cursor, phone_number):
        cursor.execute("""
            DELETE FROM Telephone_number
            WHERE phone_number = %s
        """, (phone_number, ))
        conn.commit()
        print(f'Номер телефона \'{phone_number}\' был удален из базы данных.')
    else:
        print(f'Номер телефона \'{phone_number}\' не найден в базе данных. Удалить номер не получится.')


def delete_staff(cursor, staff_id):
    """ 6. Функция, позволяющая удалить существующего преподавателя. """
    if check_staff_by_id(cursor, staff_id):
        cursor.execute("""
            DELETE FROM Telephone_number 
            WHERE staff_id = %s;
        """, (staff_id, ))
        cursor.execute("""
            DELETE FROM Hogwarts_staff
            WHERE staff_id = %s;
        """, (staff_id, ))
        conn.commit()
        print('Все данные о преподавателе были успешно удалены.')
    else:
        print(f'Преподаватель с id = \'{staff_id}\' не найден в базе данных. Удалить данные не получится.')


def find_staff(cursor, first_name=None, last_name=None, email=None, phone_number=None):
    """ 7. Функция, позволяющая найти преподавателя по его данным (имени, фамилии, email-у или телефону). """
    print('Результаты  поиска: ')
    result = []

    if first_name:
        cursor.execute("""
            SELECT Hogwarts_staff.staff_id, first_name, last_name, email, phone_number FROM Hogwarts_staff
            FULL JOIN Telephone_number ON Hogwarts_staff.staff_id = Telephone_number.staff_id
            WHERE first_name = %s;
        """, (first_name, ))
        result += cursor.fetchall()

    elif last_name:
        cursor.execute("""
            SELECT Hogwarts_staff.staff_id, first_name, last_name, email, phone_number FROM Hogwarts_staff
            FULL JOIN Telephone_number ON Hogwarts_staff.staff_id = Telephone_number.staff_id
            WHERE last_name = %s;
        """, (last_name, ))
        result += cursor.fetchall()

    elif email:
        cursor.execute("""
            SELECT Hogwarts_staff.staff_id, first_name, last_name, email, phone_number FROM Hogwarts_staff
            FULL JOIN Telephone_number ON Hogwarts_staff.staff_id = Telephone_number.staff_id
            WHERE email = %s;
        """, (email, ))
        result += cursor.fetchall()

    elif phone_number:
        cursor.execute("""
            SELECT Hogwarts_staff.staff_id, first_name, last_name, email, phone_number FROM Hogwarts_staff
            FULL JOIN Telephone_number ON Hogwarts_staff.staff_id=Telephone_number.staff_id
            WHERE Hogwarts_staff.staff_id = (
                SELECT Hogwarts_staff.staff_id FROM Hogwarts_staff
                JOIN Telephone_number ON Hogwarts_staff.staff_id=Telephone_number.staff_id
                WHERE phone_number = %s
                );
        """, (phone_number, ))
        result += cursor.fetchall()

    if not result:
        return '- преподаватель с введенными данными в системе не найден,', '- проверьте, пожалуйста, вводимые данные.'
    else:
        return result


if __name__ == '__main__':
    try:
        with psycopg2.connect(database='Hogwarts_database', user='postgres', password='postgres') as conn:
            with conn.cursor() as cursor:
                pass

                # 0. вызов функции по удалению базы данных:
                # delete_db(cursor)

                # 1. вызов функции по созданию таблиц:
                # create_db(cursor)

                # 2. вызов функции по добавлению преподавателя:
                # add_staff(cursor, 'Albus', 'Dumbledore', 'albus_dumbledore@gryffindor.hp')
                # add_staff(cursor, 'Severus', 'Snape', 'severus_snape@slytherin.hp')
                # add_staff(cursor, 'Minerva', 'McGonagall', 'minerva_mcgonagall@gryffindor.hp')
                # add_staff(cursor, 'Filius', 'Flitwick', 'filius_flitwick@ravenclaw.hp')
                # add_staff(cursor, 'Pomona', 'Sprout', 'pomona_sprout@hufflepuff.hp')
                # add_staff(cursor, 'Remus', 'Lupin', 'remus_lupin@gryffindor.hp', 89990000006)
                # add_staff(cursor, 'Rubeus', 'Hagrid', 'rubeus_hagrid@gryffindor.hp')
                # add_staff(cursor, 'Sybill', 'Trelawney', 'sybill_trelawney@ravenclaw.hp', 89990000008)
                # add_staff(cursor, 'Gilderoy', 'Lockhart', 'gilderoy_lockhart@ravenclaw.hp', 89990000009)
                # add_staff(cursor, 'Horace', 'Slughorn', 'horace_slughorn@slytherin.hp')
                # add_staff(cursor, 'Alastor', 'Moody', 'alastor_moody@gryffindor.hp', 89990000011)

                # 3. вызов функции по добавлению номера телефона для существующего преподавателя:
                # add_phone(cursor, 1, 89999999999)
                # add_phone(cursor, 2, 89999999999)
                # add_phone(cursor, 20, 89999999999)
                # add_phone(cursor, 1, 89990000001)
                # add_phone(cursor, 2, 89990000002)
                # add_phone(cursor, 3, 89990000003)
                # add_phone(cursor, 4, 89990000004)
                # add_phone(cursor, 5, 89990000005)
                # add_phone(cursor, 6, 89990000006)
                # add_phone(cursor, 7, 89990000007)
                # add_phone(cursor, 8, 89990000008)

                # 4. вызов функции по изменению данных для существующего преподавателя:
                # change_staff(cursor, 11, first_name='Alastor Mad_Eye')
                # change_staff(cursor, 11, last_name='Mad_Eye Moody', email='alastor_mad_eye_moody@gryffindor.hp')
                # change_staff(cursor, 11, first_name='Alastor Mad_Eye', last_name='Moody',
                #              email='alastor_mad_eye_moody@gryffindor.hp', phone_number=89990000011)

                # 5. вызов функции по удалению номера телефона для существующего преподавателя:
                # delete_phone(cursor, 89999999999)

                # 6. вызов функции по удалению существующего преподавателя:
                # delete_staff(cursor, 1)

                # 7. вызов функции по поиску преподавателя по его данным (имени, фамилии, email-у или телефону):
                # print(*find_staff(cursor, first_name='Severus', last_name='Snape',
                #                   email='severus_snape@slytherin.hp', phone_number=89990000002), sep='\n')
                # print(*find_staff(cursor, first_name='Severus'), sep='\n')
                # print(*find_staff(cursor, last_name='Snape'), sep='\n')
                # print(*find_staff(cursor, email='severus_snape@slytherin.hp'), sep='\n')
                # print(*find_staff(cursor, phone_number=89990000002), sep='\n')
                # print(*find_staff(cursor, phone_number=89990000019), sep='\n')
                # print(*find_staff(cursor, phone_number=89990000003), sep='\n')

    except Exception as error:
        print(f'Ошибка при работе с PostgreSQL: {error}')

    finally:
        if conn:
            conn.close()
            print("\nСоединение с PostgreSQL закрыто.")
