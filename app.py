import streamlit as st
import pandas as pd
import numpy as np
import time
import requests

st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.8)), url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba");
        background-size: cover;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="🎬 Hybrid OTT Recommender", layout="wide")

# --- 1. SESSION STATE CHECK  ---
if 'get_started' not in st.session_state:
    st.session_state.get_started = False

# --- 2. LANDING PAGE LOGIC ---
if not st.session_state.get_started:
    # Page Center Alignment ke liye columns
    _, col_mid, _ = st.columns([1, 2, 1])
    
    with col_mid:
        st.markdown("<h1 style='text-align: center; color: #FFD700;'>🎬 CineMatch AI</h1>", unsafe_allow_html=True)
        st.write("### Your ultimate AI cinema curator. Personalized. Predictive. Perfect. ✨")
        
        st.image("welcome.gif")
        
        st.info("Ready to find your next favorite movie?")
        
        if st.button("🚀 Get Started", use_container_width=True):
            st.session_state.get_started = True
            st.rerun() 
            
    st.stop() 

st.markdown("""
<style>
    /* 1. Main Title styling */
    .title-text {
        text-align: center; 
        font-size: 55px; 
        color: #FFD700 !important; /* Gold color taaki dark background par dikhe */
        font-weight: bold;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
        margin-bottom: 0px;
    }

    /* 2. Subtitle styling */
    .sub-text {
        text-align: center; 
        font-size: 20px; 
        color: #FFFFFF !important; /* Pure White */
        margin-top: -10px;
        margin-bottom: 30px;
    }

    /* 3. Movie Card styling (Netflix style glass look) */
    .movie-card {
        background-color: rgba(255, 255, 255, 0.1); 
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #FF4B4B; /* Side mein red line attractive lagti hai */
        margin-bottom: 15px;
        transition: 0.3s;
    }

    /* 4. Movie Title inside card */
    .movie-card b {
        color: #FFD700; 
        font-size: 22px;
    }

    /* 5. Genre Badge styling */
    .genre-badge {
        display: inline-block;
        background-color: #4A90E2;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 13px;
        margin-right: 5px;
        margin-top: 5px;
    }
            /* Movie sections ki setting */
.recommendation-section {
    padding: 20px;
    margin-bottom: 40px;
}

.section-title {
    color: gold; /* "Wow" effect ke liye gold color */
    font-size: 24px;
    margin-bottom: 20px;
    border-left: 5px solid gold;
    padding-left: 15px;
}

/* Posters ko bada aur space ko tight karne ke liye */
.movie-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); 
    gap: 25px; /* Cards ke beech ki gap */
}

.movie-card {
    background: #222;
    border-radius: 10px;
    overflow: hidden;
    transition: 0.3s;
}

.movie-card:hover {
    transform: scale(1.05); /* Hover karne pe thoda bada hoga */
}

.movie-card img {
    width: 100%;
    height: 320px; /* Poster height fix */
    object-fit: cover;
}
</style>
 """, unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>🎬 CineMatch AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'> Your ultimate AI cinema curator.Personalized, Predictive & Perfect</p>", unsafe_allow_html=True)

import streamlit.components.v1 as components

# --- AUTOMATIC VOICE WELCOME ---
components.html(
    """
    <script>
        var msg = new SpeechSynthesisUtterance();
        msg.text = "Elevating your movie experience with Hybrid Intelligence.Discover movies that match your mood and vibe!";
        msg.rate = 0.9; 
        window.speechSynthesis.speak(msg);
    </script>
    """,
    height=0,
)

page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Movie Recommender", "About Project"]
)

# =========================================================
# --- LIVE CLOCK AND GREETING:  ---
# =========================================================
import datetime

st.sidebar.markdown("---")

st.sidebar.markdown("<h3 style='color: #FFD700;'>🕰️ Time & Vibe Check</h3>", unsafe_allow_html=True)

# 3. Current Time and Day generate 
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%I:%M %p") # E.g., 09:30 PM
day_name = current_time.strftime("%A")             # E.g., Thursday

