# 🎧 Spotify Top 10,000 Songs Dashboard

This is an interactive music dashboard built with **Streamlit**, showcasing insights from the **Top 10,000 Spotify Songs (1950-Now)** dataset.

## 📌 Features

- 🎨 Multi-select Genre Filters  
- 📅 Year Slider  
- ⭐ Popularity Range Slider  
- 📊 Color-coded Scatter Plot  
- 🧠 Most Popular Artist & Average Danceability  
- 📈 Genre Distribution Pie Chart  
- 🔗 Clickable Playlist Table (Spotify links)  
- 🎧 Audio Previews for Songs  

## 📸 Preview

<img width="1920" height="991" alt="preview-1" src="https://github.com/user-attachments/assets/c5e59420-bfaa-482e-a5fb-9e5728bd5582" />
<img width="1920" height="984" alt="preview-2" src="https://github.com/user-attachments/assets/f2177759-1cb4-4c7a-876a-413f5bfba718" />
<img width="1920" height="994" alt="preview-3" src="https://github.com/user-attachments/assets/1a26393d-73a3-4bcf-b7f9-4ce4b6d17825" />






## 🚀 Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Matplotlib** & **Plotly**
- **Streamlit Components**

## 📂 Files

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit app |
| `requirements.txt` | Required Python packages |
| `top_10000_1950-now.csv` | Dataset |
| `preview.png` | Dashboard image |

---

## 💡 Approach

1. Cleaned & explored the dataset
2. Built filters (Genre, Year, Popularity)
3. Added visualizations (scatter + pie)
4. Integrated Spotify links + audio previews
5. Improved UI/UX with markdown, emojis, and sections

---

## 🛠️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
