from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering theh context")
    resource = "Resource acquired"
    yield resource


with my_context() as r:
    print(f"Inside the context: {r}")