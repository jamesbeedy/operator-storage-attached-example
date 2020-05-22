#!/usr/bin/env python3
import sys
sys.path.append('lib')

import logging

from ops.charm import CharmBase
from ops.framework import Object, StoredState
from ops.main import main


logger = logging.getLogger()


class FooStoredStateCharm(CharmBase):
    """This charm demonstrates using framework.StoredState
    to persist data between hook invocations.
    """

    _stored = StoredState()

 
    def __init__(self, *args):
        super().__init__(*args)

        # Initialize the stored state.
        self._stored.set_default(foo="INIT")
        self.framework.observe(self.on.foo, self._on_foo)

        self.framework.observe(self.on.start, self._on_start)
        self.framework.observe(self.on.install, self._on_install)
        self.framework.observe(self.on.update_status, self._on_update_status)

    def _on_start(self, event):
        logger.info(f"LOGGING {event.uuid}: ON_INSTALL - {self._stored.foo}")
        self._stored.foo = "ON START"

    def _on_install(self, event):
        logger.info(f"LOGGING {event.uuid}: ON_INSTALL - {self._stored.foo}")
        self._stored.foo = "ON INSTALL"

    def _on_update_status(self, event):
        logger.info(f"LOGGING {event.uuid}: ON_UPDATE_STATUS - {self._stored.foo}")
        self._stored.foo = "ON UPDATE_STATUS"

    def _on_foo(self, event):
        logger.info(f"LOGGING {event.uuid}: ON_FOO - {self._stored.foo")


if __name__ == "__main__":
    main(FooStoredStateCharm)
