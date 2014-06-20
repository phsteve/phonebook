#valid_commands = {'create': create, 'lookup': lookup, 'add': add, 'change': change}

class Entry(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __eq__(self, other):
        #do i need this?
        return (self.name == other.name and self.number == other.number)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return ": ".join([self.name, str(self.number)])

    def change(self, new_number):
        self.number = new_number


class Phonebook(object):
    def __init__(self):
        self.entries = {}

    def names(self):
        #private?
        return self.entries.keys()

    def retrieve(self, exact_name):
        #private?
        #Retrieves one entry with an exact match on exact_name
        try:
            return self.entries[exact_name]
        except KeyError:
            raise NameNotFoundError

    def add(self, name, number):
        entry = Entry(name, number)
        if entry.name in self.names():
            raise DuplicateNameError(entry.name)
        self.entries[entry.name] = entry
        return "Added " + str(entry)

    def change(self, name, new_number):
        entry = self.retrieve(name)
        entry.change(new_number)
        return "Changed %s to %s" % (entry.name, entry.number)

    def lookup(self, substring):
        #Retrieves all entries that have substring as a substring of their name
        found_entries = [str(self.retrieve(name)) for name in self.names() if substring in name]
        if not found_entries:
            return "No results found for %s" % substring
        return "\n".join(found_entries)

    def remove(self, exact_name):
        entry = self.retrieve(exact_name)
        del self.entries[entry.name]
        return "%s's entry removed." % (exact_name)

class PhonebookError(Exception):
    pass

class DuplicateNameError(PhonebookError):
    def __init__(self, name):
        self.msg = "%s already exists in the phonebook!" % name

class NameNotFoundError(PhonebookError):
    def __init__(self):
        self.msg = "That name doesn't exist in the phonebook."


