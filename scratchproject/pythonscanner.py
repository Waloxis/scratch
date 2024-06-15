import os
from creatinghtml import x

                

def modify_file(file_path, new_content, insert_after):
        try:
            # Check if the file exists
            if not os.path.exists(file_path):
                print(f"File '{file_path}' does not exist.")
                return False
            
            # Open the file in read mode and read its content
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Find the insertion point
            insert_index = None
            for i, line in enumerate(lines):
                if insert_after in line:
                    insert_index = i + 1
                    break
            
            if insert_index is None:
                print(f"'{insert_after}' not found in the file.")
                return False
            
            # Insert the new content with proper formatting
            lines.insert(insert_index, new_content + '\n')
            
            # Open the file in write mode and write the updated content back to the file
            with open(file_path, 'w') as file:
                file.writelines(lines)
            
            print(f"New content has been inserted into '{file_path}'.")
            return True
        except Exception as e:
            print(f"Error modifying file: {e}")
            return False

if __name__ == "__main__":
        file_path = "/Users/walidsphone./Desktop/scratchproject/games.js"  # Replace with your file path
        new_content = f'''        {{
                "name": "New Game",
                "path": "Games/GameFiles/{x}",
                "thumbnailpath":"Games/GameThumbnails/New Game.svg"
            }},''' # The new content to be added to the file
        
        if x != '':
            insert_after = '"files": ['  # Line after which the new content should be inserted
            modify_file(file_path, new_content, insert_after)