def show():
    try:
        print("Inside try block")
        # Uncomment the next line to simulate an exception
        # raise ValueError("An error occurred!")
    except ValueError as e:
        print(f"Caught an exception: {e}")
    finally:
        print("Executing finally block")