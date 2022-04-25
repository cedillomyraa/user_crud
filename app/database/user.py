from app.database import get_db

def output_formatter(results):#squilite returns tuples not list tuples are not mutable 
    out= [] #empty list
    for result in results: #for each loop #results is a tuple of tuples 
        result_dict = {
            "id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "hobbies": result[3],
            "active": result[4]
        }
        out.append(result_dict)
    return out

def insert(user_dict):
    value_tuple = (
        user_dict.get("first_name"),
        user_dict.get("last_name"),
        user_dict.get("hobbies")
    )
    statment = """
        INSERT INTO user(
            first_name,
            last_name,
            hobbies
        )VALUES (?, ?, ?)     
    """
#? are place holders that will be specified 
    cursor = get_db()
    cursor.execute(statment, value_tuple)
    cursor.commit()    
    cursor.close()

def scan():
    cursor = get_db().execute("SELECT * FROM user WHERE active=1", ())
    results = cursor.fetchall()   
    cursor.close()
    return output_formatter(results)

def select_by_id(pk):#pk = primary key
    cursor = get_db()
    cursor.execute("SELECT * FROM user WHERE active=1", (pk,))
    results = cursor.fetchall()   
    cursor.close()
    return output_formatter(results)

def update(pk, user_data):
    value_tuple = (
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        pk
    )
    statment = """
        UPDATE user
        SET first_name=?,
        last_name=?,
        hobbies=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(statment, value_tuple)
    cursor.commit()    
    cursor.close()    


