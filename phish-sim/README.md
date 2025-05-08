# Phishing Simulation Tool

## Project Overview and Goals

The **Phishing Simulation Tool** is an educational project designed to simulate phishing attacks for cybersecurity awareness training. It provides the following functionalities:

- **Website Scraping & Hosting**: Scrapes websites and runs them locally for testing.
- **Login Page Spoofing**: Mocks login pages to simulate phishing attempts.
- **Phishing Email Creation**: Sends phishing emails with a configurable body and tracking links.
- **Click Tracking Server**: Tracks and logs user clicks on phishing links to demonstrate the effectiveness of phishing attacks.

The goal of this project is to raise awareness about phishing tactics and demonstrate how they work in a controlled environment.

---

## Setup Instructions

### Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.7+**
- A **text editor** (e.g., Visual Studio Code, Sublime Text)
- Basic familiarity with Python and command-line tools.

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/phishing-simulation-tool.git
cd phishing-simulation-tool
````

### Step 2: Install Dependencies

Use `pip` to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

This will install the required Python libraries, such as Flask, smtplib, etc.

---

## Usage Instructions

### Running the Tool

To start the tool, run the following command from the root directory:

```bash
python src/main.py
```

This will launch a command-line interface where you can choose different options:

1. **Scrape a Website**: Scrape and serve a website locally.
2. **Spoof a Login Page**: Create a fake login page to simulate phishing.
3. **Send a Phishing Email**: Send an email containing phishing links to a target.
4. **Track User Interaction**: Track and log interactions with phishing links via a Flask-based server.

### Example Flow

1. **Option 1 (Scrape Website)**: Enter the URL of the website you wish to scrape, and the tool will save and serve it locally.
2. **Option 2 (Spoof Login Page)**: Specify the HTML for a login page to create a phishing simulation.
3. **Option 3 (Send Phishing Email)**: The tool sends a phishing email with a tracking link.
4. **Option 4 (Track Clicks)**: The Flask server logs any clicks on the phishing links, recording the timestamp and the IP address of the user.

---

## Configuration Details

### Phishing Email Configuration

* Modify the `phishing_email.py` file to include your email and the recipient's email.
* Update SMTP settings (e.g., Gmail or other services) and ensure the app-specific password is used.

### Tracking Server

* The **Flask tracking server** runs on port `5000` by default and logs each click on phishing links.
* Replace the placeholder `YOUR_SERVER` with the actual server URL or use `localhost` for local use.

### Click Logs

* Click logs are stored in `clicks.log`, which records the **timestamp**, **IP address**, and **email ID** for every click.

---

## Ethical Considerations & Responsible Use

### Ethical Guidelines:

* **Consent**: Only use this tool on systems and individuals who have explicitly consented to phishing simulations.
* **Privacy**: Handle any data responsibly and avoid misuse.
* **Purpose**: The tool is designed for educational purposes and should not be used for malicious activities.

### Responsible Use:

* **Training Simulations**: Ensure participants are aware that it’s a simulated phishing attack.
* **Anonymization**: Use anonymized data for testing purposes and avoid using real sensitive information.
* **Compliance**: Ensure all actions comply with local laws and organizational policies.

---

## Known Limitations

* **Email Providers**: The tool currently supports email sending via SMTP (e.g., Gmail). Some services may block external SMTP connections.
* **Flask Server**: The Flask server is intended for local use and is not suitable for high-traffic production environments.
* **Scraping Limitations**: Some websites may block scraping attempts or have protections in place that prevent the tool from working.

---

## Contributing

We welcome contributions to this project! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes (`git push origin feature-name`).
5. Submit a pull request.

---

## Acknowledgments

* Special thanks to the open-source community for the libraries and frameworks used in this project, such as Flask, smtplib, and others.
* This project is built to educate individuals about the risks of phishing and raise awareness about cybersecurity.

**End of README**
