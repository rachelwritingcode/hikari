#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © Nekoka.tt 2019
#
# This file is part of Hikari.
#
# Hikari is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hikari is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Hikari. If not, see <https://www.gnu.org/licenses/>.
"""
The ORM fabric. This is a reusable dataclass that is passed to all major
components and provides access to the entire object graph for all functional
and data components that are being managed by the application.
"""
from __future__ import annotations

import dataclasses

import typing

from hikari.net import gateway
from hikari.orm import event_handler as _event_handler
from hikari.orm import state_registry as _state_registry


@dataclasses.dataclass()
class Fabric:
    """
    Wraps all major API components together into one main component that can be passed
    around freely.
    """

    #: The handler for incoming events. This is expected to parse the raw event payloads that
    #: Discord provides.
    event_handler: _event_handler.IEventHandler = NotImplemented

    #: Application state information. This stores information about any users the application
    #: can see, any guilds it is in, any channels that are available, and the likes.
    state_registry: _state_registry.IStateRegistry = NotImplemented

    #: A mapping of shard ID's to gateways that are running.
    #:
    #: If no shards are running, then this defaults to one shard under the `None` key.
    gateways: typing.Dict[typing.Optional[int], gateway.GatewayClientV7] \
        = dataclasses.field(default_factory=dict)