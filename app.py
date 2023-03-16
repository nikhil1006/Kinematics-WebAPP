from flask import Flask, render_template, request, send_from_directory
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tabulate import tabulate
import os
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    input_endpoints = request.form['endpoints']
    print("Input Endpoints:", input_endpoints)

    input_endpoints = re.findall(r'\(([^)]+)\)', input_endpoints)
    input_endpoints = np.array([tuple(map(float, endpoint.split(','))) for endpoint in input_endpoints])

    joint_angles, plot_filenames = inverse_kinematics(input_endpoints)
    print("Joint Angles:", joint_angles)
    print("Plot Filenames:", plot_filenames)

    table = []
    for i in range(len(input_endpoints)):
        x, y = input_endpoints[i]
        theta1, theta2 = joint_angles[i]
        table.append([str((round(x, 2), round(y, 2))), str((round(theta1, 2), round(theta2, 2)))])

    return render_template('results.html', table=table, filenames=plot_filenames, joint_angles=joint_angles, enumerate=enumerate)

@app.route('/images/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)

def inverse_kinematics(endpoints):
    L1 = 1.0
    L2 = 1.0
    joint_angles = np.zeros((len(endpoints), 2))

    for i in range(len(endpoints)):
        x = endpoints[i, 0]
        y = endpoints[i, 1]
        theta2 = np.arccos((x**2 + y**2 - L1**2 - L2**2)/(2*L1*L2))
        theta1 = np.arctan2(y, x) - np.arctan2(L2*np.sin(theta2), L1 + L2*np.cos(theta2))
        joint_angles[i, 0] = theta1
        joint_angles[i, 1] = theta2

    plot_filenames = []

    if not os.path.exists("static/images"):
        os.makedirs("static/images")

    for i in range(len(endpoints)):
        x = endpoints[i, 0]
        y = endpoints[i, 1]
        theta1 = round(joint_angles[i, 0], 2)
        theta2 = round(joint_angles[i, 1], 2)
        plot_filename = 'figure_{}.png'.format(i)
        #plot_filename = 'images/figure_{}.png'.format(i)
        plot_filenames.append(plot_filename)
        plt.figure()
        plt.plot([0, L1*np.cos(theta1), L1*np.cos(theta1) + L2*np.cos(theta1+theta2)], [0, L1*np.sin(theta1), L1*np.sin(theta1) + L2*np.sin(theta1+theta2)])
        plt.xlim([-2, 2])
        plt.ylim([-2, 2])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.title('Endpoint: ({:.2f}, {:.2f})\nJoint angles: ({:.2f}, {:.2f})'.format(x, y, theta1, theta2), fontsize=8)
        plt.savefig(os.path.join("static/images", plot_filename), dpi=72)
        plt.close()

    return joint_angles, plot_filenames

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    #app.run(debug=True)
