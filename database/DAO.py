from database.DB_connect import DBConnect
from model.country import Country

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_allCountries():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """select * from country """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Country(row["StateAbb"], row["CCode"], row["StateNme"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_confini(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """select* from contiguity c where year<=%s order by state1no """
        cursor.execute(query,(year,))
        result = []
        for row in cursor:
            result.append((row["state1no"],row["state2no"],row["conttype"]))
        cursor.close()
        conn.close()
        return result

