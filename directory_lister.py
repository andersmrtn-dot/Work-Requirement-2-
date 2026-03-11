import os

def list_directory(path):
    try:
        items = os.listdir(path)

        if not items:
            print(f"\n📂 '{path}' is empty.")
            return

        folders = sorted([item for item in items if os.path.isdir(os.path.join(path, item))])
        files   = sorted([item for item in items if os.path.isfile(os.path.join(path, item))])
        others  = sorted([item for item in items if item not in folders and item not in files])

        print(f"\n📂 Contents of '{path}'  ({len(items)} item{'s' if len(items) != 1 else ''})\n")
        print("─" * 40)

        for folder in folders:
            print(f"  📁  {folder}/")

        for file in files:
            print(f"  📄  {file}")

        for other in others:
            print(f"  ❓  {other}")

        print("─" * 40)
        print(f"  {len(folders)} folder(s)   {len(files)} file(s)")

    except FileNotFoundError:
        print(f"\n❌ Error: The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"\n❌ Error: '{path}' is not a directory.")
    except PermissionError:
        print(f"\n❌ Error: Permission denied — cannot access '{path}'.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


def main():
    print("=" * 40)
    print("       📂  Directory Lister")
    print("=" * 40)

    while True:
        path = input("\nEnter directory path (or 'quit' to exit): ").strip()
        if path.lower() in ("quit", "exit", "q"):
            print("\nGoodbye! 👋")
            break
        list_directory(path)

if __name__ == "__main__":
    main()
