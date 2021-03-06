# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. ANSSI. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/si2ter_rest_octets.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.33a SI 2ter Rest Octets
# top-level object: SI2ter Rest Octets



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

utran_tdd_description_struct = CSN1List(name='utran_tdd_description_struct', list=[
  CSN1Val(name='', val='01'),
  CSN1Bit(name='tdd_arfcn', bit=14),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='bandwidth_tdd', bit=3)])})])

_3g_measurement_parameters_description_struct = CSN1List(name='_3g_measurement_parameters_description_struct', list=[
  CSN1Bit(name='qsearch_i', bit=4),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='fdd_qoffset', bit=4),
    CSN1Bit(name='fdd_qmin', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tdd_qoffset', bit=4)])})])

_3g_additional_measurement_parameters_description_struct = CSN1List(name='_3g_additional_measurement_parameters_description_struct', list=[
  CSN1Bit(name='fdd_qmin_offset', bit=3),
  CSN1Bit(name='fdd_rscpmin', bit=4)])

utran_fdd_description_struct = CSN1List(name='utran_fdd_description_struct', list=[
  CSN1Val(name='', val='01'),
  CSN1Bit(name='fdd_arfcn', bit=14),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='bandwidth_fdd', bit=3)])})])

si2ter_rest_octets = CSN1List(name='si2ter_rest_octets', list=[
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='si2ter_mp_change_mark'),
    CSN1Bit(name='si2ter_3g_change_mark'),
    CSN1Bit(name='si2ter_index', bit=3),
    CSN1Bit(name='si2ter_count', bit=3),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='utran_fdd_description', obj=utran_fdd_description_struct)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='utran_tdd_description', obj=utran_tdd_description_struct)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='_3g_measurement_parameters_description', obj=_3g_measurement_parameters_description_struct)])}),
    CSN1Alt(alt={
      'H': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Ref(name='_3g_additional_measurement_parameters_description', obj=_3g_additional_measurement_parameters_description_struct)])})]),
      'L': ('', []),
      None: ('', [])})]),
    'L': ('', [])}),
  CSN1Ref(obj=spare_padding)])

