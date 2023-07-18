import numpy as np
import matplotlib.pyplot as plt

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
    moment_of_inertia = m*np.power(r,2)
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

def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    '''Calculates the acceleration of the AUV in the 2D plane'''
    if type(T) != np.ndarray:
        raise TypeError("T has to be an ndarray!")
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
    if type(T) != np.ndarray:
        raise TypeError("T has to be an ndarray!")
    if L<=0 or l<=0 or inertia<=0:
        raise ValueError("Invalid values!")
    components = np.array([L*np.sin(alpha)+l*np.cos(alpha),
                           -L*np.sin(alpha)-l*np.cos(alpha),
                           L*np.sin(alpha)+l*np.cos(alpha),
                           -L*np.sin(alpha)-l*np.cos(alpha)])
    net_torque = np.matmul(components,T)
    angular_acceleration = calculate_angular_acceleration(net_torque,inertia)
    return angular_acceleration

def simulate_auv2_motion(T, alpha, L, l, mass=100, inertia=100, dt=0.1, t_final=10, x0=0, y0=0, theta0=0):
    '''Simulates the motion of the AUV in the 2D plane'''
    time = np.arange(0,t_final,dt)
    x = np.zeros_like(time) 
    x[0] = x0
    y = np.zeros_like(time)
    y[0] = y0
    theta = np.zeros_like(time)
    theta[0] = theta0
    v = np.zeros(shape=(len(time),2))
    omega = np.zeros_like(time)
    linear_acceleration = np.zeros(shape=(len(time),2))
    angular_acceleration = np.zeros_like(time) 
    for i in range(1,len(time)):
        angular_acceleration[i] = calculate_auv2_angular_acceleration(T,alpha,L,l,inertia)
        omega[i] = omega[i-1] + angular_acceleration[i-1]*dt
        theta[i] = np.mod(theta[i-1] + omega[i]*dt,(2*np.pi))

        linear_acceleration[i][0] = calculate_auv2_acceleration(T,alpha,theta[i],mass)[0]
        linear_acceleration[i][1] = calculate_auv2_acceleration(T,alpha,theta[i],mass)[1]
        v[i][0] = v[i-1][0] + linear_acceleration[i][0]*dt
        v[i][1] = v[i-1][1] + linear_acceleration[i][1]*dt
        x[i] = x[i-1] + v[i][0]*dt
        y[i] = y[i-1] + v[i][1]*dt

        
    ret = (time,x,y,theta,v,omega,linear_acceleration)
    return ret

def plot_auv2_motion(t, x, y, theta, v, omega, a):
    '''Plots the motion of the AUV in the 2D plane'''
    plt.plot(t, x, label="X-Position")
    plt.plot(t, y, label="Y-Position")
    plt.plot(t, theta, label="Angular Displacement")
    vx = np.zeros_like(t)
    vy = np.zeros_like(t)
    ax = np.zeros_like(t)
    ay = np.zeros_like(t)
    for i in range(0,len(v)):
        vx[i] = v[i][0]
        vy[i] = v[i][1]
        ax[i] = a[i][0]
        ay[i] = a[i][1]
    plt.plot(t,omega,label="Angular velocity")
    plt.plot(t,vx,label="X-Velocity")
    plt.plot(t,vy,label="Y-Velocity")
    plt.plot(t,ax,label="X-Acceleration")
    plt.plot(t,ay,label="Y-Acceleration")
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m), Velocity (m/s), Acceleration (m/s^2)")
    plt.legend()
    plt.show()

(time, x, y, theta, v, omega, a) = simulate_auv2_motion(np.array([10,0,0,0]),np.pi/4,8,6,100,100,3)
plot_auv2_motion(time, x, y, theta, v, omega, a)