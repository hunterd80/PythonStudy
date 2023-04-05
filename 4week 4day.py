# import theater_module as mv

# # theater_module.price(3)

# # theater_module.price_morning(4)

# # theater_module.price_soldier(3)

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price_soldier as price
price(5)

# import travel.thailand

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage

# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *

# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()