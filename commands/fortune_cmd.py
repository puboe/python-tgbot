import subprocess
from bot import command, msg

class FortuneCmd(command.BotCommand):
    def run(self, dest, contents, passphrase):


        output = self.process_output('fortune -n 110 -s')#.split('\n')
        print(output)

        resp = msg.BotMsg(output)
        #for x in list(range(1,len(output))):
        #    print (x)
        #    resp.add_line(output[x])

        return resp

    def process_output(self, command):
        return subprocess.check_output(command.split()).decode().strip()

command_instance = FortuneCmd(bindings = ['f', "fortune"], name = 'fortune')
