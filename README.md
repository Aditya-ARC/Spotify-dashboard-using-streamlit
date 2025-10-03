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

![Dashboard Preview](<img width="1920" height="653" alt="preview-1" src="https://github.com/user-attachments/assets/d28cfdcf-4fa8-4f86-9acd-d72fb31bd551" />) 
<img width="1920" height="912" alt="preview-2" src="https://github.com/user-attachments/assets/11651007-720c-4a44-834a-64c1f9d870ef" /> 
<img width="1920" height="896" alt="preview-3" src="https://github.com/user-attachments/assets/232ed6f7-c584-4cd4-9f2f-0fc083162528" /> 
<img width="1920" height="908" alt="preview-4" src="https://github.com/user-attachments/assets/94318cd4-b9f9-485b-8405-3fceef34a08e" />




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
