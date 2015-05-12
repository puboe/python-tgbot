import subprocess
from bot import command, msg

class MotionCmd(command.BotCommand):
    def run(self, dest, contents):
        print ('Motion contents:')
        print (contents)
        if len(contents) < 2:
            return msg.BotMsg('Usage: .motion [start | stop]')


        cmd = contents[1]
        output = self.process_output('motion ' + cmd)
        resp = msg.BotMsg('Motion: ' + cmd)
        return resp

    def process_output(self, command):
        return subprocess.check_output(command.split()).decode().strip()

command_instance = MotionCmd(bindings = ['motion'], name = 'motion')
