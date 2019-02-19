#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Orion Poplawski <orion@nwra.com>
# Copyright: (c) 2018, Frederic Bor <frederic.bor@wanadoo.fr>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
---
module: pfsense_rule
version_added: "2.8"
author: Orion Poplawski (@opoplawski), Frederic Bor (@f-bor)
short_description: Manage pfSense rules
description:
  - Manage pfSense rules
notes:
options:
  name:
    description: The name the rule
    required: true
    default: null
  action:
    description: The action of the rule
    required: true
    default: pass
    choices: [ "pass", "block", "reject" ]
  state:
    description: State in which to leave the rule
    default: present
    choices: [ "present", "absent" ]
  disabled:
    description: Is the rule disabled
    type: bool
    default: false
  interface:
    description: The interface for the rule
    required: true
  floating:
    description: Is the rule floating
    type: bool
  direction:
    description: Direction floating rule applies to
    choices: [ "any", "in", "out" ]
  ipprotocol:
    description: The IP protocol
    default: inet
    choices: [ "inet", "inet46", "inet6" ]
  protocol:
    description: The protocol
    default: any
    choices: [ "any", "tcp", "udp", "tcp/udp", "icmp" ]
  source:
    description: The source address, in [!]{IP,HOST,ALIAS,any,(self)}[:port], IP:INTERFACE or NET:INTERFACE format
    required: true
    default: null
  destination:
    description: The destination address, in [!]{IP,HOST,ALIAS,any,(self)}[:port], IP:INTERFACE or NET:INTERFACE format
    required: true
    default: null
  log:
    description: Log packets matched by rule
    type: bool
  after:
    description: Rule to go after, or "top"
  before:
    description: Rule to go before, or "bottom"
  statetype:
    description: State type
    default: keep state
    choices: ["keep state", "sloppy state", "synproxy state", "none"]
  queue:
    description: QOS default queue
  ackqueue:
    description: QOS acknowledge queue
  in_queue:
    description: Limiter queue for traffic coming into the chosen interface
  out_queue:
    description: Limiter queue for traffic leaving the chosen interface
"""

EXAMPLES = """
- name: "Add Internal DNS out rule"
  pfsense_rule:
    name: 'Allow Internal DNS traffic out'
    action: pass
    interface: lan
    ipprotocol: inet
    protocol: udp
    source: dns_int
    destination: any:53
    after: 'Allow proxies out'
    state: present
"""

RETURN = """

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.networking.pfsense.pfsense_rule import PFSenseRuleModule, RULES_ARGUMENT_SPEC, RULES_REQUIRED_IF


def main():
    module = AnsibleModule(
        argument_spec=RULES_ARGUMENT_SPEC,
        required_if=RULES_REQUIRED_IF,
        supports_check_mode=True)

    pfrule = PFSenseRuleModule(module)
    pfrule.run(module.params)
    pfrule.commit_changes()


if __name__ == '__main__':
    main()
