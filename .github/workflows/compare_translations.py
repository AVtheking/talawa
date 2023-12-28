"""
Script to encourage more efficient coding practices.

Methodology:

    Utility for comparing translations between default and other languages.

    This module defines a function to compare two translations
    and print any missing keys in the other language's translation.

Functions:
    compare_translations(default_translation, other_translation, language):
        Compare two translations and print missing keys.

    check_translations():
        Load the default translation and compare it with other translations.

Usage:
    This script can be executed to check and print missing
    translations in other languages based on the default English translation.

Example:
    python compare_translations.py
NOTE:
    This script complies with our python3 coding and documentation standards
    and should be used as a reference guide. It complies with:

        1) Pylint
        2) Pydocstyle
        3) Pycodestyle
        4) Flake8

"""
# standard imports
import json
import os
import sys


def compare_translations(default_translation, other_translation):
    """Compare two translations and print missing keys.

    Args:
        default_translation: The default translation
        other_translation: The other translation


    Returns:
        missing_translations: List of missing translations


    """
    missing_translations = []

    for key in default_translation:
        if key not in other_translation:
            missing_translations.append(key)

    return missing_translations


def load_translation(filepath):
    """Load translation from a file.

    Args:
        filepath: Path to the translation file

    Returns:
        translation: Loaded translation


    """
    with open(filepath, "r", encoding="utf-8") as file:
        translation = json.load(file)
    return translation


def check_translations():
    """Load default translation and compare with other translations."""
    default_translation = load_translation("lang/en.json")
    translations_dir = "lang"
    translations = os.listdir(translations_dir)
    translations.remove("en.json")  # Exclude default translation

    all_missing_translation = []

    for file in translations:
        translation_path = os.path.join(translations_dir, file)
        other_translation = load_translation(translation_path)

        # Compare translations
        missing_translations = compare_translations(
            default_translation, other_translation
        )
        if missing_translations:
            all_missing_translation.append((file, missing_translations))
        # Print missing translations

    for file, missing_translations in all_missing_translation:
        if missing_translations:
            print(f"Translations missing in {translations_dir}/{file} are")
        for key in missing_translations:
            print(f" {key}")

    if all_missing_translation:
        sys.exit(1)  # Exit with an error status code
    else:
        print("All translations are present")
        sys.exit(0)


if __name__ == "__main__":
    check_translations()
    # Exit with a success status code
