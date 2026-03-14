# Used an if-elif-else chain to ensure mutually exclusive conditions.
# This allows for short-circuiting (early exit) and better CPU efficiency.
distance_mi = 0
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
elif distance_mi <= 1 and not is_raining:
    print(True)
elif (distance_mi > 1 and distance_mi <= 6) and (has_bike and not is_raining):
    print(True)
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print(True)
else:
    print(False)
