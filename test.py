from zte.olt import Olt
from zte.command import CustomCommand


def main():
    # set balid host, usrname and password
    olt = Olt('host', 'username', 'password')
    # insert valid parameter to register command
    register = CustomCommand.register_ont()
    olt.connect()
    olt.send_command(register)
    
