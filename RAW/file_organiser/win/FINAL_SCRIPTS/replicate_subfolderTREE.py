import os

def replicate_subfolder_tree(source_path, target_path):
    """
    Replicate the subfolder tree from the source path to the target path.

    Parameters:
    - source_path (str): The path to the source directory.
    - target_path (str): The path to the target directory.
    """
    # Ensure the target directory exists
    if not os.path.exists(target_path):
        os.makedirs(target_path, mode=0o755, exist_ok=True)
    
    # List all items in the source directory
    items = os.listdir(source_path)
    
    # Iterate through each item
    for item in items:
        item_path = os.path.join(source_path, item)
        
        # If the item is a directory, replicate its subfolder tree
        if os.path.isdir(item_path):
            # Skip replication if the item is the "source_replica" subfolder
            if item == "source_replica":
                print("Skipping replication of 'source_replica' subfolder.")
                continue
            
            new_target_path = os.path.join(target_path, item)
            replicate_subfolder_tree(item_path, new_target_path)

# Global declarations
working_directory = r"E:\sorted Youtube vids 2023_2024\YT2024"
replica = r"E:\sorted Youtube vids 2023_2024\2024\source_replica"

# Main function to replicate the subfolder tree
def main():
    replicate_subfolder_tree(working_directory, replica)
    print(f"Subfolder tree replicated from {working_directory} to {replica}")

if __name__ == "__main__":
    main()