# 4. dynamic greeting: Time ke hisab se text set karna
hour = current_time.hour
greeting = ""
if hour < 12:
    greeting = "Rise & Shine! Good Morning 🌅 Good Morning, early bird! Tell us your morning movie requirement."
elif hour < 17:
    greeting = "Afternoon Bliss! Good Afternoon ☀️ Good Afternoon, busy bee! Need an afternoon escape?"
else:
    greeting = "Evening Vibe! Good Evening 🌙 Good Evening, Cinephile! What's the plan tonight?"

st.sidebar.markdown(f"**⏰ Current Time:** {formatted_time}", unsafe_allow_html=True)
st.sidebar.markdown(f"**📅 Today:** {day_name}", unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True) # Ek khali space

st.sidebar.markdown(f"<p style='color: #FFD700; font-style: italic; font-size: 16px;'>{greeting}</p>", unsafe_allow_html=True)


if page == "Home":
    st.title("Welcome to CineMatch AI")
    st.write("Your AI powered movie recommendation system.")

st.markdown('<p class="title">🎥 CineMatch: Smart OTT Recommender</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Exact genre matches first + hybrid scoring (content & collaborative) + Mood, Time & Social Filters</p>', unsafe_allow_html=True)

# --- WELCOME SECTION START ---
st.markdown("---")
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("### ✨ Welcome to CineMatch AI")
    st.write("Mood kharab hai ya excitement level high? Hum dhoondenge aapke liye perfect movie!")
with col2:
    st.metric(label="System Status", value="Ready ✅")
st.markdown("---")
# --- WELCOME SECTION END ---

if page == "About Project":

    st.title("About CineMatch AI")

st.write("""
    CineMatch AI is a Hybrid OTT Movie Recommendation System.

    Features:
    - Mood Based Movie Recommendation
    - Time Based Filtering
    - Social Watching Suggestions
    - Genre Based Hybrid Recommendation
    - AI Scanning Animation

    This system helps users find the best movies based on their mood,
    available time and preferences.
    """)

# LOAD DATA
# Ensure merged_movies.csv has: movieId, title, genres, rating
movies_df = pd.read_csv("merged_movies.csv")[['movieId','title','genres','rating']]

# Remove duplicate titles, keep the highest rating
movies_df = movies_df.sort_values(by='rating', ascending=False).drop_duplicates(subset='title', keep='first')

movies_df['genres'] = movies_df['genres'].fillna('Unknown')

st.sidebar.header("⚙️ Select Genres")
all_genres = set()
for g in movies_df['genres']:
    all_genres.update(g.split('|'))
all_genres = sorted(all_genres)

selected_genres = st.sidebar.multiselect(
    "Choose genres you like:",
    options=all_genres,
    default=["Action", "Adventure"]
)

num_recommendations = st.sidebar.slider("Number of Recommendations", 5, 20, 10)

# HYBRID GENRE RECOMMENDATION FUNCTION

# --- POSTER FETCH KARNE KA MAGIC FUNCTION ---
def get_movie_poster(movie_title):
    # 1. Title Clean karo (Bracket aur Year hatao)
    clean_title = movie_title.split('(')[0].strip()
    
    # 2. ", The" ko aage shift karo
    if ", The" in clean_title:
        clean_title = "The " + clean_title.replace(", The", "").strip()
    
    # 3. API Token (Jo aapne copy kiya tha)
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzhlM2E3MzFiOTJlZDg3NDM3YjFmMjUxODUyZGMxOCIsIm5iZiI6MTc3NDYwODAyNC43ODQsInN1YiI6IjY5YzY1ZTk4Zjg1YTU5MzgwZjg5YmY5NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.sgCWD7vHaeySKXj9qyaYZvw7BuZIWUO_1M-FPy-w_Xw" # <--- Yahan apna poora token check kar lena ek baar
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json;charset=utf-8"
    }
    
    # Search URL
    url = f"https://api.themoviedb.org/3/search/movie?query={clean_title}"
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if data['results']:
            poster_path = data['results'][0]['poster_path']
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except:
        pass
    
    return "https://via.placeholder.com/500x750?text=No+Poster+Found"

