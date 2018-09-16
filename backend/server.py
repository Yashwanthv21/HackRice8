#!/usr/bin/python

from flask import Flask, jsonify, request, abort, render_template
from timeseries import read_data
import json
from jsonmerge import merge

app = Flask(__name__)

data, equipments, sensors_per_equipment = read_data('input/data-large.csv')


# @app.route('/timeseries')
# def series():
#     device_id = request.args.get('deviceid')
#     sensor = request.args.get('sensor')
#     print(data)
#     for d in data:
#         print(d)
#         # if d.equipment == device_id and d.sensor == sensor:
#         if d.equipment == device_id:
#             return render_template('timeseries.html',data=d.serialize)
#             # return d.serialize
#     abort(404)

@app.route('/timeseries', methods=['POST'])
def series():
    if request.method == 'POST':
        sensors =  request.form.getlist('sensors')
        device_id = request.form.get('device_id')
        print(sensors,device_id)
    # print(data)
        out = {}
        for d in data:
            if d.equipment == device_id:
                print(True)
                for s in sensors:
                    print(s)
                    if d.sensor == s:
                        print("sensor in data")
                        # out = {key: value for (key, value) in (json.loads(d).items()+json.loads(out).items())}
                        # print(d.serialize)
                        # if bool(out):
                        #     out = merge(d.serialize,out)
                        # else: 
                        #     out = d.serialize
                        if not bool(out):
                            # print(json.loads(d.serialize)["datapoints"])
                            # out["ts"]=[k for di in json.loads(d.serialize)["datapoints"] for k in di['timestamp']]

                            out["ts"]= [a['timestamp'] for a in json.loads(d.serialize)["datapoints"]]
                        obj = json.loads(d.serialize)
                        t = {}
                        t['equipment'] = obj['equipment']
                        t['unit'] = obj['unit']
                        t['sensor'] = obj['sensor']
                        t['points'] = [a['value'] for a in obj["datapoints"]]
                        out[s] = t
                # print(out)
        # print(out["ts"])
        return render_template('timeseries.html',data=json.dumps(out))
            # return d.serialize
    abort(404)


@app.route('/ts')
def ts():
    device_id = request.args.get('deviceid')
    if(device_id in sensors_per_equipment):
        sensors=sensors_per_equipment[device_id]
        out = {}
        for d in data:
            if d.equipment == device_id:
                for s in sensors:
                    if d.sensor == s:
                        print("sensor in data")
                        if not bool(out):
                            out["ts"]= [a['timestamp'] for a in json.loads(d.serialize)["datapoints"]]
                        obj = json.loads(d.serialize)
                        t = {}
                        t['equipment'] = obj['equipment']
                        t['unit'] = obj['unit']
                        t['sensor'] = obj['sensor']
                        t['points'] = [a['value'] for a in obj["datapoints"]]
                        out[s] = t
                # print(out)
        # print(out["ts"])
        return render_template('ts.html',data=json.dumps(out))
            # return d.serialize
    abort(404)

@app.route('/sensors')
def sensors():
    device_id = request.args.get('deviceid')
    if(device_id in sensors_per_equipment):
        # return json.dumps(sensors_per_equipment[device_id])
        return render_template('sensors.html', sensors=sensors_per_equipment[device_id], device=device_id)
    abort(404)


@app.route('/devices')
def devices():
    print(json.dumps(equipments))
    return render_template('devices.html' ,devices=equipments)


# @app.after_request
# def after_request(response):
#     response.headers.add('Content-Type', 'application/json')
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers',
#                          'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=False)
