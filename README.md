# WhatsApp Bulk Message Sender

A Python automation script that sends bulk messages via WhatsApp Web using Selenium WebDriver.

## Features

- Send personalized messages to multiple contacts
- Uses WhatsApp Web interface for reliable message delivery
- Reads contacts and messages from CSV file
- Preserves WhatsApp session using Chrome profile
- Error handling and progress tracking
- Non-blocking browser session (detached mode)

## Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver executable
- Active WhatsApp account

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd whatsapp-bulk-sender
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Download ChromeDriver:
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/)
   - Download the version matching your Chrome browser
   - Place `chromedriver.exe` in the project directory

## Setup

1. **Prepare your contacts file (`contacts.csv`)**:
   Create a CSV file with the following columns:
   ```csv
   Name,Phone,Message
   John,+919999900000,"Hello there!"
   Jane,+919999900001,"Hi, how are you?"
   ```

2. **Configure Chrome Profile** (Optional):
   The script uses a dedicated Chrome profile to maintain WhatsApp Web session. The profile is stored at:
   ```
   C:/Users/swast/whatsapp_profile
   ```
   You can modify this path in the script if needed.

## Usage

1. Run the script:
```bash
python script.py
```

2. **First Time Setup**:
   - The script will open WhatsApp Web in Chrome
   - Scan the QR code with your phone to log in
   - Press Enter in the terminal when ready

3. **Subsequent Runs**:
   - If you're already logged in, the script will use the saved session
   - Messages will be sent automatically to all contacts in the CSV

## File Structure

```
whatsapp-bulk-sender/
├── script.py              # Main automation script
├── chromedriver.exe        # Chrome WebDriver executable
├── contacts.csv           # Contact list with messages
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## CSV Format

Your `contacts.csv` file should follow this format:

| Column | Description | Example |
|--------|-------------|---------|
| Name | Contact name (for logging) | John Doe |
| Phone | Phone number with country code | +919999900000 |
| Message | Message to send | Hello there! |

**Notes:**
- Phone numbers should include country code (e.g., +91 for India)
- Messages can contain spaces and special characters
- The script will automatically handle URL encoding

## Configuration

You can modify the following settings in `script.py`:

- **Chrome Profile Path**: Change the `--user-data-dir` argument
- **Wait Times**: Adjust `time.sleep()` values for different internet speeds
- **Button Selector**: Update XPath if WhatsApp Web changes its interface

## Error Handling

The script includes error handling for:
- Failed message delivery
- Element not found errors
- Network timeouts

Check the console output for detailed logs of success/failure for each contact.

## Important Notes

⚠️ **Terms of Service**: Make sure you comply with WhatsApp's Terms of Service when using this script.

⚠️ **Rate Limiting**: The script includes delays between messages to avoid being flagged as spam.

⚠️ **Account Safety**: Use this responsibly to avoid potential account restrictions.

## Troubleshooting

### Common Issues:

1. **ChromeDriver Version Mismatch**:
   - Ensure ChromeDriver version matches your Chrome browser version

2. **QR Code Scanning**:
   - Make sure your phone and computer are on the same network
   - Try refreshing the page if QR code doesn't appear

3. **Send Button Not Found**:
   - WhatsApp may have changed their interface
   - Check if the XPath selector needs updating

4. **Messages Not Sending**:
   - Verify phone numbers are in correct format
   - Check internet connection
   - Ensure WhatsApp Web is fully loaded

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is for educational purposes. Please ensure compliance with WhatsApp's Terms of Service and local regulations regarding automated messaging.

## Disclaimer

This tool is for educational and personal use only. The authors are not responsible for any misuse or violation of WhatsApp's Terms of Service. Use at your own risk.
