Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 # The proven prime

# Correct points:
# 1. Generator point (G) - guaranteed to lie on the curve
point1_x = 55066263022277343669578718895168534326250603453777594175500187360389116729240  # Gx
point1_y = 32670510020758816978083085130507043184471273380659243275938904335757337482424  # Gy

# 2. Double point G (result of ECdouble(G)) - also on the curve
point2_x = 89565891926547004231252920425935692360644145829622209833684329913297188986597
point2_y = 12158399299693830322967808612713398636155367887041628176798871954788371653930

# 3. Public key point (result of EccMultiply) - also on the curve
point3_x = 49790390825249384486033144355916864607616083520101638681403973749255924539515
point3_y = 59574132161899900045862086493921015780032175291755807399284007721050341297360

# Incorrect points:
# 1. Point with coordinates greater than Pcurve
bad_point1_x = Pcurve + 1
bad_point1_y = Pcurve + 1

# 2. Random coordinates (almost certainly not on the curve)
bad_point2_x = 12345
bad_point2_y = 67890

# 3. Zero coordinates
bad_point3_x = 0
bad_point3_y = 0

def is_point_on_curve(x, y, Pcurve=Pcurve, Bcurve=7):
    # Check if point is in field range
    if not (0 <= x < Pcurve and 0 <= y < Pcurve):
        return False
        
    # Check if point satisfies curve equation
    # y² = x³ + 7 (mod Pcurve)
    left_side = (y * y) % Pcurve
    right_side = (x * x * x + Bcurve) % Pcurve
    
    return left_side == right_side    

# Check points
print("=== Correct points ===")
print("Point G:", is_point_on_curve(point1_x, point1_y))
print("2G:", is_point_on_curve(point2_x, point2_y))
print("Public key:", is_point_on_curve(point3_x, point3_y))

print("\n=== Incorrect points ===")
print("Outside field:", is_point_on_curve(bad_point1_x, bad_point1_y))
print("Random coordinates:", is_point_on_curve(bad_point2_x, bad_point2_y))
print("Zero coordinates:", is_point_on_curve(bad_point3_x, bad_point3_y))