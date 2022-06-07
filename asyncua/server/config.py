from dataclasses import dataclass, field
from datetime import timedelta


@dataclass
class ServerLimits:
    # Session Settings
    #: the maxium count of sessions
    MaxSessionCount: int = 1000
    #: The max timeout for a session, clients can request shorter timeouts
    MaxSessionTime: timedelta = field(default_factory=timedelta(seconds=12))
    #: The min timeout for a session, clients can request longer timeouts
    MinSessionTimeout: timedelta = field(default_factory=timedelta(seconds=1))
    # Secure Channel Settings
    #: the maxium count of connections
    MaxConnectionsCount: int = 1000
    #: The max lifetime of a secure channel, clients can request shorter timeouts
    MaxSecureChannelLifeTime: timedelta = field(default_factory=timedelta(minutes=60))
    #: The min lifetime of a secure channel, clients can request longer timeouts
    MinSecureChannelLifeTime: timedelta = field(default_factory=timedelta(minutes=1))
