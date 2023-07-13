def calculate_buoyancy(v, density_fluid):
    '''Calculates the buoyancy forced exerted an object submerged in water'''
    if v<0:
        raise ValueError("Volume cannot be negative!")
    if density_fluid < 0:
        raise ValueError("The density of the fluid cannot be negative!")
    return v*density_fluid*9.81

def will_it_float(v, mass):
    '''Determines whether an object will float or sink in water'''
    if v < 0:
        raise ValueError("Volume cannot be negative!")
    if mass < 0:
        raise ValueError("Mass cannot be negative!")
    if round(mass*9.81,3) == round(v*9.81*1000,3):
        return None
    return mass*9.81 < v*9.81*1000

def calculate_pressure(depth):
    '''Calculates pressure at a given depth in water'''
    return 1000*9.81*abs(depth)

