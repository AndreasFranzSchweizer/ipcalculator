import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout

def get_user_input():
    # get user input
    userInput = ip_input_field.text() or "192.168.0.1/24"
    # split address and mask
    userInputParts = userInput.split("/")
    ipInput = userInputParts[0]
    maskInput = int(userInputParts[1])

    return ipInput, maskInput

# Funktion, um eine 32-Bit-Integer-Adresse in DDN-Format umzuwandeln
def get_ddn_string(address):
    bytes = [0, 0, 0, 0]
    bytes[0] = address >> 24 & 0xff
    bytes[1] = address >> 16 & 0xff
    bytes[2] = address >> 8 & 0xff
    bytes[3] = address & 0xff
    return ".".join(str(item) for item in bytes)


def calculate_network_info():
    ip, subnet_size = get_user_input()
    ip = get_int_from_ip(ip)
    mask = generate_subnet_mask(subnet_size)

    # Berechne die Netzwerkinformationen
    network = ip & mask
    broadcast = ip | ~mask

    # Aktualisiere die Labels mit den Ergebnissen
    ip_ddn_label.setText(f"IP DDN format: {get_ddn_string(ip)}")
    network_ddn_label.setText(f"Network address DDN format: {get_ddn_string(network)}")
    broadcast_ddn_label.setText(f"Broadcast address DDN format: {get_ddn_string(broadcast)}")
    first_host_ddn_label.setText(f"First host address DDN format: {get_ddn_string(network+1)}")
    last_host_ddn_label.setText(f"Last host address DDN format: {get_ddn_string(broadcast-1)}")


def get_int_from_ip(ddn_string):
    octets = ddn_string.split(".")

    if len(octets) != 4:
        exit()

    ip = int(octets[0]) << 24
    ip += int(octets[1]) << 16
    ip += int(octets[2]) << 8
    ip += int(octets[3])

    return ip


def generate_subnet_mask(size):
    if size > 32 or size < 1:
        exit()

    mask = 2 ** int(size) - 1
    mask = mask << (32 - size)

    return mask


# Erstelle die GUI
app = QApplication(sys.argv)
app.aboutQt()

# Erstelle das Haupt-Widget
window = QWidget()
window.setWindowTitle("IP Rechner")

# Erstelle ein vertikales Layout für das Haupt-Widget
layout = QVBoxLayout()
window.setLayout(layout)

# Erstelle das FormLayout
form_layout = QFormLayout()

# Erstelle das Label und das Textfeld für die IP-Adresse
ip_label = QLabel("IP-Adresse (CIDR-Format):")
ip_input_field = QLineEdit("192.168.0.1/24")

# Füge das Label und das Textfeld zum FormLayout hinzu
form_layout.addRow(ip_label, ip_input_field)

# Füge das FormLayout zum Haupt-Layout hinzu
layout.addLayout(form_layout)

# Erstelle den Berechnen-Button
calculate_button = QPushButton("Berechnen")
calculate_button.clicked.connect(calculate_network_info)

# Füge den Button zum Haupt-Layout hinzu
layout.addWidget(calculate_button)

# Erstelle die restlichen Labels
ip_ddn_label = QLabel()
network_ddn_label = QLabel()
broadcast_ddn_label = QLabel()
first_host_ddn_label = QLabel()
last_host_ddn_label = QLabel()

# Füge die Labels zum Haupt-Layout hinzu
layout.addWidget(ip_ddn_label)
layout.addWidget(network_ddn_label)
layout.addWidget(broadcast_ddn_label)
layout.addWidget(first_host_ddn_label)
layout.addWidget(last_host_ddn_label)

window.show()
sys.exit(app.exec_())