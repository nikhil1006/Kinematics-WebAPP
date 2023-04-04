let L1 = 100;
let L2 = 100;

function setup() {
  createCanvas(400, 400);
  angleMode(DEGREES);
}

function draw() {
  background(240);
  translate(width / 2, height / 2);

  // Draw the coordinate system grid
  drawCoordinateSystemGrid();

  let x = mouseX - width / 2;
  let y = mouseY - height / 2;

  let jointAngles = inverseKinematics(x, y);
  let theta1 = jointAngles[0];
  let theta2 = jointAngles[1];

  let elbowX = L1 * cos(theta1);
  let elbowY = L1 * sin(theta1);
  let endX = elbowX + L2 * cos(theta1 + theta2);
  let endY = elbowY + L2 * sin(theta1 + theta2);

  stroke(0);
  strokeWeight(5);

  line(0, 0, elbowX, elbowY);
  line(elbowX, elbowY, endX, endY);

  fill(255, 0, 0);
  ellipse(0, 0, 10, 10);
  ellipse(elbowX, elbowY, 10, 10);
  ellipse(endX, endY, 10, 10);

  // Display joint angles and end effector coordinates
  textSize(12);
  textAlign(LEFT, CENTER);
  fill(0);
  noStroke(); // Disable stroke for text

  push();
  translate(-width / 2, -height / 2);
  text(`Theta1: ${theta1.toFixed(2)}°`, 10, 20);
  text(`Theta2: ${theta2.toFixed(2)}°`, 10, 35);
  text(`End Effector X: ${endX.toFixed(2)}`, 10, 50);
  text(`End Effector Y: ${endY.toFixed(2)}`, 10, 65);
  pop();
}

function inverseKinematics(x, y) {
  let c2 = (x * x + y * y - L1 * L1 - L2 * L2) / (2 * L1 * L2);
  let s2 = sqrt(1 - c2 * c2);
  let theta2 = atan2(s2, c2);

  let k1 = L1 + L2 * c2;
  let k2 = L2 * s2;
  let theta1 = atan2(y, x) - atan2(k2, k1);

  return [theta1, theta2];
}

function drawCoordinateSystemGrid() {
  stroke(200);
  strokeWeight(1);

  // Grid spacing
  let gridSize = 20;

  // Draw vertical grid lines
  for (let x = -width / 2; x <= width / 2; x += gridSize) {
    line(x, -height / 2, x, height / 2);
  }

  // Draw horizontal grid lines
  for (let y = -height / 2; y <= height / 2; y += gridSize) {
    line(-width / 2, y, width / 2, y);
  }

  // Draw X and Y axes
  stroke(150);
  line(-width / 2, 0, width / 2, 0);
  line(0, -height / 2, 0, height / 2);

 // Draw axis labels
  textSize(10);
  fill(150);
  textAlign(CENTER, CENTER);
  text("X", width / 2 - 10, 10);
  text("Y", -10, -height / 2 + 20);
}
