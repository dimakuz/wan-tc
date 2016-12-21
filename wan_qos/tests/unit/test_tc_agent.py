# Copyright (c) 2016 Huawei, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from wan_qos.agent import tc_driver

from neutron.tests import base


class TestTcDriver(base.BaseTestCase):
    def setUp(self):
        super(TestTcDriver, self).setUp()
        self.tc_agent = tc_driver.TcDriver()
        self.tc_agent.set_ports('enp1s0f0', 'enp1s0f1')

    def test_clear_all(self):
        self.tc_agent.clear_all()

    def test_set_root_queue(self):
        tc_dict = {
            'port_side': 'lan_port',
            'max_rate': '100mbit'
        }
        self.tc_agent.set_root_queue(tc_dict)

        tc_dict = {
            'port_side': 'wan_port',
            'max_rate': '100mbit'
        }
        self.tc_agent.set_root_queue(tc_dict)

    def test_add_limiter(self):
        tc_dict = {
            'port_side': 'lan_port',
            'parent': '1',
            'child': '10',
            'min': '200kbit',
            'max': '512kbit'
        }
        self.tc_agent.create_traffic_limiter(tc_dict)
        tc_dict = {
            'port_side': 'wan_port',
            'parent': '1',
            'child': '10',
            'min': '2mbit',
            'max': '2mbit'
        }
        self.tc_agent.create_traffic_limiter(tc_dict)
        tc_dict = {
            'port_side': 'wan_port',
            'parent': '10',
            'child': '100',
            'min': '200kbit',
            'max': '512kbit'
        }
        self.tc_agent.create_traffic_limiter(tc_dict)

    def test_update_limiter(self):
        tc_dict = {
            'port_side': 'lan_port',
            'parent': '1',
            'child': '10',
            'min': '300kbit',
            'max': '400kbit'
        }
        self.tc_agent.update_traffic_limiter(tc_dict)
        tc_dict = {
            'port_side': 'wan_port',
            'parent': '10',
            'child': '100',
            'min': '250kbit',
            'max': '600kbit'
        }
        self.tc_agent.update_traffic_limiter(tc_dict)

    def test_add_filter(self):
        tc_dict = {
            'port_side': 'lan_port',
            'protocol': 'vxlan',
            'vni': 100,
            'child': '10'
        }
        self.tc_agent.create_filter(tc_dict)
        tc_dict = {
            'port_side': 'wan_port',
            'protocol': 'vxlan',
            'vni': 100,
            'child': '100'
        }
        self.tc_agent.create_filter(tc_dict)

    def test_remove_limiter(self):
        tc_dict = {
            'port_side': 'lan_port',
            'parent': '1',
            'child': '10'
        }
        self.tc_agent.remove_traffic_limiter(tc_dict)
        tc_dict = {
            'port_side': 'wan_port',
            'parent': '1',
            'child': '10'
        }
        self.tc_agent.remove_traffic_limiter(tc_dict)