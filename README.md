# Football Player Chatbot

This project is a chatbot application designed using **Streamlit** and powered by **LangChain** to provide insightful answers to questions about football players. The application integrates data extraction, transformation, and storage processes to ensure up-to-date and accurate responses.

## Features

### Chatbot Functionality
- The chatbot leverages LangChain to process and understand user queries.
- It provides detailed and contextual information about football players, offering a seamless user experience.

### ETL Pipeline
- **Extraction**: Data is scraped from a designated webpage.
- **Transformation**: The extracted data is cleaned and formatted for consistency.
- **Load**: The processed data is saved as a CSV file in the `files` directory.

### Data Storage
- The generated CSV files are uploaded to an Amazon S3 bucket for scalable and secure storage.

## Project Structure
```plaintext
.
├── etl_script.py         # ETL script for data extraction, transformation, and loading
├── chatbot.py            # Streamlit application for the chatbot
├── requirements.txt      # List of dependencies
├── files/                # Directory for storing generated CSV files
└── README.md             # Project documentation
```

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- AWS CLI configured with access to an S3 bucket

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/football-player-chatbot.git
   cd football-player-chatbot
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Run the ETL script to generate the CSV file:
   ```bash
   python etl_script.py
   ```
2. Start the chatbot application:
   ```bash
   streamlit run chatbot.py
   ```
3. Access the application in your web browser at `http://localhost:8501`.

## AWS S3 Integration
- The `etl_script.py` includes functionality to upload the generated CSV files to an S3 bucket.
- Ensure your AWS credentials are properly configured for seamless uploads.

## Contributing
Feel free to contribute by submitting issues or pull requests. For significant changes, please discuss them in advance.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- [Streamlit](https://streamlit.io/) for the easy-to-use web application framework.
- [LangChain](https://langchain.com/) for the robust language model chaining capabilities.
- [AWS](https://aws.amazon.com/) for cloud storage solutions.

---

Enjoy exploring football player statistics and insights!
