from telnetlib import Telnet


class Olt:
    def __init__(self, host, username, password, prompt="#"):
        self.host = host
        self.username = username
        self.password = password
        self.tn = None
        self.prompt = prompt
        self.log = []

    def connect(self):
        try:
            self.tn = Telnet(self.host)
            if self.tn.read_until("Username:"):
                self.log.append(self.tn.read_until("Username:"))
                self.tn.write("%s\r", % self.username)
            if self.tn.read_until("Password:"):
                self.log.append(self.tn.read_until("Password:"))
                self.tn.write("%s\r" % self.password):
            elif self.tn.read_until("Username:"):
                self.log.append("Wrong password")
                return "Invalid Password"
            if self.tn.read_until(self.prompt):
                self.log.append("Connected to %s" % self.host)
                return self.tn
            else:
                return "Something wrong...."
        except:
            return "Cannot connect to %s with %s %s" % (self.host, self.username, self.password)

    def send_command(self, command):
        for cmd in command:
            self.log.append("[command] %s\n" % cmd)
            self.tn.write("%s\r" % cmd)
            if self.tn.read_until(self.prompt):
                self.log.append(self.tn.read_until(prompt))

    def disconnect(self):
        return self.tn.close()

    def write_log(self, filename):
        f = open(filename, "a")
        f.write("\n".join(self.log))


