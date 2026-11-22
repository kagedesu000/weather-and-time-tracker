# Weather & Time Tracker

Python CLI weather & local time tracker powered by the Open-Meteo API, with outfit vibe recommendations.

# Features:
- **Live Weather & Temperature:** Fetches real-time temperature (°C) and weather conditions for any city worldwide.
- **Local Timezone Detection:** Automatically calculates and displays the searched city's current local time.
- **Outfit & Vibe Recommendations:** Suggests practical clothing or activity tips based on live temperature and weather conditions.
- **Error Handling:** Gracefully handles invalid or misspelled city names without crashing.

## How to Run
1. Install the required dependency:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the tracker in your terminal:
   ```bash
   python3 Weather-And-Time-Tracker.py
   ```

## Example Output
```text
-------------------

Enter city name here please: Oslo
City: Oslo, Norway
Local Time: 22:34
Temperature: 4.2°C
Weather: Mainly Clear

Freezing! Heavy coat and warm layers needed.

Enter [Q] to end the program. Else enter any other key and continue: q

--------------------
```
