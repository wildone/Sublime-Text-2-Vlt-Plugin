import sublime, sublime_plugin
import os

import vlt


class VltSideBarAddCommand(vlt.VltWindowCommand):
    def run(self, paths = []):
        self.run_command(['vlt', 'add'] + paths , self.scratch, 
            True, status_message="Adding...", title="Vlt Add", 
            syntax=vlt.plugin_file("syntax/Vlt Status.tmLanguage"))

    def is_enabled(self, paths = []):
        return True


class VltSideBarUpdateCommand(vlt.VltWindowCommand):
    def run(self, paths = []):
        self.run_command(['vlt', 'update'] + paths , self.scratch, 
            True, status_message="Updating...", title="Vlt Update", 
            syntax=vlt.plugin_file("syntax/Vlt Status.tmLanguage"))

    def is_enabled(self, paths = []):
        return True

        
class VltSideBarCommitCommand(vlt.VltWindowCommand):
    def run(self, paths = []):
        self.run_command(['vlt', 'commit'] + paths , self.scratch, 
            True, status_message="Commiting...", title="Vlt Commit", 
            syntax=vlt.plugin_file("syntax/Vlt Status.tmLanguage"))

    def is_enabled(self, paths = []):
        return True


class VltSideBarRemoveCommand(vlt.VltWindowCommand):
    def run(self, paths = []):
        self.run_command(['vlt', 'rm'] + paths , self.scratch, 
            True, status_message="removing...", title="Vlt Remove", 
            syntax=vlt.plugin_file("syntax/Vlt Status.tmLanguage"))

    def is_enabled(self, paths = []):
        return True
