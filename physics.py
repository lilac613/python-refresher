g = 9.81
water_density = 1000
def calculate_buoyancy(V, density_fluid):
    '''Calculates the buoyancy forced exerted an object submerged in water'''
    if V <= 0:
        raise ValueError("Volume cannot be negative!")
    if density_fluid <= 0:
        raise ValueError("The density of the fluid cannot be negative!")
    return V*density_fluid*g

def will_it_float(V, mass):
    '''Determines whether an object will float or sink in water'''
    if V <= 0:
        raise ValueError("Volume cannot be negative!")
    if mass <= 0:
        raise ValueError("Mass cannot be negative!")
    if round(mass*g,3) == round(V*g*water_density,3):
        return None
    return mass*g < V*g*water_density

def calculate_pressure(depth):
    '''Calculates pressure at a given depth in water where depth can be a positive or negative value'''
    return water_density*g*abs(depth)

