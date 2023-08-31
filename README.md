# Kaushal's MaCSTC Data Visualizer

This project provides a data visualization tool that allows you to analyze the frequency distribution of check-in times. It reads data from an Excel file located in the `data` folder and displays a histogram showing the distribution of check-in times.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x is installed.
- The required Python packages are listed in `requirements.txt`.

## Getting Started

1. Clone this repository to your local machine.
   - On the GitHub page, click on the green `Code` button and click `Download Zip`.
2. Install the required packages using the following command `pip install -r requirements.txt`.
3. Place your Excel files in the `data` folder within the project directory. Make sure the Excel file contains a sheet labeled as "Sheet2" with the required data format.

## Usage

1. Launch the terminal and navigate to the project directory.
   - On Windows, you can do this by hitting the `Windows` key and typing `cmd`. A command prompt window should appear. Type `cd <path-to-project-directory>` to navigate to the project directory (cd Desktop/Check-in-Visualizer/).
   - On Mac, you can do this by hitting `Command + Space` and typing `terminal`. A terminal window should appear. Type `cd <path-to-project-directory>` to navigate to the project directory (cd Desktop/Check-in-Visualizer/).
2. Run the `main.py` script:
   - In the terminal, type `python3 main.py` and hit `Enter`.
3. The program will greet you and prompt you to select 1 if you want to `view a frequency distribution` or 2 if you want to exit.
4. If you select 1, the program will prompt you to enter the name of the Excel file you want to analyze. Type the name of the file (e.g. `data`) and hit `Enter`.
    - Note: You do not need to include the file extension (e.g. `.xlsx`).
5. The program will display a histogram showing the distribution of check-in times.
    - You can save the histogram by clicking on the `Save` button.

## Data Format

The Excel file should have a sheet labeled as "Sheet2" with columns "Check In Date" and "Check In Time". The time should be in the format "hh:mm AM/PM".

[Sample Excel Data](https://ibb.co/9YvdVZW)


## Example
![Example Run](link_to_gif)


## Contact

If you have any questions or feedback, feel free to contact the project maintainer at [Email me](mailto:patelkaushalb1@gmail.com)

