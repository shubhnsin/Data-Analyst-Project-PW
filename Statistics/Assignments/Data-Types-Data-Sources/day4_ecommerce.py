# ------------------------------------------------------------
# Day 4: Real-Life Project – E-commerce System
# Task:
# 1. Design a product catalog using a suitable data structure
# 2. Simulate user reviews in JSON format and analyze them
# 3. Explain how product images (unstructured data) are handled
# ------------------------------------------------------------

import json  # Used to parse JSON review data


class EcommerceBackend:
    def __init__(self):
        # Task 1: Product Catalog
        # Using a list of dictionaries to store product details
        self.product_catalog = [
            {"id": 101, "name": "Gaming Laptop", "price": 1500.00, "category": "Electronics"},
            {"id": 102, "name": "Wireless Mouse", "price": 45.50, "category": "Accessories"},
            {"id": 103, "name": "Mechanical Keyboard", "price": 85.00, "category": "Accessories"}
        ]

    def display_catalog(self):
        # Display product catalog in a readable format
        print("--- Product Catalog ---")
        print(f"{'ID':<5} | {'Name':<20} | {'Price':<10}")
        print("-" * 40)

        for product in self.product_catalog:
            print(
                f"{product['id']:<5} | "
                f"{product['name']:<20} | "
                f"${product['price']:<10.2f}"
            )
        print()

    def analyze_reviews(self, json_data):
        # Task 2: Analyze user reviews stored in JSON format
        print("--- Review Analysis ---")

        # Convert JSON string into Python objects
        reviews = json.loads(json_data)

        # Dictionary to store ratings for each product
        product_ratings = {}

        # Collect ratings for each product
        for review in reviews:
            product_id = review["product_id"]
            rating = review["rating"]

            if product_id not in product_ratings:
                product_ratings[product_id] = []

            product_ratings[product_id].append(rating)

        # Calculate and display average rating per product
        print("Average Ratings per Product:")
        for product_id, ratings in product_ratings.items():
            average_rating = sum(ratings) / len(ratings)

            # Find product name for display
            product_name = next(
                (p["name"] for p in self.product_catalog if p["id"] == product_id),
                "Unknown Product"
            )

            print(
                f"Product: {product_name} (ID: {product_id}) "
                f"-> Average Rating: {average_rating:.1f}/5.0"
            )

    def handle_images_explanation(self):
        # Task 3: Explain handling of unstructured image data
        print("\n--- Image Handling Strategy ---")
        print("1. User uploads image through frontend.")
        print("2. Backend validates file type and size.")
        print("3. Image is stored in cloud storage (e.g., AWS S3).")
        print("4. Image URL is saved in the database with product ID.")


# Program execution starts here
if __name__ == "__main__":
    ecommerce = EcommerceBackend()

    # Display the product catalog
    ecommerce.display_catalog()

    # Simulated JSON review data
    raw_reviews_json = """
    [
        {"review_id": 1, "product_id": 101, "user": "UserA", "rating": 5, "comment": "Great laptop!"},
        {"review_id": 2, "product_id": 101, "user": "UserB", "rating": 4, "comment": "Good but expensive."},
        {"review_id": 3, "product_id": 102, "user": "UserC", "rating": 2, "comment": "Stopped working."}
    ]
    """

    # Analyze reviews
    ecommerce.analyze_reviews(raw_reviews_json)

    # Explain image handling
    ecommerce.handle_images_explanation()
