# StudentName: Olorode Feyisyomi
import tkinter as tk
import random
import requests
from datetime import datetime, timedelta

# Write the code to generate the news in this function
def generate_headline(field: str):
    ''' Make your API call, do not forget the field.
    previous date gets the current date,subtracts a day from it and then returns it
    in the yyyy/mm/dd format'''
    previous_date =(datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    api_key = 'ad82bd4fd4fc4061b2122ae119eabc7f'
    URL = (f"https://newsapi.org/v2/everything?q={field}&from={previous_date}&sortBy=popularity&apikey={api_key}")
    
    # Process the data and replace the empty string with the processed string
    try:
        # Make the API call
        response = requests.get(URL)
        response.raise_for_status()  # Raise an error for unsuccessful responses
        data = response.json()
        '''iterates through the loop and search's for an article with more than one
        result,uses random.choice too select a random article,gets the date using
        the keyword "published AT" but removes the timestamp'''
        
        if 'articles' in data and len(data['articles']) > 0:
            # Select a random article
            random_article = random.choice(data['articles'])
            date = random_article.get("publishedAt", "").split("T")[0]  # Extract date
            headline = random_article.get("title", "No title available")  # Extract headline
            author = random_article.get("author", "Unknown author")  # Extract author
            
            # Format and return the headline
            return f"{date}\n{headline}\n- {author}"
        else:
            return "No articles found for this category."
    
    except requests.exceptions.HTTPError as http_err:
        processed_headline = f"HTTP error occurred: {http_err}"
    except Exception as err:
        processed_headline = f"An error occurred: {err}"
    return processed_headline


#   !!!! Do not write any code below this line !!!!


news_categories = ["Sport", "Bitcoin", "Politics", "Movies", "Coding"]


# Function to get a random headline from the selected field
def get_random_headline():
    field = selected_field.get()
    return generate_headline(field)
# Function to update the displayed headline
def refresh_headline():
    headline_label.config(text=get_random_headline())


# Create the main window
root = tk.Tk()
root.title("Random News Headlines")
root.geometry("500x350")
root.configure(bg="#f3f4f6")

# Variable to store the selected field
selected_field = tk.StringVar(value="Sports")

# Create a frame for aesthetics
frame = tk.Frame(root, bg="#ffffff", relief=tk.RAISED, bd=2)
frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER, width=450, height=250)

# Add a dropdown menu to select the field
field_label = tk.Label(
    root,
    text="Random News\nHeadlines",
    font=("Hobo std", 17, "bold"),
    bg="#f3f4f6"
)
field_label.place(relx=0.2, rely=0.1, anchor=tk.CENTER)

# Add a dropdown menu to select the field
field_label = tk.Label(
    root,
    text="Select Field:",
    font=("Helvetica", 13, "bold"),
    bg="#f3f4f6"
)
field_label.place(relx=0.8, rely=0.08, anchor=tk.CENTER)

field_dropdown = tk.OptionMenu(
    root,
    selected_field,
    *news_categories
)
field_dropdown.config(font=("Helvetica", 10, "bold"), bg="dark slate gray", fg="white")
field_dropdown.place(relx=0.8, rely=0.15, anchor=tk.CENTER)

# Add a label for the headline
headline_label = tk.Label(
    frame,
    text=get_random_headline(),
    wraplength=400,
    font=("Helvetica", 14, "bold"),
    fg="#333333",
    bg="#ffffff",
    justify="center"
)
headline_label.pack(pady=20)

# Add a refresh button
refresh_button = tk.Button(
    frame,
    text="Refresh",
    font=("Helvetica", 12, "bold"),
    bg="#007bff",
    fg="#ffffff",
    activebackground="#0056b3",
    activeforeground="#ffffff",
    command=refresh_headline
)
refresh_button.pack(pady=10)

# Run the application
root.mainloop()
