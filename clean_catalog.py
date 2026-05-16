import json


def clean_catalog():
    input_file = "shl_catalog.json"
    output_file = "shl_catalog_clean.json"

    bad_keywords = [
        "Report",
        "Guide",
        "Profile",
        "Cards",
        "Interview",
        "Job Focused",
        "JFA",
        "Solution",
        "Narrative",
        "Development",
        "Participant",
        "Selection"
    ]

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            catalog = json.load(file)

        clean_items = []
        removed_items = []

        for item in catalog:
            item_name = str(item.get("name", ""))

            is_bad = False

            for keyword in bad_keywords:
                if keyword.lower() in item_name.lower():
                    is_bad = True
                    break

            if is_bad:
                removed_items.append(item)
            else:
                clean_items.append(item)

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(clean_items, file, indent=4, ensure_ascii=False)

        print("Cleanup Complete!")
        print("Original items:", len(catalog))
        print("Removed items:", len(removed_items))
        print("Clean items:", len(clean_items))
        print("Saved to:", output_file)

        print("\nRemoved examples:")
        for item in removed_items[:20]:
            print("-", item.get("name", ""))

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    clean_catalog()