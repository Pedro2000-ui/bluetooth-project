import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QWidget, QVBoxLayout
from PyQt5.QtBluetooth import QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo

class BluetoothWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dispositivos Bluetooth')
        self.layout = QVBoxLayout()

        # Lista para exibir os dispositivos encontrados
        self.device_list = QListWidget()

        self.layout.addWidget(self.device_list)
        self.setLayout(self.layout)

        # Inicializa o agente de descoberta de dispositivos Bluetooth
        self.discovery_agent = QBluetoothDeviceDiscoveryAgent()
        self.discovery_agent.deviceDiscovered.connect(self.device_discovered)

        # Define o range de busca para os dispositivos próximos
        self.discovery_agent.setInquiryType(QBluetoothDeviceDiscoveryAgent.GeneralUnlimitedInquiry)

        # Inicia a descoberta de dispositivos Bluetooth
        self.discovery_agent.start()

    def device_discovered(self, info: QBluetoothDeviceInfo):
        # Obtem a intensidade do sinal do dispositivo
        rssi = info.rssi()

        # Filtro de proximidade: apenas dispositivos com sinal forte o suficiente
        if rssi > -2000:  # Ajuste este valor conforme necessário para o seu caso
            # Adiciona o dispositivo encontrado à lista
            device_name = info.name()
            self.device_list.addItem(device_name)

def main():
    app = QApplication(sys.argv)
    window = BluetoothWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
