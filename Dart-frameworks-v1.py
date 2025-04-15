import streamlit as st

# Data: Dart frameworks categorized
frameworks = {
    "Mobile and Cross-Platform": [
        {"name": "Flutter", "description": "A UI toolkit for building natively compiled applications for mobile, web, and desktop from a single codebase."}
    ],
    "Web (Frontend)": [
        {"name": "AngularDart", "description": "A framework for building dynamic, single-page web applications with a structured approach."},
        {"name": "Pheasant", "description": "A modern frontend web framework with component-based files (.phs) for Dart."},
        {"name": "OverReact", "description": "A library for building statically-typed React UI components in Dart."},
        {"name": "MDL/Dart", "description": "Material Design Lite components for responsive web applications."}
    ],
    "Server-Side (Backend)": [
        {"name": "Conduit (formerly Aqueduct)", "description": "A server-side framework for building RESTful APIs with ORM and OAuth 2.0."},
        {"name": "Angel", "description": "A full-featured backend framework with MVC, GraphQL, and WebSockets support."},
        {"name": "Shelf", "description": "A minimalistic web server middleware framework for custom solutions."},
        {"name": "Dart Frog", "description": "A modern, minimal backend framework for APIs and microservices."},
        {"name": "Start", "description": "A Sinatra-inspired lightweight web framework."},
        {"name": "Vane", "description": "A lightweight server-side framework with a middleware system."},
        {"name": "Angle", "description": "A full-stack server framework for secure, scalable web apps."},
        {"name": "Conduct", "description": "A web and server framework for enterprise-grade applications."}
    ]
}

# Streamlit app
def main():
    # Title of the app
    st.title("Dart Frameworks Explorer")

    # Dropdown at the top for selecting framework category
    category = st.selectbox(
        "Select a Framework Category",
        options=list(frameworks.keys()),
        index=0  # Default to the first category
    )

    # Display the list of frameworks for the selected category
    st.subheader(f"Frameworks in {category}")
    for framework in frameworks[category]:
        with st.expander(framework["name"]):
            st.write(framework["description"])

if __name__ == "__main__":
    main()
