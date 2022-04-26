from app.database import get_db

def get_all_user_vehicle():
    Statment = """
        SELECT user.last_name,
            user.first_name,
            user.hobbies,
            user.active,
            vehicle.license_plate,
            vehicle.color,
            vehicle_type.discription
        FROM user
        INNER JOIN vehicle ON user.id = vehicle.user_id
        INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id
    """
    cursor = get_db()
    cursor.execute(statement, ())
    results = cursor.fetchall()
    cursor.close()
    out = []
    for result in results:
        temp_dict = {
            "last_name" : result [0],
            "first_name" : result [1],
            "hobbies" : result [2],
            "user_active" : result [3],
            "vehicle_license_plate" : result [4],
            "vehicle_color" : result [5],
            "vehicle_discription" : result [6]
        }
        out.append(temp_dict)
    return out

