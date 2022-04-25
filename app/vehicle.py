from unittest import result
from app.database import get_db

def output_formatter(results):
    out = []
    for result in results: 
        result_dict = {
            "id": result[0],
            "color": result[1],
            "license_plate": result[2],
            "v_type": result[3],
            "owner_id": result[4],
            "active": result[5]  
        }
        out.append(result_dict)
    return out

def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict.get("color"),
        vehicle_dict.get("licence_plate"),
        vehicle_dict.get("v_trype"),
        vehicle_dict.get("owner_id")
    )
    statment = """
        INSERT INTO vehicle(
            color,
            licence_plate,
            v_type,
            owner_id
        )VALUES (?, ?, ?)     
    """
#? are place holders that will be specified 
    cursor = get_db()
    cursor.execute(statment, value_tuple)
    cursor.commit()    
    cursor.close()

def scan():
    cursor =get_db().execute("SELECT FROM vehicle WHERE active=1",())
    result = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id(pk):
    cursor =get_db().execute("SELECT FROM vehicle WHERE id=?",())
    result = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data.get("color"),
        vehicle_data.get("licence_plate"),
        vehicle_data.get("v_trype"),
        vehicle_data.get("owner_id"),
        pk
    )

    statment = """
        UPDATE vehicle
            SET color,
            licence_plate =?,
            v_type =?,
            WHERE id=?    
    """
    cursor = get_db()
    cursor.execute(statment, value_tuple)
    cursor.commit()    
    cursor.close()

def deactivate(pk):
    cursor =get_db()
    statment = """
        UPDATE vehicle
        SET active
        WHERE id=?
    """
    cursor.execute(statment, (pk,))
    cursor.commit()    
    cursor.close()




