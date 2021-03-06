#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from federatedml.util import LOGGER
from federatedml.util import consts


class Guest(object):
    def _register_batch_data_index_transfer(self, batch_data_info_transfer,
                                            batch_data_index_transfer,
                                            batch_validate_info_transfer,
                                            has_arbiter):
        self.batch_data_info_transfer = batch_data_info_transfer.disable_auto_clean()
        self.batch_data_index_transfer = batch_data_index_transfer.disable_auto_clean()
        self.batch_validate_info_transfer = batch_validate_info_transfer
        self.has_arbiter = has_arbiter

    def sync_batch_info(self, batch_info, suffix=tuple()):
        self.batch_data_info_transfer.remote(obj=batch_info,
                                             role=consts.HOST,
                                             suffix=suffix)

        if self.has_arbiter:
            self.batch_data_info_transfer.remote(obj=batch_info,
                                                 role=consts.ARBITER,
                                                 suffix=suffix)

    def sync_batch_index(self, batch_index, suffix=tuple()):
        self.batch_data_index_transfer.remote(obj=batch_index,
                                              role=consts.HOST,
                                              suffix=suffix)

    def sync_batch_validate_info(self, suffix):
        if not self.batch_validate_info_transfer:
            raise ValueError("batch_validate_info should be create in transfer variable")

        validate_info = self.batch_validate_info_transfer.get(idx=-1,
                                                              suffix=suffix)
        return validate_info


class Host(object):
    def _register_batch_data_index_transfer(self, batch_data_info_transfer, batch_data_index_transfer,
                                            batch_validate_info_transfer):
        self.batch_data_info_transfer = batch_data_info_transfer.disable_auto_clean()
        self.batch_data_index_transfer = batch_data_index_transfer.disable_auto_clean()
        self.batch_validate_info_transfer = batch_validate_info_transfer

    def sync_batch_info(self, suffix=tuple()):
        LOGGER.debug("In sync_batch_info, suffix is :{}".format(suffix))
        batch_info = self.batch_data_info_transfer.get(idx=0,
                                                       suffix=suffix)
        batch_size = batch_info.get('batch_size')
        if batch_size < consts.MIN_BATCH_SIZE and batch_size != -1:
            raise ValueError(
                "Batch size get from guest should not less than {}, except -1, batch_size is {}".format(
                    consts.MIN_BATCH_SIZE, batch_size))
        return batch_info

    def sync_batch_index(self, suffix=tuple()):
        batch_index = self.batch_data_index_transfer.get(idx=0,
                                                         suffix=suffix)
        return batch_index

    def sync_batch_validate_info(self, validate_info, suffix=tuple()):
        self.batch_validate_info_transfer.remote(obj=validate_info,
                                                 role=consts.GUEST,
                                                 suffix=suffix)


class Arbiter(object):
    def _register_batch_data_index_transfer(self, batch_data_info_transfer, batch_data_index_transfer):
        self.batch_data_info_transfer = batch_data_info_transfer.disable_auto_clean()
        self.batch_data_index_transfer = batch_data_index_transfer.disable_auto_clean()

    def sync_batch_info(self, suffix=tuple()):
        batch_info = self.batch_data_info_transfer.get(idx=0,
                                                       suffix=suffix)
        return batch_info
