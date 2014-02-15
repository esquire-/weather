Weather Updates
===============

weather.py is a simple Python script that integrates the [Weather Underground API](http://www.wunderground.com/weather/api/) with [Notify My Android](http://notifymyandroid.com/). It periodically polls WU and will send an NMA alert if it starts raining or snowing.

Motivation
----------

I work in a lab with no windows. In a part of the world where it can start raining unpredictably. So I wrote this script, which runs automatically when I log in. It will check for rain every five minutes and send me an alert. When I log out and leave the lab it stops checking.

Setup
-----

Get API keys for Weather Underground and Notify My Android. Set those values in the top of the weather.py file.

Usage
-----

`python weather.py`

And let it run.

Running Automatically
---------------------

There is a .plist file supplied, edit it to point to your copy of weather.py and save it in `~/Library/LaunchAgents/`. The script will automatically run at login.

Alternatively, add it as a login item.

License
-------
Mozilla Public License 2

Author
------
John Heenan

[@0xEsquire](https://twitter.com/0xEsquire)