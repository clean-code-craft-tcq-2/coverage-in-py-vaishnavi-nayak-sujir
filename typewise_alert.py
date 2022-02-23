# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:15:08 2022

@author: IVA3KOR
"""


coolimgtype_limit = {'PASSIVE_COOLING':[0,35],'HI_ACTIVE_COOLING':[0,45],'MED_ACTIVE_COOLING':[0,40]}
email_message = {'TOO_LOW':'Hi, the temperature is too low','TOO_HIGH':'Hi, the temperature is too high' }
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit = coolimgtype_limit[coolingType][0]
  upperLimit = coolimgtype_limit[coolingType][1]
  return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
    return 1
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)
    return 1


def send_to_controller(breachType):
  header = 0xfeed
  print('{}, {}'.format(header,breachType))
  return 1


def send_to_email(breachType):
	recepient = "a.b@c.com"
	print('To: {}'.format(recepient))
	print(email_message[breachType])
	return 1
	

