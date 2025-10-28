"""
Inventory Management System.

A simple inventory tracking system with add, remove, and reporting functions.
"""
import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.

    Args:
        item: Name of the item to add
        qty: Quantity to add
        logs: Optional list to store log messages
    """
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove a quantity of an item from inventory.

    If the quantity reaches zero or below, the item is deleted.

    Args:
        item (str): Name of the item to remove
        qty (int): Quantity to remove
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: Item '{item}' not found in inventory")


def get_qty(item):
    """
    Get the current quantity of an item in inventory.

    Args:
        item (str): Name of the item

    Returns:
        int: Current quantity of the item
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file (str): Path to the JSON file to load from
    """
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with empty inventory.")
        stock_data = {}


def save_data(file="inventory.json"):
    """
    Save current inventory data to a JSON file.

    Args:
        file (str): Path to the JSON file to save to
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data, indent=2))


def print_data():
    """
    Print a formatted report of all items in inventory.
    """
    print("Items Report")
    for item in stock_data:
        print(item, "->", stock_data[item])


def check_low_items(threshold=5):
    """
    Check for items with quantity below a threshold.

    Args:
        threshold (int): Minimum quantity threshold (default: 5)

    Returns:
        list: List of item names below the threshold
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """
    Main function to demonstrate inventory system operations.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    # removed this dangerous line :eval("print('eval used')")  # dangerous


main()
