# v0.1.0
# { "Depends": "py-genlayer:latest" }

# This header is mandatory and must be on the first line. 
# Using "latest" should work in the current Studio environment.

from genlayer import *

# The class must extend gl.Contract to be recognized as a valid Intelligent Contract.
class Storage(gl.Contract):
    # Persistent storage fields must be declared here.
    # Note: Using u256 for unsigned 256-bit integers.
    storage_str: str
    storage_int: u256  

    # The constructor sets the initial state of the contract.
    def __init__(self, initial_str_storage: str):
        self.storage_str = initial_str_storage
        self.storage_int = 0

    # View methods allow reading state without modifying it.
    @gl.public.view
    def get_storage(self) -> str:
        """Returns the current string stored in the contract."""
        return self.storage_str

    # Debug method to demonstrate logging (only for off-chain/debug purposes).
    @gl.public.view
    def debug(self, x: u256, *, flag: bool) -> None:
        """Prints debug information to the console."""
        print(f"Debug info: {self.storage_int}, {x}, {flag}")

    # Write methods modify the persistent storage of the contract.
    @gl.public.write
    def update_storage(self, new_storage: str) -> None:
        """Updates the stored string with a new value."""
        self.storage_str = new_storage
        
    # Example of a write method to update the integer storage.
    @gl.public.write
    def update_int(self, new_val: u256) -> None:
        """Updates the stored integer value."""
        self.storage_int = new_val