def hybrid_genre_recommend(selected_genres, n=10):
    if not selected_genres:
        return []
    
    selected_set = set(selected_genres)
    
    #Exact genre matches only
    exact_matches = movies_df[movies_df['genres'].apply(lambda x: set(x.split('|')) == selected_set)]
    exact_matches = exact_matches.sort_values(by='rating', ascending=False)
    exact_list = exact_matches['title'].tolist()
    
    #Partial matches: include all selected genres but may have extra
    def extra_genres_count(x):
        x_set = set(x.split('|'))
        if selected_set.issubset(x_set) and x_set != selected_set:
            return len(x_set - selected_set)
        else:
            return np.nan

    partial_matches = movies_df.copy()
    partial_matches['extra_count'] = partial_matches['genres'].apply(extra_genres_count)
    partial_matches = partial_matches.dropna(subset=['extra_count'])
    
    # Sort by rating DESC, then extra genres ASC
    partial_matches = partial_matches.sort_values(by=['rating', 'extra_count'], ascending=[False, True])
    partial_list = partial_matches['title'].tolist()
    
    # Combine exact + partial, remove duplicates, limit to n
    final_list = list(dict.fromkeys(exact_list + partial_list))  # removes duplicates while keeping order
    return final_list[:n]

if st.button("🎬 Get Recommendations"):

    my_bar = st.progress(0)

    for i in range(100):
      time.sleep(0.02)
      my_bar.progress(i+1)

    final_movies = hybrid_genre_recommend(selected_genres, num_recommendations)

    with st.spinner('CineMatch AI is analyzing your mood and scanning the database...'):
      time.sleep(1.5) # Yeh 1.5 second ka artificial delay dega real feel ke liye
      st.balloons()   # Jab result aaye toh thoda celebration ho!

    if not final_movies:
      st.warning("No movies found for the selected genres.")
    else:
      st.markdown("### Recommended Movies")
    for i, movie in enumerate(final_movies, 1):
      # 1. Movie Title with Emoji
        st.markdown(f"### 🎬 {movie}")

        # 2. Poster Fetch
        with st.spinner(f'Loading poster for {movie}...'):
            poster_url = get_movie_poster(movie)
            st.image(poster_url, width=300)

        # 3. Rating fetch (Aapke second image jaisa)
        m_row = movies_df[movies_df['title'] == movie].iloc[0]
        rating = m_row['rating']
        genres = m_row['genres'].replace('|', ' | ')

        st.write(f"**Genre:** {genres} | **Rating:** ⭐ {rating}")
       
      # 4. Watch Trailer Button
        search_query = movie.replace(" ", "+") + "+trailer"
        trailer_link = f"https://www.youtube.com/results?search_query={search_query}"
        
        st.markdown(f"""
            <a href="{trailer_link}" target="_blank" style="text-decoration: none;">
                <button style="background-color: #e50914; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;">
                    ▶ Watch Trailer on YouTube
                </button>
            </a>
        """, unsafe_allow_html=True)
        
        st.write("---") # Partition line 
       
st.markdown("---")
st.caption("Hybrid content + collaborative genre-based recommendation: exact matches first, then include movies with extra genres, sorted by rating")

# Fill missing genres
st.sidebar.markdown("---")
st.sidebar.subheader("Smart Personalization")

# 1. Mood Selection
user_mood = st.sidebar.selectbox("Select Your Current Mood:", ["Any","Happy", "Sad", "Demotivated", "Thrilled", "Bored", "Romantic"])

# 2. Time based Selection
time_of_day = st.sidebar.selectbox("Select Time of Day:",["Anytime", "Morning(Short Movies)", "Afternoon(Quick)", "Evening(Long Movies)", "Night(Binge-Watching)"])

# 3. Social Selection
watching_with = st.sidebar.selectbox("Who are you watching with?", ["Alone", "Friends", "Family", "Partner", "Kids", "Siblings"])

# --- STEP 2: ACTUAL FILTERING LOGIC ---

# 1. Pehle pure data ki ek copy banaiye
filtered_df = movies_df.copy()

# 2. MOOD LOGIC (Matching your sidebar options)
if user_mood == "Happy":
    filtered_df = filtered_df[filtered_df['genres'].str.contains('Comedy|Children|Animation|Fantasy', case=False, na=False)]
