# Translation Guide for Python Deadlines

[![Crowdin](https://badges.crowdin.net/python-deadlines/localized.svg)](https://crowdin.com/project/python-deadlines)

Thank you for your interest in helping translate the Python Deadlines website! This document explains how to contribute translations using Crowdin.

## What is Crowdin?

[Crowdin](https://crowdin.com) is a localization management platform that helps us manage translations for the Python Deadlines website. It provides a user-friendly interface for translators to contribute without needing to understand Git or the technical structure of the project.

## How to Join as a Translator

1. Visit our Crowdin project at [https://crowdin.com/project/python-deadlines](https://crowdin.com/project/python-deadlines) (Note: Update this URL with your actual project link)
2. Create a Crowdin account or sign in if you already have one
3. Select the language you want to translate to
4. Start translating!

## Project Structure

The Python Deadlines website uses Jekyll's internationalization features. Here's how the translation files are structured:

-   `_i18n/en.yml`: Main language file containing UI strings
-   `_i18n/en/*.md`: Markdown files for specific sections
-   `_i18n/en/_posts/`: Blog post content
-   `_i18n/en/search`, `_i18n/en/footer`, etc.: Section-specific content

## Translation Guidelines

### General Tips

1. **Maintain the same formatting**: Preserve Markdown formatting, HTML tags, and variables (like `{% t ... %}` or `{{ ... }}`)
2. **Be consistent**: Use consistent terminology throughout your translations
3. **Keep the same meaning**: Focus on conveying the same meaning rather than translating word-for-word
4. **Respect context**: Pay attention to the context in which a string appears
5. **Test your translations**: If possible, test how your translations look on the site

### Variables and Special Syntax

When translating, be careful with:

-   **Jekyll Liquid tags**: Tags like `{% t ... %}`, `{{ ... }}`, `{% include ... %}` should remain unchanged
-   **HTML tags**: Keep all HTML tags (e.g., `<div>`, `<span>`, `<a href="...">`) intact
-   **Pluralization**: Some languages have different forms based on count; Crowdin supports handling these cases

### Date and Time Formats

Pay attention to date and time formats that may be different in your language. The website uses Luxon for date/time formatting.

## Translation Workflow

1. **String Translation**: Translate strings in the Crowdin interface
2. **Review**: Translations are reviewed by language moderators
3. **Integration**: Approved translations are automatically synced to the GitHub repository
4. **Deployment**: Once merged into the main branch, translations are deployed to the live site

## Testing Your Translations

If you would like to test your translations locally before submitting:

1. Clone the repository: `git clone https://github.com/JesperDramsch/python-deadlines.git`
2. Install Jekyll and dependencies: `bundle install`
3. Run the site locally: `bundle exec jekyll serve`
4. Visit `http://localhost:4000/{language-code}/` to see the site in your language

## Supported Languages

Currently, Python Deadlines is being translated into:

-   English (source language)
-   Spanish (es)
-   German (de)
-   French (fr)
-   Portuguese (Brazilian) (pt-br)
-   Chinese (Simplified) (zh-cn)
-   Russian (ru)
-   Indonesian (id)
-   Hindi (hi)

If you would like to add a new language, please contact the project maintainers.

## Contact

If you have any questions or issues related to translation, please:

-   Open an issue on GitHub

Thank you for helping make Python Deadlines accessible to a wider audience!
