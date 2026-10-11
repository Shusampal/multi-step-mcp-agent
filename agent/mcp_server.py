import random
import secrets
import string
from datetime import datetime

from fastmcp import FastMCP


mcp = FastMCP("my-tools-mcp")


@mcp.tool()
def get_current_time() -> str:
    """Return the current local system date and time as a formatted string."""
    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


@mcp.tool()
def roll_dice() -> int:
    """Roll one six-sided die and return its result as an integer from 1 to 6."""
    return random.randint(1, 6)


@mcp.tool()
def generate_password() -> str:
    """Generate a cryptographically secure password.
    """

    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(12))


if __name__ == "__main__":
    mcp.run()
