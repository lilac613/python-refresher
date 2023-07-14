import numpy as np

g = 9.81
water_density = 1000
pressure_at_surface = 101325 #kiloPascals

def calculate_buoyancy(V, density_fluid):
    '''Calculates the buoyancy forced exerted an object submerged in water'''
    if V <= 0 or density_fluid<=0:
        raise ValueError("Invalid values!")
    buoyancy = V*density_fluid*g
    return buoyancy

def will_it_float(V, mass):
    '''Determines whether an object will float or sink in water'''
    if V <= 0 or mass<=0:
        raise ValueError("Invalid values!")
    gravitational_force = mass*g
    buoyant_force = V*g*water_density
    if round(gravitational_force,3) == round(buoyant_force,3):
        return None
    return gravitational_force < buoyant_force

def calculate_pressure(depth):
    '''Calculates pressure at a given depth in water where depth can be a positive or negative value'''
    pressure = water_density*g*abs(depth) + pressure_at_surface
    return pressure

def calculate_acceleration(F,m):
    '''Calculates the acceleration of an object given the force 
    applied to its mass'''
    if m<=0:
        raise ValueError("Invalid values!")
    acceleration = F/m
    return acceleration

def calculate_angular_acceleration(tau, I):
    '''Calculates the angular acceleration of an object 
    given torque applied to it and its moment of inertia'''
    if I <= 0:
        raise ValueError("Invalid values!")
    return tau/I

def calculate_torque(F_magnitude,F_direction_degrees,r):
    '''Calculates the torque applied to an object given the force applied
    to it and the distance from the axis of rotation to the point where the
    force is applied'''
    if F_magnitude<=0 or r<=0:
        raise ValueError("Invalid values!")
    F_direction_radians = (F_direction_degrees*np.pi)/180
    torque = F_magnitude*np.sin(F_direction_radians)*r
    return torque

def calculate_moment_of_inertia(m,r):
    '''Calculates the moment of inertia of an object given its mass and
    the distance from the axis of rotation to the center of mass of the object'''
    if m<=0 or r<=0:
        raise ValueError("Invalid values!")
    moment_of_inertia = m*(r**2)
    return moment_of_inertia

def calculate_auv_acceleration(F_magnitude, F_angle_radians, mass=100, volume=0.1, thruster_distance=0.5):
    '''Calculates the acceleration of the AUV in the 2D plane'''
    if F_magnitude<=0 or mass<=0 or volume<=0 or thruster_distance <=0:
        raise ValueError("Invalid value for the magnitude of force!")
    F_x = F_magnitude*np.cos(F_angle_radians)
    acceleration_x = calculate_acceleration(F_x,mass)
    F_y = F_magnitude*np.sin(F_angle_radians)
    acceleration_y = calculate_acceleration(F_y,mass)
    net_acceleration = np.array([acceleration_x,acceleration_y])
    return net_acceleration
    
def calculate_auv_angular_acceleration(F_magnitude,F_angle_radians,inertia=1,thruster_distance=0.5):
    '''Calculates the angular acceleration of the AUV'''
    if F_magnitude <=0 or inertia <=0 or thruster_distance <= 0:
        raise ValueError("Invalid values!")
    perpendicular_force = F_magnitude*np.sin(F_angle_radians)
    angular_acceleration = calculate_angular_acceleration(perpendicular_force*thruster_distance,inertia)
    return angular_acceleration

def calculate_auv2_acceleration(T, alpha, theta, mass):
    '''Calculates the acceleration of the AUV in the 2D plane'''
    if mass <= 0:
        raise ValueError("Invalid values!")
    # reference frame of ROV
    components = np.array([[np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
                               [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)]])
    net_force_prime = np.matmul(components,T)

    # global reference frame
    rotation_matrix = np.array([[np.cos(theta),-np.sin(theta)],
                                [np.sin(theta),np.cos(theta)]])
    net_force = np.matmul(rotation_matrix,net_force_prime)
    acceleration_x = net_force[0]/mass
    acceleration_y = net_force[1]/mass
    net_acceleration = np.array([acceleration_x,acceleration_y])
    return net_acceleration

def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    '''Calculates the angular acceleration of the AUV'''
    if L<=0 or l<=0 or inertia<=0:
        raise ValueError("Invalid values!")
    components = np.array([[L*np.sin(alpha)+l*np.cos(alpha)],
                           [-L*np.sin(alpha)+l*np.cos(alpha)]
                           [L*np.sin(alpha)+l*np.cos(alpha)]
                           [-L*np.sin(alpha)+l*np.cos(alpha)]])
    net_torque = np.matmul(components,T)
    angular_acceleration = net_torque/inertia
    return angular_acceleration