import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# 1. Load the dataset
df = pd.read_csv("top_10000_1950-now.csv")

# 2. Preprocess 'Album Release Date' → 'Release Year'
df['Album Release Date'] = pd.to_datetime(df['Album Release Date'], errors='coerce')
df['Release Year'] = df['Album Release Date'].dt.year

# 3. Page setup
st.set_page_config(page_title="Spotify Top 10K", layout="wide")
st.markdown("## 🎵 Spotify Top 10,000 Songs Dashboard")
st.image("https://upload.wikimedia.org/wikipedia/commons/8/84/Spotify_icon.svg", width=80)

st.markdown("""
> 🎶 **Welcome to the Spotify Top 10,000 Songs Dashboard!**  
> Explore popular songs across genres and years. Use the sidebar to filter by genre, year, and popularity range.  
> Enjoy visual insights, charts, and direct access to tracks!
""")


# 4. Sidebar filters
st.sidebar.header("🔍 Filter Songs")

# Genre filter
genres = df['Artist Genres'].dropna().unique().tolist()
genres.sort()
selected_genres = st.sidebar.multiselect("Select Genre(s)", genres, default=genres[:1]) 

# Year slider
min_year = int(df['Release Year'].min())
max_year = int(df['Release Year'].max())
selected_year = st.sidebar.slider("Select Year", min_year, max_year, max_year)

# Popularity range slider
min_pop = int(df['Popularity'].min())
max_pop = int(df['Popularity'].max())
selected_pop_range = st.sidebar.slider("Select Popularity Range", min_pop, max_pop, (min_pop, max_pop))

# Combine selected genres into a regex OR string (e.g., "pop|rock|jazz")
genre_regex = '|'.join(selected_genres)

# Apply filters
filtered_df = df[
    df['Artist Genres'].str.contains(genre_regex, case=False, na=False) &
    (df['Release Year'] == selected_year) &
    (df['Popularity'] >= selected_pop_range[0]) &
    (df['Popularity'] <= selected_pop_range[1])
]


# 6. Show fallback if no results
if filtered_df.empty:
    st.warning("⚠️ No songs found for the selected filters. Try changing Genre, Year, or Popularity Range.")
else:
    # 7. Show KPIs
    st.subheader(f"📊 Spotify Top 10,000 Songs Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Tracks", len(filtered_df))
    col2.metric("Avg Danceability", round(filtered_df['Danceability'].mean(), 2))
    col3.metric("Most Popular Artist", filtered_df['Artist Name(s)'].mode()[0])

    # 8. Scatter chart
   # Color-coded scatter plot using Altair
#import altair as alt

st.subheader(f"📈 Popularity vs Energy ({', '.join(selected_genres)} - {selected_year})")
scatter_chart = alt.Chart(filtered_df).mark_circle(size=100).encode(
    x='Popularity',
    y='Energy',
    color=alt.Color('Artist Genres', scale=alt.Scale(scheme='category10'), legend=alt.Legend(title="Genres")),
    tooltip=['Track Name', 'Artist Name(s)', 'Popularity', 'Energy']
).interactive()

st.altair_chart(scatter_chart, use_container_width=True)


# 9. Expandable Raw Data
with st.expander("📋 Show Raw Data"):
    st.dataframe(filtered_df.head(50))

# 🎵 Interactive playlist with links
st.subheader("🎧 Interactive Playlist Table")
playlist_df = filtered_df[['Track Name', 'Artist Name(s)', 'Popularity', 'Album Name', 'Track URI']].copy()
playlist_df['Spotify Link'] = playlist_df['Track URI'].apply(lambda x: f"https://open.spotify.com/track/{x.split(':')[-1]}")
playlist_df = playlist_df.drop(columns=['Track URI'])

# Turn into clickable links
playlist_df['Spotify Link'] = playlist_df['Spotify Link'].apply(lambda x: f"[🔗 Link]({x})")

st.write(playlist_df.to_markdown(index=False), unsafe_allow_html=True)

# 📊 Genre distribution Pie Chart
import matplotlib.pyplot as plt

st.subheader("📊 Genre Distribution")
genre_counts = filtered_df['Artist Genres'].value_counts().head(10)

fig, ax = plt.subplots()
ax.pie(genre_counts.values, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig)

# 🔊 Audio previews
st.subheader("🔊 Audio Previews (if available)")
previewable_df = filtered_df[['Track Name', 'Artist Name(s)', 'Track Preview URL']].dropna()

for index, row in previewable_df.iterrows():
    st.write(f"**{row['Track Name']}** by *{row['Artist Name(s)']}*")
    st.audio(row['Track Preview URL'])

