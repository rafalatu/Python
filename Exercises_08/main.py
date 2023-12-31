from devices import Firewall

# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()

# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

from devices import Load_balancers

# Create a firewall instance
load_balancers27 = Load_balancers("load_balancers")
# Configure it
load_balancers27.configure_load_balancers()

# Create a firewall instance
load_balancers28 = Load_balancers("load_balancers28")
# Verify a CRC
load_balancers28.calculate_crc("dummy data")

from devices import Switches

# Create a firewall instance
switches27 = Switches("switches27")
# Configure it
switches27.configure_switches()

# Create a firewall instance
switches28 = Switches("switches28")
# Verify a CRC
switches28.calculate_crc("dummy data")