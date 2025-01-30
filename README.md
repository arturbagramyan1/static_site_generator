# Tolkien Fan Club Website

This project generates a static website for a Tolkien fan club. The website includes articles and information about J.R.R. Tolkien's works, particularly "The Lord of the Rings".

## Project Structure


- `content/`: Contains the markdown files for the website content.
- `public/`: Contains the generated static website files.
- `src/`: Contains the source code for generating the static website.
- `static/`: Contains static files like CSS and images.
- `template.html`: HTML template used for generating the pages.
- `main.sh`: Script to generate the website and start a local server.
- `test.sh`: Script to run unit tests.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. Generate the static website:

   ```sh
   ./main.sh
   ```
2. Open your browser and navigate to `http://localhost:8888` to view the website.

### Running Tests

To run the unit tests, execute:

```sh
./test.sh
```
