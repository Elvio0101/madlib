import os
import re
from datetime import datetime
from typing import List, Dict

# Import rich for better console output.
# If you don't have it, run: pip install rich
from rich.console import Console
from rich.prompt import Prompt, Confirm

# Initialize rich console for beautiful printing
console = Console()

TEMPLATE_DIR = 'templates'
SAVE_DIR = 'saved_stories'


def select_template() -> str | None:
    """Display available templates and let the user pick one."""
    console.print("\n[bold magenta]Available Mad Libs Templates:[/bold magenta]")
    try:
        templates = [f for f in os.listdir(TEMPLATE_DIR) if f.endswith('.txt')]
        if not templates:
            console.print("[bold red]No templates found in the 'templates' directory.[/bold red]")
            return None

        for i, template_name in enumerate(templates):
            display_name = os.path.splitext(template_name)[0].replace('_', ' ').title()
            console.print(f"  [cyan]{i + 1}[/cyan]. {display_name}")
        console.print(f"  [cyan]{len(templates) + 1}[/cyan]. Random Template")

        while True:
            try:
                choice = int(Prompt.ask("\n[bold yellow]Choose a template number[/bold yellow]", default="1"))
                if choice == len(templates) + 1:
                    template_path = os.path.join(TEMPLATE_DIR, random.choice(templates))
                elif 1 <= choice <= len(templates):
                    template_path = os.path.join(TEMPLATE_DIR, templates[choice - 1])
                else:
                    console.print("[bold red]Invalid choice. Please enter a number from the list.[/bold red]")
                    continue
                return template_path
            except ValueError:
                console.print("[bold red]Invalid input. Please enter a number.[/bold red]")

    except FileNotFoundError:
        console.print(f"[bold red]Error: The directory '{TEMPLATE_DIR}' was not found.[/bold red]")
        return None


def load_template(file_path: str) -> str:
    """Load template text from file."""
    with open(file_path, 'r') as file:
        return file.read()


def extract_placeholders(template: str) -> List[str]:
    """Extract placeholders like <noun>, <verb> from template."""
    placeholders = re.findall(r'<([^>]+)>', template)
    return list(dict.fromkeys(placeholders))


def validate_input(word: str, placeholder: str) -> bool:
    """Basic validation for user input."""
    if not word.strip():
        return False
    if placeholder.lower() == 'number':
        return word.isdigit()
    if placeholder.lower() == 'verb ending in -ing':
        return word.lower().endswith('ing')
    return True


def get_user_inputs(placeholders: List[str]) -> Dict[str, str]:
    """Ask user for inputs for each placeholder."""
    inputs = {}
    console.print("\n[bold magenta]Please provide the following words:[/bold magenta]")

    for i, ph in enumerate(placeholders, 1):
        console.print(f"  ({i}/{len(placeholders)}) Input for [green]{ph}[/green]")
        while True:
            user_input = Prompt.ask(f"  Enter a [green]{ph}[/green]").strip()

            if validate_input(user_input, ph):
                inputs[ph] = user_input
                break
            else:
                console.print(f"[yellow]Invalid input for '{ph}'. Please try again.[/yellow]")

    return inputs


def fill_template(template: str, user_inputs: Dict[str, str]) -> str:
    """Fill template with user inputs."""
    return re.sub(r'<([^>]+)>', lambda m: f"[bold cyan]{user_inputs[m.group(1)]}[/bold cyan]", template)


def save_story(story: str, template_name: str):
    """Save story to file (without colors)."""
    plain_story = re.sub(r'\[bold cyan\]|\[/bold cyan\]', '', story)
    if Confirm.ask("\n[bold yellow]Do you want to save your story?[/bold yellow]", default=False):
        os.makedirs(SAVE_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.splitext(template_name)[0]
        file_path = os.path.join(SAVE_DIR, f"{base_name}_{timestamp}.txt")
        with open(file_path, 'w') as file:
            file.write(plain_story)
        console.print(f"\n[bold green]Story saved successfully to:[/] [underline]{file_path}[/underline]")


def play_game(template_path: str = None) -> bool:
    """Run one round of the game."""
    if not template_path:
        template_path = select_template()
        if not template_path:
            return False

    try:
        template = load_template(template_path)
        placeholders = extract_placeholders(template)
        if not placeholders:
            console.print("[yellow]This template has no placeholders.[/yellow]")
            return False

        user_inputs = get_user_inputs(placeholders)
        story = fill_template(template, user_inputs)

        console.print("\n" + "=" * 50)
        console.print("[bold magenta]Here's your Mad Libs story![/bold magenta]")
        console.print("=" * 50 + "\n")
        console.print(story)
        console.print("\n" + "=" * 50)

        save_story(story, os.path.basename(template_path))

        return Confirm.ask("\n[bold yellow]Replay with the same template?[/bold yellow]", default=False)

    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        return False


def main():
    """Main game loop."""
    console.print("[bold green]Welcome to the Mad Libs Generator! 🚀[/bold green]")
    while True:
        template_path = None
        while play_game(template_path):
            pass
        if not Confirm.ask("\n[bold yellow]Do you want to play again with a new template?[/bold yellow]", default=True):
            console.print("\n[bold blue]Thanks for playing! Goodbye 👋[/bold blue]")
            break


if __name__ == "__main__":
    main()