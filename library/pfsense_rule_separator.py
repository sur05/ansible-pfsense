#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Frederic Bor <frederic.bor@wanadoo.fr>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
---
module: pfsense_rule_separator
version_added: "2.8"
author: Frederic Bor (@f-bor)
short_description: Manage pfSense rule separators
description:
  - Manage pfSense rule separators
notes:
options:
  name:
    description: The name of the separator
    required: true
  state:
    description: State in which to leave the separator
    required: true
    choices: [ "present", "absent" ]
    default: present
  interface:
    description: The interface for the separator
    required: true
  floating:
    description: Is the rule on floating tab
    type: bool
  after:
    description: Rule to go after, or "top"
  before:
    description: Rule to go before, or "bottom"
  color:
    description: The separator's color
    default: info
    choices: [ 'info', 'warning', 'danger', 'success' ]
"""

EXAMPLES = """
- name: Add rule separator voip
  pfsense_rule_separator:
    name: voip
    state: present
    interface: lan_100

- name: Remove rule separator voip
  pfsense_rule_separator:
    name: voip
    state: absent
    interface: lan_100
"""

RETURN = """
commands:
    description: the set of separators commands that would be pushed to the remote device (if pfSense had a CLI)
    returned: success
    type: list
    sample: ["create rule_separator 'SSH', interface='lan', color='info'", "update rule_separator 'SSH' set color='warning'", "delete rule_separator 'SSH'"]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.networking.pfsense.pfsense_rule_separator import PFSenseRuleSeparatorModule
from ansible.module_utils.networking.pfsense.pfsense_rule_separator import RULE_SEPARATORS_ARGUMENT_SPEC
from ansible.module_utils.networking.pfsense.pfsense_rule_separator import RULE_SEPARATORS_REQUIRED_ONE_OF
from ansible.module_utils.networking.pfsense.pfsense_rule_separator import RULE_SEPARATORS_MUTUALLY_EXCLUSIVE


def main():
    module = AnsibleModule(
        argument_spec=RULE_SEPARATORS_ARGUMENT_SPEC,
        required_one_of=RULE_SEPARATORS_REQUIRED_ONE_OF,
        mutually_exclusive=RULE_SEPARATORS_MUTUALLY_EXCLUSIVE,
        supports_check_mode=True)

    pfseparator = PFSenseRuleSeparatorModule(module)
    pfseparator.run(module.params)
    pfseparator.commit_changes()


if __name__ == '__main__':
    main()
