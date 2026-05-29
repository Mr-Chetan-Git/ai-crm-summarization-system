import sys
import os

current_dir = os.path.dirname(__file__)

transformer_path = os.path.join(
    current_dir,
    "transformer",
    "Transformer-main"
)

sys.path.append(transformer_path)

from run_project import generate_summary_text


def generate_text(prompt):

    return generate_summary_text(prompt)