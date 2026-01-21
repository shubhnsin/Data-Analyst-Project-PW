# ------------------------------------------------------------
# Day 3: Structured, Semi-Structured, and Unstructured Data
# Task:
# 1. Load and display structured data (CSV format)
# 2. Load and analyze semi-structured data (JSON format)
# 3. Explain how unstructured data can be processed
# ------------------------------------------------------------

import pandas as pd        # Used for handling structured data (CSV)
import json                # Used for handling JSON data
import io                  # Used to simulate file input


def analyze_structured_data():
    # This function demonstrates structured data handling
    print("\n--- Analyzing Structured Data (CSV) ---")

    # Simulated CSV content (as if read from a file)
    csv_content = """Date,Product,Sales
2023-10-01,Laptop,1200
2023-10-02,Mouse,25
2023-10-02,Keyboard,45
"""

    # Load CSV data into a DataFrame
    df = pd.read_csv(io.StringIO(csv_content))

    # Display the structured data
    print("Data Loaded:")
    print(df)

    # Display basic statistics of numeric columns
    print("\nSummary Statistics:")
    print(df.describe())


def analyze_semi_structured_data():
    # This function demonstrates semi-structured data handling
    print("\n--- Analyzing Semi-Structured Data (JSON) ---")

    # Simulated JSON data (as if received from an API)
    json_content = """
    [
        {
            "user_id": 1,
            "name": "Alice",
            "posts": [
                {"id": 101, "likes": 25},
                {"id": 102, "likes": 50}
            ]
        },
        {
            "user_id": 2,
            "name": "Bob",
            "posts": []
        }
    ]
    """

    # Parse JSON string into Python objects
    data = json.loads(json_content)

    # Analyze parsed JSON data
    print("Parsed JSON Data:")
    for user in data:
        post_count = len(user["posts"])
        print(f"User: {user['name']}, Total Posts: {post_count}")

        # Calculate total likes if posts exist
        if post_count > 0:
            total_likes = sum(post["likes"] for post in user["posts"])
            print(f"  - Total Likes: {total_likes}")


def analyze_unstructured_data_plan():
    # This function explains how unstructured data can be handled
    print("\n--- Unstructured Data Processing Plan ---")
    print("Example: Image Data Analysis")
    print("1. Load images using libraries like PIL or OpenCV.")
    print("2. Preprocess images (resize, normalize).")
    print("3. Extract features using a CNN model.")
    print("4. Classify images into categories.")


# Program execution starts here
if __name__ == "__main__":
    analyze_structured_data()
    analyze_semi_structured_data()
    analyze_unstructured_data_plan()
