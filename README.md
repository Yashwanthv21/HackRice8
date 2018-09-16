# Schlumberger Hackathon Challenge

## Challenge

Ask an engineer how to improve an application, and they will likely say, "give me a way to see MORE DATA". Surveillance engineers may analyze output from a dozen or more sensors in the same visualization.​

Line charts are the default choice for this workflow, but they are cumbersome, especially if the data streams have different scaling and units.  And as IIoT becomes pervasive at the wellsite, this problem will only grow.​

Show us how to do it better!

Deliver a web application to display/query/analyze time-series data from downhole equipment in innovative ways.​​

## Requirements
 * [Python](https://www.python.org/)
 * [Flask](http://flask.pocoo.org/)
 * [Node.js](https://nodejs.org/en/download/)
 * [Angular CLI](https://cli.angular.io/)

## Launch Application
 - Go to directory **backend**
 - run  `python server.py`
 - Go to directory **frontend**
 - run  `npm install`
 - run `npm start`
 - Browse to  [http:\\\localhost:5000\devices](http:localhost:5000\devices)

 ## Use the APIs
 - API 1:
	- GET: /devices
		- Description: list all different devices in the dataset
		- Click on any device to visualize its data

 ## Data
 - The data currently used is static, but it is animated using JavaScript to look like the live data.
 - This project can be extended to realt-time data by using sockets to get the stream of data and update the plots.

 ## ScreenShots
 - There are currently two types of Devices IC and ESP, so there are two types of charts. One for each type.

 