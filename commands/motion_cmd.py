import subprocess
from bot import command, msg

class StatusCmd(command.BotCommand):
    def run(self, dest, contents):
      output = self.process_output('motion start')

      resp = msg.BotMsg('Motion: ' + output)

      return resp

    def process_output(self, command):
      return subprocess.check_output(command.split()).decode().strip()

command_instance = StatusCmd(bindings = ['motion'], name = 'motion')
