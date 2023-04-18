from user import User
from route import Route
from vehicles.passenger_car import PassengerCar
from vehicles.cargo_van import CargoVan


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f'{driving_license_number} has already been registered to our platform.'
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)

        return f'{first_name} {last_name} was successfully registered under DLN-{driving_license_number}'

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ('PassengerCar', 'CargoVan'):
            return f'Vehicle type {vehicle_type} is inaccessible.'
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f'{license_plate_number} belongs to another vehicle.'
        if vehicle_type == "PassengerCar":
            new_vehicle = PassengerCar(brand, model, license_plate_number)
        else:
            new_vehicle = CargoVan(brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)

        return f'{brand} {model} was successfully uploaded with LPN-{license_plate_number}.'

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f'{start_point}/{end_point} - {length} km had already been added to our platform.'
                elif route.length < length:
                    return f'{start_point}/{end_point} shorter route had already been added to our platform.'
                else:
                    route.is_locked = True
                    new_route = Route(start_point, end_point, length, len(self.routes) + 1)
                    self.routes.append(new_route)
                    return f'{start_point}/{end_point} - {length} km is unlocked and available to use.'
        new_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(new_route)

        return f'{start_point}/{end_point} - {length} km is unlocked and available to use.'

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user = None
        for curr_user in self.users:
            if curr_user.driving_license_number == driving_license_number:
                user = curr_user
                break

        if user.is_blocked:
            return f'User {driving_license_number} is blocked in the platform! This trip is not allowed.'

        vehicle = None
        for curr_v in self.vehicles:
            if curr_v.license_plate_number == license_plate_number:
                vehicle = curr_v
                break

        if vehicle.is_damaged:
            return f'Vehicle {license_plate_number} is damaged! This trip is not allowed.'

        route = None
        for curr_route in self.routes:
            if curr_route.route_id == route_id:
                route = curr_route
                break

        if route.is_locked:
            return f'Route {route_id} is locked! This trip is not allowed.'

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.rating -= 1
        else:
            user.rating += 1

        status = 'Damaged' if vehicle.is_damaged else 'OK'
        return f'{vehicle.brand} {vehicle.model} License plate: {vehicle.license_plate_number} Battery: {vehicle.battery_level}% Status: {status}'

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted([vehicle for vehicle in self.vehicles if vehicle.is_damaged],
                                  key=lambda vehicle: (vehicle.brand, vehicle.model))
        count = min(count, len(damaged_vehicles))
        for vehicle in damaged_vehicles[:count]:
            vehicle.repair()
            vehicle.recharge()
        count_of_repaired_vehicles = len(damaged_vehicles[:count])

        return f'{count_of_repaired_vehicles} vehicles were successfully repaired!'

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda user: user.rating, reverse=True)
        report = '*** E-Drive-Rent ***\n'
        for user in sorted_users:
            report += f'{user}\n'
        return report