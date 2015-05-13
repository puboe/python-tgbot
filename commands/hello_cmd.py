from bot import command, msg

class HelloCmd(command.BotCommand):
	def run(self, dest, contents, passphrase):
		return msg.BotMsg('Hello there.')


command_instance = HelloCmd(bindings = ['hello'], name = 'hello')
