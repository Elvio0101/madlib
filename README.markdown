# MADLIB GENERATOR

A **simple interactive story generator** built with Streamlit, allowing users to create fun, customized stories by filling in the blanks using predefined templates.

## FEATURES

- **Choose Your Adventure**: Select from various story templates (e.g., Fantasy Adventure, Mystery Detective).
- **Personalize Your Story**: Input custom words to fill placeholders in the selected template.
- **Instant Story Creation**: Generate and view your completed story with a single click.
- **Save Your Masterpiece**: Save your generated story as a text file with a timestamp for easy access.

## PREREQUISITES

To run the MadLib Generator, ensure you have the following:

- **Python**: Version 3.7 or higher
- **Required Packages**:
  - `streamlit`
  - `re`
- **Directory Setup**:
  - `templates/` (contains `.txt` files with story templates)
  - `saved_stories/` (where generated stories will be saved)

## INSTALLATION

1. **Clone or Download**:
   - Clone the repository or download the project files.
2. **Install Dependencies**:
   ```bash
   pip install streamlit
   ```
3. **Verify Directory Structure**:
   Ensure the following structure is in place:
   ```
   MadLib Generator/
   ├── templates/
   │   ├── fantasy_adventure.txt
   │   ├── history_lesson.txt
   │   ├── mystery_detective.txt
   │   └── spacy_odyssey.txt
   ├── saved_stories/
   │   └── (generated files, e.g., fantasy_adventure_20250928_124200.txt)
   ├── main.py
   ├── image.png
   ├── image-1.png
   ├── image-2.png
   ├── image-3.png
   ├── image-4.png
   └── README.md
   ```

## USAGE

1. **Launch the App**:
   Run the Streamlit app from your terminal:
   ```bash
   streamlit run main.py
   ```
2. **Interact with the App**:
   - Select a story template from the dropdown menu.
   - Enter words for each placeholder prompted.
   - Click **✨ Generate Story** to view your completed story.
   - Click **💾 Save Story** to save the story to the `saved_stories` directory.

## UI SCREENSHOTS

Below are screenshots of the MadLib Generator's user interface:
![alt text](image-5.png)
![alt text](image-6.png)
## OUTPUT
![alt text](image-7.png)
![alt text](image-8.png)

## CUSTOMIZATION

- **Add New Templates**:
  - Create new `.txt` files in the `templates` directory.
  - Use placeholders in the format `<placeholder>` (e.g., `<noun>`, `<verb>`).
- **Style the App**:
  - Modify the CSS in `main.py` under the **Page Styling** section to customize the app's appearance.

## TROUBLESHOOTING

- **Directory Permissions**:
  - Ensure write permissions are granted for the `saved_stories` directory.
- **Story Saving Issues**:
  - Check the console for permission or file path errors if the story doesn't save.
- **Template Errors**:
  - Verify all template files in the `templates` directory are valid `.txt` files with proper placeholders.

## LICENSE

This project is **open-source**. Feel free to modify, distribute, or enhance it as needed.