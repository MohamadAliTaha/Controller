from controller_ui import Ui_MainWindow
from useful import emergency_stop


class Controller(Ui_MainWindow):
    def __init__(self, width, height, parent=None):
        super().__init__(width=width, height=height, parent=parent)
        self.throttle = 0.50
        self.voltage = 0
        self.temps = (0, 0, 0)
        self.currents = (0, 0, 0, 0, 0, 0)
        self.velocity = [0, 0, 0, 0]
        self.commands = {
            'ctrl-p': "ping rover mcu",
            'alt-p': "ping odroid",
            'q': "emergency stop all motors",
            'l': "view key commands",
            'u': "increase throttle value",
            'i': "decrease throttle value",
        }

    def set_velocity(self, arg):
        self.velocity[arg] = self.throttle

    def reset_velocity(self, arg):
        self.velocity[arg] = 0

    def list_commands(self):
        """This method appends this program's keyboard shortcuts
        to the UI's text browser """

        for command in self.commands:
            self.log_browser.append_to_browser(
                f"'{command}': '{self.commands[command]}'")
        self.log_browser.append_to_browser("\n")

    def change_throttle(self, change):
        """Changes the current throttle value either increasing or
        decreasing and outputs the new value to the throttle label"""

        if change == "+" and not self.throttle >= 1:
            # This weird sum is done to avoid arithmetic errors when it comes to decimals in python
            self.throttle = (self.throttle * 10 + 0.50) / 10
        elif change == "-" and not self.throttle <= 0:
            self.throttle = (self.throttle * 10 - 0.50) / 10

        self.throttle_value.setText(f"{self.throttle}")

    def display_temps(self, data):
        degree = u'\N{DEGREE SIGN}'
        self.temps = tuple(str(data).split()[1::2])
        self.temp1_label.setText(f"{self.temps[0]} {degree}C")
        self.temp2_label.setText(f"{self.temps[1]} {degree}C")
        self.temp3_label.setText(f"{self.temps[2]} {degree}C")

    def display_currents(self, data):
        self.currents = tuple(data.effort)

        self.r_front_current.setText(f"{self.currents[0]}")
        self.r_mid_current.setText(f"{self.currents[1]}")
        self.r_back_current.setText(f"{self.currents[2]}")
        self.l_front_current.setText(f"{self.currents[3]}")
        self.l_mid_current.setText(f"{self.currents[4]}")
        self.l_back_current.setText(f"{self.currents[5]}")

    def display_voltage(self, data):
        self.voltage = data.data
        self.voltage_label.setText(f"{self.voltage} V")

    def start_handling_clicks(self):
        """This method is for grouping all button click methods for 
        the Rover Controller Page"""

        self.list_commands_button.clicked.connect(self.list_commands)
        self.stop_button.clicked.connect(emergency_stop)

        self.controller_up.pressed.connect(lambda: self.set_velocity(0))
        self.controller_up.released.connect(lambda: self.reset_velocity(0))

        self.controller_right.pressed.connect(lambda: self.set_velocity(1))
        self.controller_right.released.connect(lambda: self.reset_velocity(1))

        self.controller_down.pressed.connect(lambda: self.set_velocity(2))
        self.controller_down.released.connect(lambda: self.reset_velocity(2))

        self.controller_left.pressed.connect(lambda: self.set_velocity(3))
        self.controller_left.released.connect(lambda: self.reset_velocity(3))