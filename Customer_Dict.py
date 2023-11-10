from random import randint
from faker import Faker

# Generate dynamic random account numbers
gen_numbers = [''.join(str(randint(0, 9)) for x in range(10)) for m in range(10)]
# Generate dynamic names
gen_names = [Faker().name() for x in range(10)]
# Generate dynamic amounts
gen_amounts = [float(randint(0, 1000)) for x in range(10)]
# Generate dynamic pin
gen_pins = [str(randint(1000, 9000)) for x in range(10)]