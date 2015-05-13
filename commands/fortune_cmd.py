import subprocess
from bot import command, msg

class MotionCmd(command.BotCommand):
    def run(self, dest, contents, passphrase):

        output = self.process_output('fortune')
        resp = msg.BotMsg(output)
        return resp

    def process_output(self, command):
        return subprocess.check_output(command.split()).decode().strip()

command_instance = MotionCmd(bindings = ['f', "fortune"], name = 'fortune')
