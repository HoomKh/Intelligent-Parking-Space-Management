<div style="text-align: center;">
    <img src="banner/banner.jpg" style="width:950px;height:450px;">
</div>

---

# Intelligent Parking Space Management

## Overview

**Intelligent Parking Space Management** is a computer vision-based project designed to detect and manage parking spaces in real-time. By utilizing OpenCV and machine learning techniques, this project identifies vacant spots in a parking lot from video footage, making parking management efficient and automated. This solution is ideal for modern smart city applications.

## Features

- **Real-Time Detection**: Continuously monitors parking spaces using video footage.
- **Efficient Management**: Automatically updates and displays the number of available parking spots.
- **User Interaction**: Allows users to add or remove parking space positions with mouse clicks.
- **Visual Feedback**: Highlights available and occupied spots on the video feed.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- cvzone

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/HoomKh/intelligent_parking_space_management.git
    cd intelligent_parking_space_management
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Place the required video file (`carPark.mp4`) and image file (`carParkImg.png`) in the project directory.

## Usage

1. **Mark Parking Spaces**:
    - Run `ParkingSpacePicker.py` to mark the positions of parking spaces.
    - Left-click to add a parking space.
    - Right-click to remove a parking space.
    - The positions are saved in a file named `CarParkPos`.

    ```bash
    python ParkingSpacePicker.py
    ```

2. **Run the Main Application**:
    - Run `main.py` to start the real-time parking space detection.
    - The video feed will display the parking lot with highlighted available and occupied spots.

    ```bash
    python main.py
    ```

## Files

- `ParkingSpacePicker.py`: Script to manually mark parking spaces.
- `main.py`: Main script for real-time parking space detection and management.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [OpenCV](https://opencv.org/)
- [cvzone](https://github.com/cvzone/cvzone)

---
