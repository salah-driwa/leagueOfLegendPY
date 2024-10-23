# League of Legends Champion Data Scraper  

This repository contains a **Python script** that scrapes **League of Legends** champion data by visiting each champion's page from Riot Games’ official site. It extracts useful information such as champion names, roles, abilities, and skins.  

The script **maps each champion's name to its corresponding URL** and retrieves the data. Since the information is **publicly accessible**, collecting it via web scraping is **legal**.

---

## Table of Contents  
- [Overview](#overview)  
- [Technologies Used](#technologies-used)  
- [How It Works](#how-it-works)  
- [Setup and Usage](#setup-and-usage)  
- [Data Format](#data-format)  
- [Legal Disclaimer](#legal-disclaimer)  
- [License](#license)

---

## Overview  
This project automates the process of collecting champion data from the League of Legends website. The goal is to gather a complete champion database for educational purposes, analysis, or personal projects.  

The scraped data includes:  
- Champion **names, roles, and difficulty**  
- **Descriptions** and **abilities** with images  
- List of **skins** with splash art  

---

## Technologies Used  
- **Python**: Main language for the script  
- **BeautifulSoup**: For HTML parsing and data extraction  
- **Requests**: For sending HTTP requests to the League of Legends website  
- **Google Colab**: Supports file download functionality  

---

## How It Works  
1. **Champion Mapping**:  
   - The script defines a list of all champions by name.  
   - It **maps each champion's name to its URL** by formatting the name in lowercase and removing spaces (e.g., `Aatrox` becomes `aatrox`).  

2. **Data Extraction**:  
   - For each champion page, the script retrieves:
     - **Name, subname, and description**  
     - **Role** and **difficulty**  
     - **Abilities** (name and icon URL)  
     - **Skins** (name and splash art URL)  
   - It stores the collected data in a structured JSON format.

3. **Error Handling**:  
   - If a page fails to load, the script logs the error and moves to the next champion.  

4. **Export and Download**:  
   - The final data is saved in a `champions_data.json` file and **downloaded automatically** if using Google Colab.

---

## Setup and Usage  

### Prerequisites  
- **Python 3.x** installed  
- **Google Colab** (optional but recommended for easy downloads)

### Installation  
1. Clone the repository:  
   ```bash
   git clone <your-repository-url>
   cd your-repository
