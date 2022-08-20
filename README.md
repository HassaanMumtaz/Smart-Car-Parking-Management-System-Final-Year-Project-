# Smart-Car-Parking-Management-System-Final-Year-Project-
Smart Car Parking Management System is an IoT-based management system to identify which parking area is occupied or available, dependent on sensory inputs to design a real-time parking map. The map will be available to the driver through a mobile application and the web before entering the parking lot, thus avoiding traffic congestion and time wastage. In each parking slot, there will be sensors that will detect cars’ movement and update it on the digital map. The project is designed according to the university parking. Hence, it will also keep track of authorized vehicles entering the parking lot and notify each person’s payment. The system makes it easier to detect empty parking spots and provides security features to allow access to only authorized vehicles.

## NODEMCU IMPLEMENTATION:
1. Install Arduino IDE
2. Select "File" then "Preferences" and paste:
http://arduino.esp8266.com/stable/package_esp8266com_index.json
3. Go to "Tools", and then select Board Manager.
4. Navigate to esp8266 by esp8266 community and install the software for Arduino.
5. Go to:
https://github.com/FirebaseExtended/firebase-arduino
and ZIP this package.
6. Go to "Sketch" then "Include Library" then "Add .ZIP library"
7. Add the downloaded ZIP package
8. Go to "Sketch" then "Include Library" then "Manage Libraries"
9. Download "ArduinoJSON by Benoit Blanchon Version 5.13.5"
10. Copy paste the code.
11. Change WIFI_SSID, WIFI_PASSWORD to one near user.
12. Run Code.

## RASPBERRY PI IMPLEMENTATION:
1. Open Images_Data.
2. Open "pictures.txt" and change value to "pic10.jpg"
3. Open terminal on Raspberry Pi and write 
sudo pip3 install opencv
sudo pip3 install imutils
sudo pip3 install pytesseract
sudo pip3 install firebase_admin
4. Open exitImages and change "picturesExit.txt" to "pic10.jpg"
5. Open Final_Ultrasonic.py in Images_Data.
6. Run Code

## DATA VISUALIZATION:
1. Open DataViz folder.
2. Install Anaconda Distribution from :
https://www.anaconda.com/products/distribution/download-success-2
3. Open Jupyter Notebook on Anaconda
4. Open DataViz.ipynb
5. Run cell by cell using "Shift+Enter"

## Web App:
1. Install Node Package Manager and npm.
2. Install node modules in of the web app by writing npm install in the web app folder.
3. After installation write npm start on terminal to start the web app.

## Mobile App:
1. Install Node Package Manager and npm.
2. Install node modules in of the mobile app by writing npm install in the Mobile app folder.
3. After installation write npm start on terminal to start Metro Builder.
4. Install expo go on your IOS or Android Device.
5. Scan the qr code of that appear on the metro builder to start the mobile app. 

