from collections import OrderedDict

from cloudshell.cli.service.command_mode import CommandMode
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.cli.session.telnet_session import TelnetSession
from cloudshell.networking.cisco.cli.cisco_cli_handler import CiscoCliHandler
from cloudshell.networking.cisco.cli.cisco_command_modes import EnableCommandMode, \
    DefaultCommandMode, ConfigCommandMode


ConfigCommandMode.ENTER_COMMAND = "configure"


class L1EnableCommandMode(EnableCommandMode):
    def enter_action_map(self):
        return OrderedDict()


class CiscoL1CliHandler(CiscoCliHandler):
    REGISTERED_SESSIONS = (
        SSHSession,
        TelnetSession,
    )

    def __init__(self, resource_config, logger):
        super(CiscoL1CliHandler, self).__init__(None, resource_config, logger)
        ConfigCommandMode.ENTER_COMMAND = "configure"

    @property
    def enable_mode(self):
        return self.modes[L1EnableCommandMode]

    def _on_session_start(self, session, logger):
        pass


CommandMode.RELATIONS_DICT = {
    DefaultCommandMode: {L1EnableCommandMode: {ConfigCommandMode: {}}}
}