elif user_mood == "Sad":
    filtered_df = filtered_df[filtered_df['genres'].str.contains('Drama|Romance', case=False, na=False)]
elif user_mood == "Demotivated":
    filtered_df = filtered_df[filtered_df['genres'].str.contains('War|Western|Drama|Musical', case=False, na=False)]
elif user_mood == "Thrilled":
    filtered_df = filtered_df[filtered_df['genres'].str.contains('Action|Thriller|Mystery|Horror|Crime', case=False, na=False)]
elif user_mood == "Bored":
    filtered_df = filtered_df[filtered_df['genres'].str.contains('Drama|Sci-Fi|Fantasy', case=False, na=False)]
elif user_mood == "Romantic":
    filtered_df = filtered_df[filtered_df['genres'].str.contains('Romance', case=False, na=False)]

# 3. SOCIAL LOGIC (Including Kids, Siblings, Partner from your photo)
if watching_with in ["Family", "Kids", "Siblings"]:
    # Inke liye hamesha clean aur family genres filter honge
    filtered_df = filtered_df[filtered_df['genres'].str.contains('Animation|Comedy|Family|Drama', case=False, na=False)]
elif watching_with == "Friends":
    filtered_df = filtered_df[filtered_df['genres'].str.contains('Horror|Action|Sci-Fi|Comedy', case=False, na=False)]
elif watching_with == "Partner":
    filtered_df = filtered_df[filtered_df['genres'].str.contains('Romance|Drama|Mystery', case=False, na=False)]

# 4. TIME LOGIC (Morning vs Evening vs Night)
if "Morning" in time_of_day:
    # Morning ke liye light aur fresh content
    filtered_df = filtered_df[filtered_df['genres'].str.contains('Adventure|Animation', case=False, na=False)]
elif "Evening" in time_of_day or "Night" in time_of_day:
    # Der raat ke liye Thriller ya Binge-worthy Drama
    filtered_df = filtered_df[filtered_df['genres'].str.contains('Thriller|Crime|Drama|Mystery', case=False, na=False)]
elif "Afternoon" in time_of_day:
    # Dopahar ke liye short/quick genres
    filtered_df = filtered_df[filtered_df['genres'].str.contains('Comedy|Children', case=False, na=False)]

# --- STEP 3: SHOW RESULTS ON SCREEN ---

st.write("---") # Ek separator line banayega
st.subheader("Recommended for You 🎬")

# Hum top 10 movies dikhayenge jo filters se match karti hain
top_results = filtered_df.head(10)

if not top_results.empty:
        # Loop chalakar ek-ek karke dikhao
        for index, row in top_results.iterrows():
            # 🎬 1. Movie Title (Bade font mein)
            st.markdown(f"### 🎬 {row['title']}")
            
            # 🖼️ 2. Poster Fetch (Humaara naya function)
            with st.spinner(f"Loading poster for {row['title']}..."):
                poster_url = get_movie_poster(row['title'])
                st.image(poster_url, width=200)
            
            # 📝 3. Genre aur Rating
            st.write(f"**Genre:** {row['genres']} | **Rating:** ⭐ {row['rating']}")
            
            # 📺 4. YouTube Trailer Button
            search_query = row['title'].replace(" ", "+")
            trailer_link = f"https://www.youtube.com/results?search_query={search_query}+official+trailer"
            
            st.markdown(f'''
                <a href="{trailer_link}" target="_blank" style="text-decoration: none;">
                    <button style="
                        background-color: #e50914; 
                        color: white; 
                        border: none; 
                        padding: 10px 20px; 
                        border-radius: 5px; 
                        font-weight: bold;
                        cursor: pointer;">
                        ▶ Watch Trailer on YouTube
                    </button>
                </a>
            ''', unsafe_allow_html=True)
            
            st.write("---") # Ek line separator har movie ke baad
else:
    # Agar koi movie match nahi hui (Rare case)
    st.warning("No movies found for this combination. Try changing your filters from the sidebar!")

# --- PROJECT FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("Project by: Nandani Patel")
