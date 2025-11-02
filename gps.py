import math

# WGS84 Ellipsoid constants
a = 6378137.0          # semi-major axis (meters)
e2 = 6.69437999014e-3    # eccentricity squared

def ecef_to_geodetic(x, y, z):
    # Longitude
    lon = math.atan2(y, x)

    # Distance from Earth's rotation axis
    r = math.sqrt(x*x + y*y)

    # Initial latitude estimate
    lat = math.atan2(z, r * (1 - e2))

    # Iterative refinement of latitude
    for _ in range(5):
        N = a / math.sqrt(1 - e2 * math.sin(lat)**2)
        h = r / math.cos(lat) - N
        lat = math.atan2(z, r * (1 - e2 * (N/(N + h))))

    # Final calculations
    N = a / math.sqrt(1 - e2 * math.sin(lat)**2)
    h = r / math.cos(lat) - N

    # Convert to degrees
    lat_deg = math.degrees(lat)
    lon_deg = math.degrees(lon)

    return lat_deg, lon_deg, h


# ----------- USER INPUT -------------
x = float(input("Enter X coordinate (meters): "))
y = float(input("Enter Y coordinate (meters): "))
z = float(input("Enter Z coordinate (meters): "))

lat, lon, alt = ecef_to_geodetic(x, y, z)

print("\nConverted Geographical Coordinates:")
print(f"Latitude:  {lat:.8f}°")
print(f"Longitude: {lon:.8f}°")
print(f"Altitude:  {alt:.3f} meters")
