import subprocess
from bot import command, msg

class MotionCmd(command.BotCommand):
    def run(self, dest, contents):
        print "Motion contents:"
        print contents
        if len(contents) < 2 or len(contents) >= 3:
			return msg.BotMsg('Usage: .motion [start | stop]')

      output = self.process_output('motion ' + cmd)

      resp = msg.BotMsg('Motion: ' + cmd)

      return resp

    def process_output(self, command):
      return subprocess.check_output(command.split()).decode().strip()

command_instance = StatusCmd(bindings = ['motion'], name = 'motion')
