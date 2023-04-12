from flask import Flask, render_template, request, send_from_directory
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import re
import ray

app = Flask(__name__)

ray.init()

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    print("calculating...")
    input_endpoints = request.form['endpoints']
    print("Input Endpoints:", input_endpoints)

    input_endpoints = re.findall(r'\(([^)]+)\)', input_endpoints)
    input_endpoints = np.array([tuple(map(float, endpoint.split(','))) for endpoint in input_endpoints])

    tasks = [inverse_kinematics.remote(i, endpoint) for i, endpoint in enumerate(input_endpoints)]

    results = ray.get(tasks)

    # Reorder the results based on the index returned by the tasks
    results.sort(key=lambda x: x[0])

    # Separate the results into joint_angles and plot_filenames
    joint_angles, plot_filenames = zip(*[(joint_angle, plot_filename) for _, joint_angle, plot_filename in results])
    joint_angles = np.array(joint_angles)

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

@app.route('/visualization')
def visualization():
    print("Visualizing...")
    return render_template('visualization.html')

@ray.remote
def inverse_kinematics(i, endpoint):
    L1 = 1.0
    L2 = 1.0
    
    x = endpoint[0]
    y = endpoint[1]
    theta2 = np.arccos((x**2 + y**2 - L1**2 - L2**2)/(2*L1*L2))
    theta1 = np.arctan2(y, x) - np.arctan2(L2*np.sin(theta2), L1 + L2*np.cos(theta2))
    joint_angles = (theta1, theta2)

    plot_filename = 'figure_{}.png'.format(i)
    plt.figure()
    plt.plot([0, L1*np.cos(theta1), L1*np.cos(theta1) + L2*np.cos(theta1+theta2)], [0, L1*np.sin(theta1), L1*np.sin(theta1) + L2*np.sin(theta1+theta2)])
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Endpoint: ({:.2f}, {:.2f})\nJoint angles: ({:.2f}, {:.2f})'.format(x, y, theta1, theta2), fontsize=8)
    plt.savefig(os.path.join("static/images", plot_filename), dpi=72)
    plt.close()

    return i, joint_angles, plot_filename

if __name__ == "__main__":
    app.run(debug=True)

ray.shutdown()
