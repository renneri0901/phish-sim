# Phishing Simulation Tool - User Manual

## 1. Introduction

The **Phishing Simulation Tool** allows users to simulate phishing attacks to educate and train individuals on recognizing and preventing phishing schemes. This user manual provides instructions on how to set up and use the tool effectively.

---

## 2. Prerequisites

Before using the tool, make sure you have the following:

- **Python 3.7+** installed on your system.
- Basic understanding of running Python scripts and command-line operations.
- A text editor (e.g., VSCode or PyCharm) for editing configuration files.

---

## 3. Installation and Setup

### Step 1: Clone the Repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/your-username/phishing-simulation-tool.git
cd phishing-simulation-tool
````

### Step 2: Install Dependencies

Install the necessary Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This will install the required modules, including Flask and other dependencies.

---

### Step 3: Configuration

* **Email Settings**: Modify the `phishing_email.py` file to include your email credentials. You may need to generate an app-specific password for Gmail or use another email service that allows sending emails via SMTP.
* **Tracking Server**: Make sure the tracking server URL in `phishing_email.py` matches the local server URL (`localhost:5000`) for testing.

---

## 4. Running the Tool

To run the phishing simulation tool, simply run the following command:

```bash
python src/main.py
```

This will start the tool and present a menu of options:

1. **Scrape a Website**: Scrape a target website and serve it locally.
2. **Spoof a Login Page**: Create a fake login page to simulate a phishing attack.
3. **Send a Phishing Email**: Send an email with a phishing link to the target.
4. **Track User Interaction**: Track user clicks on phishing links via a Flask-based server.

### Example Usage

* If you choose **1** to scrape a website, you'll be prompted to enter a URL. The tool will fetch the site and serve it locally.
* If you choose **2** to spoof a login page, you'll be asked to provide the HTML content to spoof.
* When you choose **3** to send a phishing email, the tool will ask you to enter the target email address and customize the subject and body.
* The tracking server will log each click on the phishing link, recording the timestamp and IP address.

---

## 5. Click Tracking

The tool logs each user click on the phishing link in a log file called `clicks.log`. This log file will contain details such as:

* **Timestamp**: When the link was clicked.
* **IP Address**: The IP address of the user who clicked the link.

You can view this log by opening the `clicks.log` file.

---

## 6. Troubleshooting

* **Error**: "SMTP Authentication Error"

  * **Solution**: Make sure your email credentials are correct, and if using Gmail, enable "less secure apps" or generate an app-specific password.
* **Error**: "Flask Server Not Starting"

  * **Solution**: Ensure that port 5000 is open and not being used by another application. You can change the port in the `tracking_server.py` file.

---

## 7. Ethical Use and Guidelines

* **Training Purpose**: The tool is designed for cybersecurity training and awareness.
* **Permission**: Always ensure that you have permission from users and organizations before conducting phishing simulations.
* **Respect Privacy**: Any data logged during testing should be handled with care and should be anonymized if shared.

---

## 8. Conclusion

This tool helps users understand phishing attacks and improve their ability to recognize suspicious activities. It should be used responsibly and ethically, following all legal and organizational guidelines for phishing simulations.