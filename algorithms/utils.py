from re import S
import rich


def highlight(arr, target=None, idx=None, color="red"):
    for i, item in enumerate(arr):
        if i == idx or item == target:
            rich.print(f"[bold {color}]{item}[/bold {color}]", end=" ")
        else:
            print(item, end=" ")
    print()

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    highlight(arr, 5)