# Caesar Cipher Encryption Tool

## Project Overview
This project demonstrates the classical Caesar cipher encryption technique, where each letter in a message is shifted by a specified number of positions within the alphabet. The tool supports both encryption and decryption and was initially developed as a Python command-line application. It was later enhanced with a Streamlit-based web interface to offer a more interactive user experience.

## Features
- **Text Encryption and Decryption**: Encode or decode messages based on a shift value.
- **Dynamic Shift Handling**: Modular arithmetic ensures smooth wrapping around the alphabet.
- **Flexible Input**: Only alphabetic characters are modified; numbers, spaces, and special characters remain unchanged.
- **Interactive Web Interface**: Built with Streamlit for real-time user interaction.

## Technologies Used
- **Python**: Core encryption and decryption logic.
- **Streamlit**: Frontend development for creating a simple and effective web interface.

## How It Works
1. Users can input their text message.
2. Choose whether to **encode** (encrypt) or **decode** (decrypt).
3. Select a shift number.
4. View the encrypted or decrypted result instantly.

## Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/caesar-cipher-streamlit.git
