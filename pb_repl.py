import sys
import phonebook as pb

class REPL:
    def __init__(self):
        self.book = pb.Phonebook() #TODO: add database
        self.valid_commands = {'retrieve': self.book.retrieve, 'add': self.book.add, 'change': self.book.change, 'lookup': self.book.lookup,
                               'remove': self.book.remove, 'help': self.help, 'exit': self.exit}
        self.expected_arg_len = {'retrieve': 1, 'add': 2, 'change': 2, 'lookup': 1, 'remove': 1, 'help':0, 'exit': 0}

    def execute(self, cmd, args):
        if cmd not in self.valid_commands:
            raise InvalidCommandError
        if len(args) != self.expected_arg_len[cmd]:
            raise InvalidCommandError(cmd, self.expected_arg_len[cmd])
        try:
            print self.valid_commands[cmd](*args)
        except KeyError:
            raise InvalidCommandError

    def run(self):
        while True:
            cmds = raw_input('> ').split(' ') #TODO: add quoted name handling
            cmd = cmds[0]
            args = cmds[1:]
            try:
                self.execute(cmd, args)
            except pb.PhonebookError as e:
                print e.msg

    def exit(self):
        print "Bye!"
        sys.exit()

    def help(self):
        return ' '.join([cmd for cmd in self.valid_commands.keys()])

class InvalidCommandError(pb.PhonebookError):
    def __init__(self, cmd=None, expected_arg_len=0):
        if cmd == '':
            self.msg = "Please enter a command"
        elif cmd is not None:
            self.msg = "%s expects %d arguments separated by spaces." % (cmd, expected_arg_len)
        else:
            self.msg = "That's not a valid command."

if __name__ == '__main__':
    repl = REPL()
    repl.run()