[app]

# Your app title
title = SpamFilterApp

# Package name for your app
package.name = spam_filter_app

# Domain for your app package
package.domain = org.streamlit

# Source directory
source.dir = .

# App version
version = 1.0.0

# Orientation of the app (portrait or landscape)
orientation = portrait

# List of files to include in the package
source.include_exts = py,csv

# List of requirements (Python dependencies) to include
[requirements]
python = 3.8.10
streamlit = 1.5.0
pandas
scikit-learn
