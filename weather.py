#!/usr/bin/python
'''
Weather.py
John Heenan
14 February 2014
A simple utlity to send notifications to your phone when it starts raining outside of your windowless CS lab.
Run as a login item/launchd process/drop it in .bashrc and it will only call you when you're in the lab.
'''

import urllib2
import json
import time

import pynma

'''
Some configuration variables
'''

WU_KEY = '' # Weather Underground API Key - The free developer tier should suffice
NMA_KEY = '' # Notify My Android API Key
LOC = 'UK/London' # Weather Underground Area ID/Location Name
DELAY = 300 # Refresh interval

'''
You shouldn't need to modify anything after this point.
'''

notifier = pynma.PyNMA(NMA_KEY)

def sendMessage(message):
	notifier.push("Weather Checker", message, "The weather outside the CS lab has changed. It is currently " + message + " .\nData by Weather Underground\nImplementation by J. Heenan.")

def main():
	print("Weather monitor started.")

	last_observation = ''

	while True:
		notify = False

		data = urllib2.urlopen('http://api.wunderground.com/api/' + WU_KEY + '/geolookup/conditions/q/' + LOC + '.json')
		json_string = data.read()
		parsed_json = json.loads(json_string)
		observation = parsed_json['current_observation']['weather']
		if "Rain" in observation or "Snow" in observation:
			if observation != last_observation:
				notify = True # Send message if it has started raining/rain conditions change

		if "Rain" in last_observation or "Snow" in last_observation:
			if observation != last_observation:
				notify = True # Send message if it was raining and it isn't. If rain conditions change this will have no effect, notify is already True

		if notify:
			sendMessage(observation)

		last_observation = observation

		time.sleep(DELAY)

if __name__ == '__main__':
	main()