import requests

URL = "http://127.0.0.1:5000/vehicles/"
SAMPLE_VEHICLE = {
    "color":"red",
    "license_plate":"7777",
    "v_type": "Car",
    "owner_id": "Maira"
}

def create_vehicle(color, license_plate, v_type,owner_id):
    vehicle_data = SAMPLE_VEHICLE
    vehicle_data ["color"]= color
    vehicle_data ["license_plate"]= license_plate
    vehicle_data ["v_type"]= v_type
    vehicle_data ["owner_id"] = owner_id
    response = requests.post(URL, json = vehicle_data)
    if response.status_code == 204:
        print("Successfully created new vehicle.")
    else:
        print ("Something went wrong while trying to create a vehicle")

if __name__ == "__main__":
    color = input("Enter a color:")
    license_plate = input("Enter a llicense plate:")
    v_type = input("Enter a vehicle type:")
    owner_id = int((input("Enter a owner id:")))
    create_vehicle(color, license_plate, v_type,owner_id)